"""Read-only live timing and controlled frame-preload diagnostic."""
import collections
import copy
import json
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.perf-tools'))
from playwright.sync_api import sync_playwright
from performance_audit import OBSERVER

OUT=ROOT/'artifacts/performance/egbim-interface-live'
OUT.mkdir(parents=True,exist_ok=True)
URL='https://baroncs.co.kr/ko/egbim/interface.html'
RESULTS=[]

with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='msedge',headless=True)
    for mode in ('live','limited','limited-without-frame-preload'):
        for repeat in range(1,4):
            context=browser.new_context(viewport={'width':1365,'height':768},locale='ko-KR',service_workers='block')
            page=context.new_page();page.add_init_script(OBSERVER)
            cdp=context.new_cdp_session(page)
            cdp.send('Network.enable');cdp.send('Network.setCacheDisabled',{'cacheDisabled':True})
            if mode!='live':
                cdp.send('Network.emulateNetworkConditions',{'offline':False,'latency':40,'downloadThroughput':1250000,'uploadThroughput':625000})
                cdp.send('Emulation.setCPUThrottlingRate',{'rate':4})
            if mode=='limited-without-frame-preload':
                # Browser-only diagnostic; first frame remains available.
                cdp.send('Network.setBlockedURLs',{'urls':[f'https://baroncs.co.kr/ko/egbim/img/com_img/comp_{i}.png' for i in range(2,105)]})
            requests={};received=[0];errors=[];consoles=[]
            def requested(e):
                stack=e.get('initiator',{}).get('stack',{}).get('callFrames',[])
                requests[e['requestId']]={'url':e['request']['url'],'type':e.get('type'),'start':e['timestamp'],'initiatorType':e.get('initiator',{}).get('type'),'initiatorFrames':[{k:f.get(k) for k in ('url','lineNumber','functionName')} for f in stack[:5]]}
            def response(e):
                if e['requestId'] not in requests:return
                r=e['response'];h={k.lower():v for k,v in r.get('headers',{}).items()}
                requests[e['requestId']].update(status=r['status'],mimeType=r.get('mimeType'),responseTime=e['timestamp'],timing=r.get('timing'),headers={k:h.get(k) for k in ('content-length','content-type','content-encoding','cache-control','cf-cache-status','age')},fromDiskCache=r.get('fromDiskCache',False))
            def finished(e):
                if e['requestId'] in requests:requests[e['requestId']].update(end=e['timestamp'],encodedBytes=e.get('encodedDataLength',0))
            def failed(e):
                if e['requestId'] in requests:requests[e['requestId']].update(end=e['timestamp'],failure=e.get('errorText'),blockedReason=e.get('blockedReason'))
            cdp.on('Network.requestWillBeSent',requested);cdp.on('Network.responseReceived',response)
            cdp.on('Network.loadingFinished',finished);cdp.on('Network.loadingFailed',failed)
            cdp.on('Network.dataReceived',lambda e:received.__setitem__(0,received[0]+e.get('encodedDataLength',0)))
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('console',lambda m:consoles.append({'type':m.type,'text':m.text[:400]}) if m.type in ('error','warning') else None)
            started=time.monotonic();timeout=None
            try:page.goto(URL,wait_until='domcontentloaded',timeout=30000)
            except Exception as e:timeout=str(e).splitlines()[0]
            if mode=='live':
                try:page.wait_for_load_state('load',timeout=max(100,45000-(time.monotonic()-started)*1000))
                except Exception:pass
                page.wait_for_timeout(3000)
            else:page.wait_for_timeout(max(0,35-(time.monotonic()-started))*1000)
            metrics=page.evaluate('''()=>({...window.__perf,url:location.href,navigation:performance.getEntriesByType('navigation')[0]?.toJSON(),resources:performance.getEntriesByType('resource').map(r=>r.toJSON()),headerLinks:document.querySelectorAll('header a').length,images:[...document.images].map(i=>({src:i.currentSrc,complete:i.complete,naturalWidth:i.naturalWidth})),objects:[...document.querySelectorAll('object')].map(o=>({src:o.data,top:o.getBoundingClientRect().top,width:o.clientWidth,height:o.clientHeight,loaded:!!o.contentDocument?.documentElement}))})''')
            network=list(requests.values())
            row={'mode':mode,'run':repeat,'browser':browser.version,'observedSeconds':time.monotonic()-started,'metrics':metrics,'network':network,'receivedBytes':received[0],'errors':errors,'console':consoles,'timeout':timeout}
            RESULTS.append(copy.deepcopy(row))
            (OUT/'measurements.json').write_text(json.dumps(RESULTS,ensure_ascii=False,indent=2),encoding='utf-8')
            frames=[r for r in network if '/img/com_img/comp_' in r['url'] and r['url'].endswith('.png')]
            print(json.dumps({'mode':mode,'run':repeat,'load':metrics['navigation']['loadEventEnd'],'dcl':metrics['navigation']['domContentLoadedEventEnd'],'lcp':metrics.get('lcp'),'receivedMB':round(received[0]/1e6,2),'frameRequests':len(frames),'frameCompleted':sum('encodedBytes' in r for r in frames),'httpErrors':len([r for r in network if r.get('status',0)>=400]),'jsErrors':errors}),flush=True)
            if repeat==1:
                try:page.screenshot(path=str(OUT/(mode+'.png')),timeout=5000)
                except Exception:pass
            context.close()
    browser.close()
