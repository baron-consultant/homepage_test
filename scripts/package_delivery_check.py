"""Check optimized assets, rendered SVGs, scrolling and package navigation locally."""
import json
from io import BytesIO
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.perf-tools'))
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

OUT = ROOT / 'artifacts/performance/latest-20260915'
BASE = 'http://baron.test'
manifest = json.loads((OUT/'asset-optimizations.json').read_text(encoding='utf-8'))
routes = list(dict.fromkeys(r['route'] for r in json.loads((OUT/'before.json').read_text(encoding='utf-8'))))
result = {'assets': [], 'svgComparisons': [], 'pages': []}
svg_only = '--svg-only' in sys.argv

def save():
    (OUT/('svg-render-check.json' if svg_only else 'delivery-check.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')

with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='msedge',headless=True)
    context = browser.new_context(viewport={'width':1365,'height':768})
    for asset in ([] if svg_only else manifest['assets']):
        response = context.request.get(BASE+'/'+asset['output'])
        result['assets'].append({'path':asset['output'],'status':response.status,'bytes':len(response.body()),'expectedBytes':asset['afterBytes']})
    page = context.new_page()
    # Browser rasterization verifies support for embedded WebP inside SVG.
    for asset in manifest['assets']:
        if not asset['output'].endswith('.svg'):
            continue
        shots = []
        phases = [500,1500,2500,3500,4500,5500]
        for path in (asset['source'],asset['output']):
            page.goto(BASE+'/'+path,wait_until='load')
            page.wait_for_timeout(300)
            frames=[]
            for ms in phases:
                page.evaluate('''ms => {
                    for(const a of document.getAnimations()) {a.pause();a.currentTime=ms;}
                    const svg=document.documentElement;
                    if(svg.pauseAnimations) {svg.pauseAnimations();svg.setCurrentTime(ms/1000);}
                }''',ms)
                frames.append(Image.open(BytesIO(page.screenshot())).convert('RGB'))
            shots.append(frames)
        identical=[ImageChops.difference(a,b).getbbox() is None for a,b in zip(*shots)]
        result['svgComparisons'].append({'path':asset['output'],'identicalBrowserPixels':all(identical),'animationTimesMs':phases,'identicalAtEachTime':identical})
    context.close()
    save()
    if svg_only:
        browser.close()
        print(json.dumps(result['svgComparisons']),flush=True)
        sys.exit(0)
    for width,height in ((1365,768),(390,844)):
        selected = routes + [r.replace('/ko/','/en/',1) for r in routes] if width==1365 else routes
        for route in selected:
            if not (ROOT/route.lstrip('/')).exists():
                continue
            context = browser.new_context(viewport={'width':width,'height':height},locale='ko-KR')
            page = context.new_page()
            errors, bad_responses = [], []
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('response',lambda r:bad_responses.append({'url':r.url,'status':r.status}) if r.status>=400 else None)
            row = {'route':route,'viewport':[width,height]}
            try:
                page.goto(BASE+route,wait_until='load',timeout=30000)
                page.wait_for_timeout(1000)
                row['actualUrl']=page.url
                page.screenshot(path=str(OUT/f'delivery-{width}-{route.strip("/").replace("/","_")}.png'))
                row['top'] = page.evaluate('''() => ({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,headerLinks:document.querySelectorAll('header a').length,lazyImages:document.querySelectorAll('img[loading="lazy"]').length})''')
                menu = page.locator('header .btn_menu')
                if menu.count() and menu.first.is_visible():
                    menu.first.click(timeout=3000)
                    page.wait_for_timeout(250)
                    panel = page.locator('.popup_wrap.sitemap')
                    row['menuOpened']=bool(panel.count() and panel.first.is_visible())
                    close=page.locator('.popup_wrap.sitemap .btn_close')
                    if close.count() and close.first.is_visible():
                        close.first.click(timeout=3000)
                        page.wait_for_timeout(250)
                        row['menuClosed']=not panel.first.is_visible()
                samples=[]
                total=page.evaluate('document.documentElement.scrollHeight')
                # Cover scroll-triggered panels without submitting forms or opening apps.
                for step in range(21):
                    page.evaluate('(y)=>window.scrollTo(0,y)',max(0,(total-height)*step/20))
                    page.wait_for_timeout(180)
                    samples.extend(page.evaluate('''() => [...document.images].filter(i=>{const r=i.getBoundingClientRect();return r.width>0&&r.height>0&&r.bottom>0&&r.top<innerHeight}).map(i=>({src:i.currentSrc,complete:i.complete,naturalWidth:i.naturalWidth,loading:i.loading}))'''))
                page.wait_for_timeout(1200)
                row['visibleSamples']=samples
                row['brokenCompleteImages']=page.evaluate('''() => [...document.images].filter(i=>i.complete&&i.naturalWidth===0&&i.currentSrc).map(i=>i.currentSrc)''')
                row['lazyLoaded']=page.evaluate('''() => [...document.querySelectorAll('img[loading="lazy"]')].map(i=>({src:i.currentSrc,complete:i.complete,naturalWidth:i.naturalWidth}))''')
                row['guideVideoPreload']=page.locator('video.guide-video').evaluate_all('(vs)=>vs.map(v=>v.preload)')
            except Exception as e:
                row['checkError']=str(e).splitlines()[0]
            row.update(errors=errors,badResponses=bad_responses)
            result['pages'].append(row)
            save()
            print(json.dumps({'route':route,'width':width,'checkError':row.get('checkError'),'errors':len(errors),'broken':len(row.get('brokenCompleteImages',[]))}),flush=True)
            context.close()
    browser.close()
save()
