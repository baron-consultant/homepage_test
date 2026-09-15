"""Targeted delivery optimizations for package pages, without changing page logic.

Original assets are retained. Run after collecting latest-20260915/before.json.
New assets remain under ignored img directories and require separate R2 upload.
"""
import base64
from collections import defaultdict
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artifacts/performance/latest-20260915'
sys.path.insert(0, str(ROOT / '.perf-tools'))
from PIL import Image, ImageOps

PRODUCTS = ('egbim', 'tova', 'gaia', 'kngil')
REFERENCE = re.compile(r'''(?P<attrprefix>\b(?:src|poster|data)\s*=\s*["'])(?P<attr>[^"']+)(?P<attrsuffix>["'])|(?P<cssprefix>url\(\s*["']?)(?P<css>[^)'"\s]+)(?P<csssuffix>["']?\s*\))''')

def source_files():
    for lang in ('ko', 'en'):
        for product in PRODUCTS:
            base = ROOT / lang / product
            for p in list(base.glob('*.html')) + list((base / 'css').glob('*.css')):
                if '_bak' not in p.name and 'copy' not in p.name.lower() and not re.search(r'_(?:20)?\d{6}', p.name):
                    yield p

def resolve(file, reference):
    if any(c in reference for c in ('${', '<', '>')):
        return None
    parsed = urlsplit(urljoin('/' + file.relative_to(ROOT).as_posix(), reference))
    if parsed.scheme or parsed.netloc:
        return None
    result = (ROOT / unquote(parsed.path).lstrip('/')).resolve()
    return result if result.is_relative_to(ROOT) else None

def matches(file, source):
    comments = [m.span() for m in re.finditer(r'<!--.*?-->|/\*.*?\*/', source, re.S)]
    for m in REFERENCE.finditer(source):
        if any(start <= m.start() < end for start, end in comments):
            continue
        ref = m['attr'] if m['attr'] is not None else m['css']
        yield m, ref, resolve(file, ref)

def encode_lossless(image):
    original = image.convert('RGBA')
    output = BytesIO()
    original.save(output, format='WEBP', lossless=True, method=4, exact=True,
                  **({'icc_profile':image.info['icc_profile']} if image.info.get('icc_profile') else {}))
    encoded = output.getvalue()
    # Verify the decoded pixels including transparency, not only dimensions.
    decoded = Image.open(BytesIO(encoded)).convert('RGBA')
    assert decoded.size == original.size and decoded.tobytes() == original.tobytes()
    return encoded

def main():
    baseline = json.loads((OUT / 'before.json').read_text(encoding='utf-8'))
    assert len(baseline) == 24, 'Collect all eight pages x three runs before optimizing.'
    files = list(source_files())
    sources = {p:p.read_text(encoding='utf-8') for p in files}
    references = defaultdict(set)
    for file, source in sources.items():
        for match, ref, target in matches(file, source):
            if target and target.is_file() and '/img/' in target.as_posix() and target.suffix.lower() in {'.png','.jpg','.jpeg','.svg'}:
                references[target].add(file)
    heroes = {}
    hidden = defaultdict(set)
    for row in baseline:
        if row['run'] != 1:
            continue
        lcp = row['metrics'].get('lcp') or {}
        path = unquote(urlsplit(lcp.get('url','')).path)
        if path and lcp.get('element') in {'SECTION','DIV'}:
            heroes[row['route']] = (ROOT / path.lstrip('/')).resolve()
        for im in row['metrics'].get('images', []):
            if im['src'] and im['width'] == 0 and im['height'] == 0:
                hidden[row['route']].add(unquote(urlsplit(im['src']).path))
    # English duplicates get the same delivery hints without moving their assets.
    for route, path in list(heroes.items()):
        translated_route = route.replace('/ko/', '/en/', 1)
        translated_path = ROOT / path.relative_to(ROOT).as_posix().replace('ko/', 'en/', 1)
        if translated_path.exists() and (ROOT / translated_route.lstrip('/')).exists():
            heroes[translated_route] = translated_path
    for route, paths in list(hidden.items()):
        hidden[route.replace('/ko/', '/en/', 1)] = {p.replace('/ko/','/en/',1) for p in paths}
    hero_paths = set(heroes.values())
    # Only photographic first-screen backgrounds use lossy encoding/resizing.
    # All other PNG/JPEGs and embedded SVG images preserve every RGBA pixel.
    photo_names = {'value_introbg.png','value_intro_bg.jpg','value_intro_bg_top.png',
                   'primary_intro_bg.jpg','primary_intro_bg.png','public_intro_bg.jpg',
                   'bg_value_visual.jpg','bg_primary_visual.jpg'}
    mapping, conversions, cache = {}, [], {}
    for index, path in enumerate(sorted(references)):
        # Retain these originals: controlled browser rendering did not match.
        if path.relative_to(ROOT).as_posix() in {'ko/egbim/img/interface_img_02.svg','ko/egbim/img/interface_img_03.svg'}:
            continue
        if path.stat().st_size < 150_000:
            continue
        original = path.read_bytes()
        photo = path in hero_paths and path.name in photo_names
        mode = 'photo-webp-q90-max1920' if photo else 'lossless-webp'
        if path.suffix.lower() == '.svg':
            mode = 'svg-lossless-embedded-webp'
        key = (hashlib.sha256(original).hexdigest(), mode)
        if key in cache:
            encoded, dimensions = cache[key]
        elif path.suffix.lower() == '.svg':
            svg = original.decode('utf-8')
            count = [0]
            def convert_embedded(match):
                raw = base64.b64decode(match[1])
                with Image.open(BytesIO(raw)) as image:
                    if getattr(image,'is_animated',False):
                        return match[0]
                    packed = encode_lossless(image)
                if len(packed) >= len(raw) * .9:
                    return match[0]
                count[0] += 1
                return 'data:image/webp;base64,' + base64.b64encode(packed).decode('ascii')
            encoded = re.sub(r'data:image/png;base64,([A-Za-z0-9+/=\r\n]+)',convert_embedded,svg).encode('utf-8')
            dimensions = {'embeddedImagesConverted':count[0]}
            cache[key] = (encoded, dimensions)
        else:
            with Image.open(path) as image:
                if getattr(image,'is_animated',False):
                    continue
                before_size = image.size
                if photo:
                    render = ImageOps.exif_transpose(image).convert('RGBA')
                    render.thumbnail((1920,1920),Image.Resampling.LANCZOS)
                    output = BytesIO()
                    render.save(output,format='WEBP',quality=90,method=4,
                                **({'icc_profile':image.info['icc_profile']} if image.info.get('icc_profile') else {}))
                    encoded = output.getvalue()
                    dimensions = {'before':before_size,'after':render.size}
                else:
                    encoded = encode_lossless(image)
                    dimensions = {'before':before_size,'after':before_size,'pixelIdentical':True}
            cache[key] = (encoded, dimensions)
        if len(encoded) >= len(original) * .9:
            continue
        destination = path.with_name(path.stem + ('.perf.svg' if path.suffix.lower()=='.svg' else '.perf.webp'))
        destination.write_bytes(encoded)
        mapping[path] = destination
        conversions.append({'source':path.relative_to(ROOT).as_posix(),'output':destination.relative_to(ROOT).as_posix(),
                            'beforeBytes':len(original),'afterBytes':len(encoded),'mode':mode,**dimensions})
        if len(conversions) % 10 == 0:
            print(f'Generated {len(conversions)} optimized assets',flush=True)
    changes = []
    for file, source in sources.items():
        modified = source
        edits = []
        for m, ref, target in matches(file,source):
            if target not in mapping:
                continue
            rewritten = os.path.relpath(mapping[target], file.parent).replace('\\','/')
            if ref.startswith('/'):
                rewritten = '/' + mapping[target].relative_to(ROOT).as_posix()
            elif ref.startswith('./') and not rewritten.startswith('.'):
                rewritten = './' + rewritten
            query = urlsplit(ref).query
            fragment = urlsplit(ref).fragment
            rewritten += ('?' + query if query else '') + ('#' + fragment if fragment else '')
            field = 'attr' if m['attr'] is not None else 'css'
            edits.append((m.start(field),m.end(field),rewritten))
        for start,end,value in reversed(edits):
            modified = modified[:start] + value + modified[end:]
        route = '/' + file.relative_to(ROOT).as_posix()
        lazy_count = 0
        if file.suffix == '.html':
            if route in heroes:
                hero = mapping.get(heroes[route], heroes[route])
                href = os.path.relpath(hero,file.parent).replace('\\','/')
                hint = f'    <link rel="preload" as="image" href="{href}" fetchpriority="high" />\n'
                if hint.strip() not in modified:
                    modified = modified.replace('</head>',hint+'</head>',1)
            def lazy_image(m):
                nonlocal lazy_count
                tag=m[0]
                src=re.search(r'''\bsrc=["']([^"']+)["']''',tag)
                if not src or 'loading=' in tag:
                    return tag
                target=resolve(file,src[1])
                if not target:
                    return tag
                path='/' + target.relative_to(ROOT).as_posix()
                original_paths = hidden.get(route,set())
                optimized_paths = {'/'+mapping[ROOT/p.lstrip('/')].relative_to(ROOT).as_posix() for p in original_paths if ROOT/p.lstrip('/') in mapping}
                if path not in original_paths | optimized_paths:
                    return tag
                lazy_count+=1
                return tag.replace('<img','<img loading="lazy" decoding="async"',1)
            modified=re.sub(r'<img\b[^>]*>',lazy_image,modified,flags=re.S)
            if '/kngil/' in route:
                modified=modified.replace('class="guide-video" playsinline preload="metadata"','class="guide-video" playsinline preload="none"')
        if modified != source:
            file.write_text(modified,encoding='utf-8',newline='\r\n')
            changes.append({'file':file.relative_to(ROOT).as_posix(),'assetReferences':len(edits),'hiddenImagesLazy':lazy_count,'heroPreload':route in heroes})
    manifest={'assets':conversions,'files':changes,'originalAssetsRetained':True,'gitPolicy':'img directories remain ignored; separate asset upload required'}
    (OUT/'asset-optimizations.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'assets':len(conversions),'files':len(changes),'beforeBytes':sum(x['beforeBytes'] for x in conversions),'afterBytes':sum(x['afterBytes'] for x in conversions)},ensure_ascii=False),flush=True)

if __name__ == '__main__':
    main()
