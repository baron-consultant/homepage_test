"""Inventory image URL syntax without changing application files."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/performance/latest-20260915'
SKIP={'.git','.perf-tools','node_modules','artifacts','docs','scripts','vendor','__pycache__'}
IMAGE=re.compile(r'\.(?:png|jpe?g|gif|svg|webp|avif|ico|bmp)(?:[?#].*)?$',re.I)
rows=[]
def add(file,line,url,kind):
    url=url.strip()
    if not url: return
    if url.startswith('data:'): category='embedded'
    elif '${' in url or '{{' in url or '<%' in url: category='dynamic'
    elif re.match(r'^(?:https?:)?//',url): category='external'
    elif url.startswith('/'): category='root-relative'
    elif url.startswith('#'): category='fragment'
    elif re.match(r'^[a-z][a-z0-9+.-]*:',url,re.I): category='other-scheme'
    else: category='relative'
    rows.append({'file':file,'line':line,'url':url if category!='embedded' else url.split(',',1)[0]+',…','kind':kind,'category':category})

class Parser(HTMLParser):
    def __init__(self,file): super().__init__(convert_charrefs=True); self.file=file
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);line=self.getpos()[0]
        candidates=[]
        if tag in ('img','image'): candidates+=['src','href','xlink:href','data-src','data-original','data-lazy-src']
        if tag=='video': candidates+=['poster']
        if tag=='input' and a.get('type','').lower()=='image': candidates+=['src']
        if tag=='object' and IMAGE.search(a.get('data','')): candidates+=['data']
        if tag=='link' and ('icon' in a.get('rel','') or a.get('as')=='image'): candidates+=['href']
        if tag=='meta' and 'image' in (a.get('property','')+a.get('name','')).lower(): candidates+=['content']
        for name in candidates:
            if a.get(name): add(self.file,line,a[name],tag+'.'+name)
        if tag in ('img','source','link'):
            for name in ('srcset','data-srcset','imagesrcset'):
                if a.get(name):
                    if a[name].startswith('data:'): add(self.file,line,a[name],tag+'.'+name)
                    else:
                        for item in a[name].split(','):
                            if item.strip(): add(self.file,line,item.strip().split()[0],tag+'.'+name)

files=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or any(x in SKIP for x in p.relative_to(ROOT).parts) or p.suffix.lower() not in ('.html','.css','.js','.svg'): continue
    file=p.relative_to(ROOT).as_posix(); files.append(file)
    text=p.read_text(encoding='utf-8',errors='replace')
    if p.suffix in ('.html','.svg'):
        if p.suffix=='.html' or '<image' in text:
            parser=Parser(file)
            try: parser.feed(text)
            except Exception: pass
    if p.suffix in ('.html','.css','.js'):
        # Keep line offsets while removing multiline comments.
        clean=re.sub(r'<!--.*?-->|/\*.*?\*/',lambda m:'\n'*m[0].count('\n'),text,flags=re.S)
        for m in re.finditer(r'''url\(\s*(["']?)([^\s)'";]+)\1\s*\)''',clean):
            url=m[2]
            if IMAGE.search(url) or url.startswith(('data:image/','#')): add(file,clean.count('\n',0,m.start())+1,url,'css-url')
        if p.suffix=='.js' or p.suffix=='.html':
            for m in re.finditer(r'''(["'`])([^"'`\r\n]+)\1''',clean):
                url=m[2]
                if IMAGE.search(url) and not re.search(r'\s',url): add(file,clean.count('\n',0,m.start())+1,url,'string-candidate')

unique={}
for r in rows:
    key=(r['file'],r['line'],r['url'])
    if key not in unique or unique[key]['kind']=='string-candidate': unique[key]=r
rows=list(unique.values())
manifest=json.loads((OUT/'asset-optimizations.json').read_text(encoding='utf-8'))
new_names={Path(a['output']).name for a in manifest['assets']}
new_names.update(p.name for p in (ROOT/'assets/media').glob('*') if p.suffix in ('.jpg','.webp'))
new=[r for r in rows if r['url'].split('?',1)[0].split('#',1)[0].rsplit('/',1)[-1] in new_names]
counts=Counter(r['category'] for r in rows);new_counts=Counter(r['category'] for r in new)
result={'filesScanned':len(files),'counts':dict(counts),'newAssetReferenceCounts':dict(new_counts),'references':rows,'newAssetReferences':new}
(OUT/'image-reference-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# 이미지 참조 경로 검사','',
'이미지 참조를 수정하지 않고 현재 HTML·CSS·JavaScript·SVG를 검사했다. 라이브러리·데모·백업 파일도 포함한다. scripts/docs/artifacts 및 도구 설치 폴더는 제외했다.','',
f'검사 파일 {len(files):,}개. 정적 참조와 JS 문자열 후보를 파일·행·URL 기준으로 중복 제거했다. 주석과 일부 동적 문자열은 정적 분석 한계가 있어 실제 요청 여부와 구분해야 한다.','',
'| 분류 | 전체 참조 후보 | 새로 생성한 이미지 참조 |','|---|---:|---:|']
for k in ('relative','root-relative','external','embedded','fragment','dynamic','other-scheme'):
    md.append(f'| {k} | {counts[k]} | {new_counts[k]} |')
md+=['','- `relative`: `img/a.webp`, `../assets/img/a.svg`처럼 현재 기준 URL에서 해석되는 경로.',
'- `root-relative`: `/assets/img/a.svg`처럼 현재 도메인의 루트 기준 경로. 도메인을 고정한 절대 URL은 아니지만 현재 폴더 기준 상대경로와 다르다.',
'- `external`: https:// 또는 //로 시작하는 도메인 지정 URL.',
'- CSS 파일의 url()은 CSS 파일 위치, HTML src는 문서 위치를 기준으로 해석된다. JS 문자열은 실제 대입 대상·실행 문서에 따라 기준이 달라진다.',
'- SVG 내부 data:image는 파일 경로가 아닌 내장 데이터다. 동적 연결·API가 반환하는 URL은 이 검사만으로 모두 확정할 수 없다.',
'','## 현재 폴더 기준 상대경로가 아닌 참조','',
'아래는 root-relative/external/dynamic/other-scheme 후보의 전체 목록이다. 라이브러리 또는 사용하지 않는 파일의 문자열도 포함하며, 실제 화면 요청임을 뜻하지 않는다.','',
'| 파일:행 | 분류 | 참조 |','|---|---|---|']
for r in rows:
    if r['category'] in ('root-relative','external','dynamic','other-scheme'):
        url=r['url'].replace('|','%7C').replace('`','')
        md.append(f"| `{r['file']}:{r['line']}` | {r['category']} | `{url}` |")
(ROOT/'docs/image-reference-audit.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(json.dumps({'files':len(files),'counts':dict(counts),'new':dict(new_counts),'newNonRelative':[r for r in new if r['category']!='relative'][:15],'rootExamples':[r for r in rows if r['category']=='root-relative'][:5],'externalExamples':[r for r in rows if r['category']=='external'][:5]},ensure_ascii=False))
