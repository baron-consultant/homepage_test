"""Render the complete baseline file inventory as Markdown."""
from pathlib import Path
import collections
import json

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'artifacts/performance/inventory.json').read_text(encoding='utf-8'))
pages = {p['path']: p for p in data['pages']}
refs = collections.defaultdict(list)
for ref in data['references']: refs[ref['file']].append(ref)
lines = ['# 전체 파일 로딩 감사 목록', '',
         '개선 전 저장소 스캔. `.git`, 설치 도구, node_modules, 측정 산출물은 제외했습니다.', '',
         'HTML/CSS/JS는 주석을 제거한 뒤 정적 URL 참조를 검사했습니다. 바이너리는 크기와 참조 관계를 검사했습니다. 모든 소스의 업무 로직을 수동 검증한 목록은 아닙니다.', '',
         '외부 참조에는 링크도 포함됩니다. 존재하지 않는 참조도 동적 경로·앵커·템플릿 해석의 한계가 있으므로 실제 네트워크 오류로 단정하지 않습니다. 실행 시 오류는 별도 Playwright 보고서를 확인하세요.', '',
         f"총 {len(data['files']):,}개 파일, {len(pages)}개 HTML, {sum(f['bytes'] for f in data['files'])/1e9:.3f} GB.", '',
         '| 파일 | 크기 (bytes) | 검사 내용 |', '|---|---:|---|']
for f in sorted(data['files'],key=lambda x:x['path']):
    path = f['path']; p = pages.get(path); r = refs[path]
    notes = []
    if p:
        notes.append(f"HTML: 동기 외부 스크립트 {p['blockingScripts']}, 이미지 {p['images']} (lazy {p['lazyImages']}), video {p['videos']}, iframe {p['iframes']}")
    elif path.endswith(('.css','.js')): notes.append('텍스트 리소스 참조 검사')
    else: notes.append('파일 크기/참조 검사')
    if r:
        notes.append(f"외부 URL {sum(bool(x.get('external')) for x in r)}, 로컬 참조 확인 필요 {sum(x.get('exists') is False for x in r)}")
    if f['bytes'] > 10_000_000: notes.append('10 MB 초과: 실제 요청될 때 전송 부담')
    if 'ckeditor' in path or '_bak' in path: notes.append('샘플/백업 포함, 초기 로드 여부 별도 확인')
    lines.append(f"| `{path.replace('|','%7C')}` | {f['bytes']:,} | {'; '.join(notes)} |")
(root / 'docs').mkdir(exist_ok=True)
(root / 'docs/performance-file-inventory.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Wrote docs/performance-file-inventory.md')
