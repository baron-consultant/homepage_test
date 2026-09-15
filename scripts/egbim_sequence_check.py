"""Exercise the real scroll sequence on Laragon, including a failed frame."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.perf-tools'))
from playwright.sync_api import sync_playwright

results = []
with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='msedge')
    for lang, width in [('ko', 1365), ('en', 1365), ('ko', 390), ('en', 390)]:
        context = browser.new_context(viewport={'width': width, 'height': 844})
        page = context.new_page()
        errors, requests, inflight = [], [], set()
        peak = [0]
        def requested(req):
            if '/com_img/' in req.url and req.url.endswith('.png'):
                requests.append(req.url)
                inflight.add(req)
                peak[0] = max(peak[0], len(inflight))
        page.on('request', requested)
        page.on('requestfinished', lambda req: inflight.discard(req))
        page.on('requestfailed', lambda req: inflight.discard(req))
        page.on('pageerror', lambda err: errors.append(str(err)))
        cdp = context.new_cdp_session(page)
        cdp.send('Network.enable')
        cdp.send('Network.setBlockedURLs', {'urls': [f'http://baron.test/{lang}/egbim/img/com_img/' + ('eng/' if lang == 'en' else '') + 'comp_80.png']})
        page.goto(f'http://baron.test/{lang}/egbim/interface.html', wait_until='load')
        page.wait_for_timeout(1500)
        assert len(requests) == 0, requests
        assert page.locator('#myimg').evaluate('(i)=>i.complete && i.naturalWidth>0')
        assert page.locator('header a').count() > 0
        page.add_style_tag(content='html,body { scroll-behavior: auto !important; }')
        if lang == 'en' and width <= 1200:
            assert page.locator('#dualm').count() == 0
            page.evaluate('()=>window.scrollTo(0,document.body.scrollHeight)')
            page.wait_for_timeout(1000)
            assert not requests and not errors
            assert page.locator('#myimg').evaluate('(i)=>i.complete&&i.naturalWidth>0')
            row = {'lang':lang,'width':width,'initialPngRequests':0,'staticMobilePreserved':True,'errors':errors,'passed':True}
            results.append(row)
            print(json.dumps(row),flush=True)
            context.close()
            continue
        bounds = page.evaluate('''()=>{ScrollTrigger.refresh();let t=ScrollTrigger.getAll().find(t=>t.vars.pin && t.trigger?.id==='dualm');return {start:t.start,end:t.end};}''')
        for fraction in [0.1, 0.5, 1, 0.3, 0]:
            y = bounds['start'] + (bounds['end'] - bounds['start']) * fraction
            page.evaluate('(y)=>window.scrollTo(0,y)', y)
            page.wait_for_timeout(1000)
            frame = round(103 * fraction) + 1
            suffix = 'comp_1.perf.webp' if frame == 1 else f'comp_{frame}.png'
            page.wait_for_function('(suffix)=>{let i=document.querySelector("#myimg");return i.src.endsWith(suffix)&&i.complete&&i.naturalWidth>0}', arg=suffix, timeout=15000)
        # A failed target must keep the last valid image and allow later recovery.
        page.evaluate('(y)=>window.scrollTo(0,y)', bounds['start'] + 79 / 103 * 2500)
        page.wait_for_timeout(1200)
        assert page.locator('#myimg').evaluate('(i)=>i.complete&&i.naturalWidth>0&&!i.src.endsWith("comp_80.png")')
        page.evaluate('(y)=>window.scrollTo(0,y)', bounds['start'] + 90 / 103 * 2500)
        page.wait_for_function('()=>{let i=document.querySelector("#myimg");return i.src.endsWith("comp_91.png")&&i.complete&&i.naturalWidth>0}')
        assert peak[0] <= 4, peak
        assert not errors, errors
        row = {'lang': lang, 'width': width, 'initialPngRequests': 0, 'peakConcurrentFrames': peak[0], 'scrollFrameRequests': len(requests), 'errors': errors, 'passed': True}
        results.append(row)
        print(json.dumps(row), flush=True)
        context.close()
    browser.close()
out = ROOT / 'artifacts/performance/egbim-interface-after'
out.mkdir(parents=True, exist_ok=True)
(out / 'sequence-check.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
