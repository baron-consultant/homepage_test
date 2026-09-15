"""Restore missing referenced images from the public site; never overwrite files."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import threading
from urllib.parse import quote, unquote, urljoin, urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artifacts/performance'
ORIGIN = 'https://baroncs.co.kr'
IMAGE_EXTENSIONS = {'.svg', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.ico', '.avif'}
EXCLUDED = {'.git', '.perf-tools', 'node_modules', 'artifacts', 'ckeditor', 'font', 'img', '_00.back'}

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

def find_missing():
    paths = set()
    for file in ROOT.rglob('*'):
        if file.suffix.lower() not in {'.html', '.css'} or not file.is_file():
            continue
        relative = file.relative_to(ROOT)
        if EXCLUDED.intersection(relative.parts) or '_bak' in file.name or ' copy' in file.name:
            continue
        source = file.read_text(encoding='utf-8', errors='replace')
        source = re.sub(r'<!--.*?-->|/\*.*?\*/', '', source, flags=re.S)
        references = re.findall(r'''(?:src|poster)\s*=\s*["']([^"']+)["']|url\(\s*["']?([^\s)'";]+)''', source)
        for pair in references:
            reference = next(part for part in pair if part)
            if any(token in reference for token in ('${', '<', '>')):
                continue
            url = urlsplit(urljoin('/' + relative.as_posix(), reference))
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            target = (ROOT / path.lstrip('/')).resolve()
            if '/img/' in path and target.suffix.lower() in IMAGE_EXTENSIONS and target.is_relative_to(ROOT) and not target.exists():
                paths.add(path)
    # Includes injected via JS can use paths resolved differently from the HTML file.
    previous = OUT / 'local-image-audit.json'
    if previous.exists():
        for page in json.loads(previous.read_text(encoding='utf-8')):
            for error in page['httpErrors']:
                url = urlsplit(error['url'])
                if url.hostname not in {'baron.test', 'localhost', '127.0.0.1'}:
                    continue
                path = unquote(url.path)
                if path.startswith('/baron/'):
                    path = path[len('/baron'):]
                target = (ROOT / path.lstrip('/')).resolve()
                if '/img/' in path and target.suffix.lower() in IMAGE_EXTENSIONS and target.is_relative_to(ROOT) and not target.exists():
                    paths.add(path)
    return sorted(paths)

def restore(paths):
    lock = threading.Lock()
    total_bytes = 0
    def fetch(path):
        nonlocal total_bytes
        result = {'path': path, 'source': ORIGIN + quote(path, safe='/')}
        target = (ROOT / path.lstrip('/')).resolve()
        try:
            assert target.is_relative_to(ROOT) and '/img/' in path
            if target.exists():
                return {**result, 'status': 'already-exists'}
            request = Request(result['source'], headers={'User-Agent': 'Baron-local-image-restore/1.0'})
            with build_opener(NoRedirect()).open(request, timeout=15) as response:
                content_type = response.headers.get('Content-Type', '').split(';')[0].lower()
                if response.status != 200 or not content_type.startswith('image/'):
                    return {**result, 'status': 'not-public-image', 'contentType': content_type}
                body = response.read(20_000_001)
                if len(body) > 20_000_000:
                    return {**result, 'status': 'file-size-limit'}
                with lock:
                    if total_bytes + len(body) > 200_000_000:
                        return {**result, 'status': 'total-size-limit'}
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with target.open('xb') as output:
                        output.write(body)
                    total_bytes += len(body)
                return {**result, 'status': 'restored', 'bytes': len(body), 'contentType': content_type}
        except Exception as error:
            return {**result, 'status': 'unavailable', 'error': str(error)}
    results = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(fetch, paths):
            results.append(result)
            if len(results) % 25 == 0:
                print(f'Checked {len(results)}/{len(paths)}; restored {sum(r["status"] == "restored" for r in results)}', flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'restored-local-images.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'checked': len(results), 'restored': sum(r['status'] == 'restored' for r in results), 'bytes': total_bytes,
                     'unavailable': [r for r in results if r['status'] not in {'restored', 'already-exists'}]}, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--download', action='store_true')
    args = parser.parse_args()
    missing = find_missing()
    print(f'Missing referenced images: {len(missing)}', flush=True)
    if args.download:
        restore(missing)
