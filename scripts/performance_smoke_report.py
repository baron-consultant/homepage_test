"""Render every Playwright smoke-tested route and observed failure."""
import json
from pathlib import Path
from urllib.parse import urlsplit

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'artifacts/performance/smoke-after.json').read_text(encoding='utf-8'))
def short(url):
    p=urlsplit(url)
    return p.path if p.hostname=='127.0.0.1' else f'{p.hostname}{p.path}'
lines=['# 전체 HTML 페이지 브라우저 점검', '',
       f'개선 후 {len(data)}개 경로를 실제 Playwright/Edge로 각각 탐색했습니다. include HTML 조각과 CKEditor 샘플은 제외하며 백업 HTML과 폰트 데모는 포함합니다.', '',
       f"JS 오류가 관측된 경로 {sum(bool(r['errors']) for r in data)}개, HTTP 400 이상 응답이 관측된 경로 {sum(any(e['status']>=400 for e in r['responses']) for r in data)}개, 탐색 시간초과 {sum(bool(r['timeout']) for r in data)}개입니다. 항목 간 경로는 중복될 수 있습니다.", '',
       '성능 비교 실험과 별도입니다. 네트워크/CPU 감속 없이 새 컨텍스트·캐시 비활성화로 실행했습니다. 탐색 시작부터 최소 2초 관측하며 DOMContentLoaded를 최대 15초 기다립니다. load가 관측되지 않은 것은 0ms 로딩이 아닙니다.', '',
       '초기 탐색 검사만 수행합니다. 폼 제출·다운로드·모든 버튼/스크롤은 시험하지 않았습니다. 아래 오류는 이 로컬 복사본에서 관측한 결과이며 운영 환경과 다를 수 있습니다. 기존 오류와 이번 변경의 회귀 여부는 주요 페이지 전후 비교 및 별도 메뉴 테스트를 함께 확인해야 합니다.', '',
       '| 페이지 | DCL ms | load ms | JS 오류 | HTTP ≥400 | 요청 실패 | 탐색 시간초과 |',
       '|---|---:|---:|---:|---:|---:|---|']
for r in data:
    nav=r['metrics'].get('navigation',{})
    fmt=lambda v: f'{v:.1f}' if v else '미관측'
    lines.append(f"| `{r['route']}` | {fmt(nav.get('domContentLoadedEventEnd'))} | {fmt(nav.get('loadEventEnd'))} | {len(r['errors'])} | {sum(e['status']>=400 for e in r['responses'])} | {len(r['failures'])} | {r['timeout'] or '—'} |")
lines += ['', '## 관측 오류 상세', '',
          'ERR_ABORTED는 영상 소스 교체·페이지 이동·분석 beacon 중단·테스트 컨텍스트 종료 등에서도 발생하므로 모두 사용자에게 보이는 장애로 단정하지 않습니다.', '']
for r in data:
    issues=list(dict.fromkeys(r['errors']))
    issues += list(dict.fromkeys(f"HTTP {e['status']}: {short(e['url'])}" for e in r['responses'] if e['status']>=400))
    issues += list(dict.fromkeys(f"{e['error']}: {short(e['url'])}" for e in r['failures']))
    if r['metrics'].get('captureError'): issues.append(r['metrics']['captureError'])
    if not issues: continue
    lines += [f"### {r['route']}", '']
    lines += ['- '+i.replace('\n',' ').replace('|','\\|') for i in issues]
    lines += ['']
recheck=root/'artifacts/performance/smoke-recheck.json'
if recheck.exists():
    lines += ['## 로컬 연결 실패 경로 재검증', '',
              '최초 순회에서 일부 로컬 리소스에 ERR_CONNECTION_REFUSED가 관측되어 테스트 서버의 연결 대기열을 128로 늘린 뒤 해당 경로만 재검증했습니다. 최초 기록은 위에 보존했으며 아래는 별도 실행 결과입니다. 전후 성능 48회 측정에서는 이 변경 이전의 동일 서버 설정을 사용했습니다.', '',
              '| 경로 | JS 오류 | HTTP ≥400 | 요청 실패 |', '|---|---:|---:|---:|']
    for r in json.loads(recheck.read_text(encoding='utf-8')):
        lines.append(f"| `{r['route']}` | {len(r['errors'])} | {sum(e['status']>=400 for e in r['responses'])} | {len(r['failures'])} |")
    lines += ['']
lines += ['## 메뉴·미디어 기능 확인', '']
functional=root/'artifacts/performance/functional.json'
if functional.exists():
    checks=json.loads(functional.read_text(encoding='utf-8'))
    lines += ['| 경로 | 화면 | 메뉴 열기/닫기 | 영상/사진 | JS 오류 |','|---|---|---|---|---:|']
    for c in checks:
        lines.append(f"| `{c['route']}` | {c['viewport'][0]}×{c['viewport'][1]} | {c['menuOpenClose']} | {c['media']} | {len(c['errors'])} |")
    lines += ['', '채용 페이지는 common.js 요청이 한 번인지도 검증했습니다. 국문·영문 메인은 실제 재생 시간이 1초 이상 증가하는지 확인했습니다.', '']
(root/'docs/performance-page-smoke.md').write_text('\n'.join(lines),encoding='utf-8')
print('Wrote docs/performance-page-smoke.md')
