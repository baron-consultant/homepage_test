"""Check functionality affected by media, defer and include-loader changes."""
import functools
import json
import threading
from performance_audit import Handler, ROOT, OUT, ThreadingHTTPServer
from playwright.sync_api import sync_playwright, expect

server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}'
results=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='msedge',headless=True)
    for width,height in [(1365,768),(390,844)]:
        for route in ['/ko/index.html','/en/index.html','/recruit/br_recruit.html']:
            context=browser.new_context(viewport={'width':width,'height':height},locale='ko-KR')
            page=context.new_page(); errors=[]; requests=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('request',lambda r:requests.append(r.url))
            page.goto(base+route,wait_until='load')
            page.wait_for_function("document.querySelectorAll('header nav a').length > 0")
            page.wait_for_function("document.querySelectorAll('.popup_wrap.sitemap nav a').length > 0")
            page.locator('header .btn_menu').click()
            expect(page.locator('.popup_wrap.sitemap')).to_be_visible()
            expect(page.locator('.popup_wrap.sitemap nav a').first).to_be_attached()
            page.locator('.popup_wrap.sitemap .btn_close').click()
            expect(page.locator('.popup_wrap.sitemap')).to_be_hidden()
            if '/index.html' in route:
                page.wait_for_function("document.querySelector('video').currentTime > 1")
                expect(page.locator('video')).to_be_visible()
            else:
                page.wait_for_function("[...document.querySelectorAll('.intro .img_box img')].every(i => i.complete && i.naturalWidth > 0)")
                assert sum('/assets/js/common.js' in u for u in requests)==1, requests
            assert not errors, errors
            page.screenshot(path=str(OUT/f'functional-{width}-{route.strip("/").replace("/","_")}.png'))
            result={'route':route,'viewport':[width,height],'menuOpenClose':'pass','media':'pass','errors':errors,'includeRequests':[u.split(base)[-1] for u in requests if '/_include/' in u]}
            results.append(result); print(json.dumps(result),flush=True)
            context.close()
    browser.close()
server.shutdown()
(OUT/'functional.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
