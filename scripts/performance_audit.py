"""Read-only inventory and Playwright measurements. See docs/performance-audit.md."""
import argparse
import collections
import copy
import functools
import json
import re
import threading
import time
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote

# Avoid refusing bursts of parallel browser requests on Windows.
ThreadingHTTPServer.request_queue_size = 128

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.perf-tools'))
OUT = ROOT / 'artifacts/performance'
OUT.mkdir(parents=True, exist_ok=True)

def files():
    return [p for p in ROOT.rglob('*') if p.is_file() and not any(
        x in p.relative_to(ROOT).parts for x in ('.git', '.perf-tools', 'node_modules', 'artifacts'))]

def inventory():
    entries, pages, refs = [], [], []
    for p in files():
        rel = p.relative_to(ROOT).as_posix()
        entries.append({'path': rel, 'bytes': p.stat().st_size})
        if p.suffix.lower() not in ('.html', '.css', '.js'): continue
        s = p.read_text(encoding='utf-8', errors='replace')
        # Remove comments so commented-out resources do not become findings.
        s = re.sub(r'<!--.*?-->|/\*.*?\*/', '', s, flags=re.S)
        urls = re.findall(r'''(?:src|href)\s*=\s*["']([^"']+)["']|url\(\s*["']?([^\s)'";]+)''', s)
        for pair in urls:
            url = next(x for x in pair if x)
            parsed = urlsplit(url)
            if parsed.scheme or url.startswith('//'):
                if parsed.scheme in ('http','https') or url.startswith('//'):
                    refs.append({'file': rel, 'url': url, 'external': True})
                continue
            if not parsed.path or any(c in url for c in ('${','<','>')): continue
            target = (ROOT / unquote(parsed.path).lstrip('/') if url.startswith('/') else p.parent / unquote(parsed.path)).resolve()
            refs.append({'file': rel, 'url': url, 'exists': target.exists(),
                         'bytes': target.stat().st_size if target.is_file() else 0})
        if p.suffix == '.html':
            pages.append({'path': rel, 'blockingScripts': len(re.findall(r'<script\b(?![^>]*\b(?:defer|async)\b)(?![^>]*type=["\']module)[^>]*\bsrc=', s)),
                          'images': len(re.findall(r'<img\b', s)), 'lazyImages': len(re.findall(r'<img\b[^>]*loading=["\']lazy', s)),
                          'videos': len(re.findall(r'<video\b', s)), 'iframes': len(re.findall(r'<iframe\b', s))})
    result = {'files': sorted(entries, key=lambda x: -x['bytes']), 'pages': pages, 'references': refs}
    (OUT / 'inventory.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'files':len(entries), 'pages':len(pages),'largest':result['files'][:12]},ensure_ascii=False), flush=True)

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
    def send_head(self):
        path = Path(self.translate_path(self.path))
        if path.is_file() and self.headers.get('Range'):
            size = path.stat().st_size
            match = re.fullmatch(r'bytes=(\d+)-(\d*)', self.headers['Range'])
            if match:
                start, end = int(match[1]), int(match[2]) if match[2] else size - 1
                end = min(end, size - 1)
                if start > end:
                    self.send_error(416); return None
                f = path.open('rb'); f.seek(start)
                self.range_remaining = end - start + 1
                self.send_response(206)
                self.send_header('Content-Type', self.guess_type(str(path)))
                self.send_header('Accept-Ranges', 'bytes')
                self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
                self.send_header('Content-Length', str(self.range_remaining))
                self.end_headers(); return f
        return super().send_head()
    def copyfile(self, source, outputfile):
        remaining = getattr(self, 'range_remaining', None)
        try:
            while remaining is None or remaining > 0:
                data = source.read(65536 if remaining is None else min(65536, remaining))
                if not data: break
                outputfile.write(data)
                if remaining is not None: remaining -= len(data)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError): pass

OBSERVER = """(() => {
 window.__perf = {lcp: null, cls: 0, longTasks: [], videoFirstFrame: null, headerReady: null};
 new PerformanceObserver(l => {for(const e of l.getEntries()) window.__perf.lcp={ms:e.startTime, element:e.element?.tagName,url:e.url};}).observe({type:'largest-contentful-paint',buffered:true});
 new PerformanceObserver(l => {for(const e of l.getEntries()) if(!e.hadRecentInput) window.__perf.cls+=e.value;}).observe({type:'layout-shift',buffered:true});
 new PerformanceObserver(l => {for(const e of l.getEntries()) window.__perf.longTasks.push({start:e.startTime,duration:e.duration});}).observe({type:'longtask',buffered:true});
 function watch() {
   if(!window.__perf.headerReady && document.querySelector('header nav a')) window.__perf.headerReady=performance.now();
   const v=document.querySelector('#video_play');
   if(v && !v.dataset.perfObserved) {v.dataset.perfObserved='1'; v.requestVideoFrameCallback(()=>window.__perf.videoFirstFrame=performance.now());}
 }
 new MutationObserver(watch).observe(document,{childList:true,subtree:true});
})();"""

def run(args):
    from playwright.sync_api import sync_playwright
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = args.base or f'http://127.0.0.1:{server.server_port}'
    routes = args.routes.split(',') if args.routes else ['/ko/index.html','/en/index.html','/ko/br_value.html','/ko/dt_explain.html','/ko/tova/index.html','/ko/gaia/index.html','/ko/egbim/primary.html','/recruit/br_recruit.html']
    if args.smoke and not args.routes:
        routes = ['/'+p.relative_to(ROOT).as_posix() for p in files() if p.suffix=='.html' and not any(x in p.parts for x in ('_include','ckeditor'))]
    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel='msedge', headless=True)
        for route in routes:
            for repeat in range(1 if args.smoke else args.runs):
                context = browser.new_context(viewport={'width':1365,'height':768}, locale='ko-KR',service_workers='block')
                page = context.new_page()
                page.add_init_script(OBSERVER)
                cdp = context.new_cdp_session(page)
                cdp.send('Network.enable')
                cdp.send('Network.setCacheDisabled', {'cacheDisabled':True})
                if not args.smoke:
                    cdp.send('Network.emulateNetworkConditions', {'offline':False,'latency':40,'downloadThroughput':1250000,'uploadThroughput':625000})
                    cdp.send('Emulation.setCPUThrottlingRate', {'rate':4})
                requests, failures, errors, responses = [], [], [], []
                received = [0]
                cdp.on('Network.dataReceived', lambda e: received.__setitem__(0,received[0]+e.get('encodedDataLength',0)))
                page.on('request', lambda r: requests.append({'url':r.url,'type':r.resource_type}))
                page.on('requestfailed', lambda r: failures.append({'url':r.url,'error':r.failure}))
                page.on('response', lambda r: responses.append({'url':r.url,'status':r.status}))
                page.on('pageerror', lambda e: errors.append(str(e)))
                started = time.monotonic(); timeout = None
                try: page.goto(base+route, wait_until='domcontentloaded', timeout=15000 if args.smoke else 25000)
                except Exception as e: timeout = str(e).splitlines()[0]
                wait = max(0, (2 if args.smoke else args.seconds) - (time.monotonic()-started))
                page.wait_for_timeout(wait*1000)
                try:
                    metrics = page.evaluate("""() => ({...window.__perf, actualUrl:location.href, navigation:performance.getEntriesByType('navigation')[0]?.toJSON(), paints:performance.getEntriesByType('paint').map(e=>e.toJSON()),resources:performance.getEntriesByType('resource').map(e=>e.toJSON()),video:[...document.querySelectorAll('video')].map(v=>({src:v.currentSrc,readyState:v.readyState,currentTime:v.currentTime,error:v.error?.code})),images:[...document.images].map(i=>({src:i.currentSrc,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight,top:i.getBoundingClientRect().top,width:i.getBoundingClientRect().width,height:i.getBoundingClientRect().height,complete:i.complete,loading:i.loading})),headerLinks:document.querySelectorAll('header nav a').length,footerLinks:document.querySelectorAll('footer a').length})""")
                except Exception as e: metrics = {'captureError':str(e)}
                result = {'route':route,'run':repeat+1,'browser':browser.version,'base':base,'windowSeconds':args.seconds if not args.smoke else 2,'metrics':metrics,'requests':requests,'responses':responses,'failures':failures,'errors':errors,'receivedBytes':received[0],'timeout':timeout}
                # Freeze the observation window before screenshot/teardown events.
                results.append(copy.deepcopy(result))
                (OUT / f'{args.label}.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
                print(json.dumps({'route':route,'run':repeat+1,'dcl':metrics.get('navigation',{}).get('domContentLoadedEventEnd'),'load':metrics.get('navigation',{}).get('loadEventEnd'),'lcp':metrics.get('lcp'),'frame':metrics.get('videoFirstFrame'),'requests':len(requests),'errors':len(errors)},ensure_ascii=False),flush=True)
                if not args.smoke and repeat==0:
                    try: page.screenshot(path=str(OUT / f'{args.label}-{route.strip("/").replace("/","_")}.png'),timeout=7000)
                    except Exception as e: print(f'Screenshot unavailable: {route}: {e}',flush=True)
                context.close()
        browser.close()
    server.shutdown()

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--inventory',action='store_true'); parser.add_argument('--smoke',action='store_true')
    parser.add_argument('--label',default='before'); parser.add_argument('--runs',type=int,default=3)
    parser.add_argument('--seconds',type=int,default=15); parser.add_argument('--routes'); parser.add_argument('--base')
    parser.add_argument('--output-dir')
    args=parser.parse_args()
    if args.output_dir:
        OUT = (ROOT / args.output_dir).resolve()
        OUT.mkdir(parents=True,exist_ok=True)
    if args.inventory: inventory()
    else: run(args)
