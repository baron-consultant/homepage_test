"""Generate the current baseline comparison; historical results are not mixed in."""
import collections
import json
from pathlib import Path
import statistics
from urllib.parse import urlsplit, unquote

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/performance/latest-20260915'
DOC=ROOT/'docs'
def read(name): return json.loads((OUT/name).read_text(encoding='utf-8'))
def med(rows, getter): return statistics.median(getter(r) for r in rows)
def pct(before,after): return f'{(1-after/before)*100:.1f}%' if before else '—'
def sec(n): return f'{n/1000:.2f}' if n else '>15 (미완료)'
def clean(s):
    value=str(s).replace('|','/').replace('\n',' ')
    return value if len(value)<=240 else value[:237]+'…'
def short_url(url):
    p=urlsplit(url)
    return (p.netloc if p.netloc!='baron.test' else '')+unquote(p.path)

before,after,manifest=read('before.json'),read('after.json'),read('asset-optimizations.json')
assert len(before)==len(after)==24
routes=list(dict.fromkeys(r['route'] for r in before))
summary=[]
for route in routes:
    a=[r for r in before if r['route']==route]; b=[r for r in after if r['route']==route]
    row={'route':route}
    for key,fn in [('lcp',lambda r:(r['metrics'].get('lcp') or {}).get('ms',0)),('load',lambda r:r['metrics']['navigation']['loadEventEnd']),('dcl',lambda r:r['metrics']['navigation']['domContentLoadedEventEnd']),('bytes',lambda r:r['receivedBytes']),('cls',lambda r:r['metrics'].get('cls',0))]:
        row[key+'Before']=med(a,fn); row[key+'After']=med(b,fn)
    summary.append(row)
(OUT/'comparison.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
smoke=read('smoke-after.json'); delivery=read('delivery-check.json'); syntax=read('js-syntax.json'); inventory=read('inventory.json')
svg_render=read('svg-render-check.json')
final_interface=read('smoke-interface-final.json')
for replacement in final_interface:
    smoke=[replacement if r['route']==replacement['route'] else r for r in smoke]
active_assets={a['output'] for a in manifest['assets']}
active_svg=[x for x in svg_render['svgComparisons'] if x['path'] in active_assets]
bad_assets=[x for x in delivery['assets'] if x['status']!=200 or x['bytes']!=x['expectedBytes']]
svg_bad=[x for x in active_svg if not x['identicalBrowserPixels']]
total_before=sum(x['beforeBytes'] for x in manifest['assets']); total_after=sum(x['afterBytes'] for x in manifest['assets'])
lines=['# 최신 소스 로딩 속도 개선 및 재검증 — 2026-09-15','',
'## 결론','',
'패키지 S/W의 페이지 구조·메뉴·애니메이션 로직을 리팩토링하지 않고, 이미지 전송량과 요청 우선순위를 조정했다. 아래 수치는 최신 소스에서 새로 수집한 동일 조건 3회 중앙값이다. 운영 서버 실측값은 아니다.','',
'| 페이지 | LCP 개선 전 → 후 (초) | LCP 단축 | 전체 load 개선 전 → 후 (초) | load 단축 |',
'|---|---:|---:|---:|---:|']
for r in summary:
    load_pct=pct(r['loadBefore'],r['loadAfter']) if r['loadBefore'] and r['loadAfter'] else '관측 한계로 정확한 비율 제외'
    lines.append(f"| `{r['route']}` | {sec(r['lcpBefore'])} → {sec(r['lcpAfter'])} | {pct(r['lcpBefore'],r['lcpAfter'])} | {sec(r['loadBefore'])} → {sec(r['loadAfter'])} | {load_pct} |")
lines += ['',
'- LCP: 첫 화면에서 가장 큰 콘텐츠가 표시된 시점. 사용자가 화면이 나타났다고 느끼는 속도에 가깝다.',
'- load: 일반 이미지 등 페이지의 초기 리소스 로딩 완료 이벤트. 지연 로딩 이미지까지 전부 본 시간은 아니다.',
'- `>15 (미완료)`는 15초 관측 종료까지 load 이벤트를 관측하지 못했다는 뜻이다. 원시값 0을 0초로 계산하지 않았다.',
'- 표의 단축률은 각 페이지의 개선 전후 중앙값으로 계산했다. 파일 용량 감소율과 페이지 속도 개선율은 다르다.','',
'## 측정 기준','',
'- 저장소: `baron-consultant/homepage_test`, HEAD `cebb14baf73cf2302c9d53a5df827e9de53f27f5`.',
'- 작업 브랜치: `bff-integration`; 기준 수집 당시 HEAD가 `origin/main`과 같았다. 로컬 미커밋 변경을 포함한다.',
'- 이전 메인 영상·폰트·include 개선과 복원된 로컬 이미지를 이미 포함한 상태가 **이번 개선 전**이다. 과거 `90c1cc9` 측정과 혼합하지 않았다.',
f"- Playwright 1.62 / Edge {after[0]['browser']}, `http://baron.test`, 데스크톱 1365×768, 캐시 비활성화, 매번 새 브라우저 컨텍스트, 서비스 워커 차단.",
'- 다운로드 10 Mbps / 업로드 5 Mbps / 지연 40 ms / CPU 4배 감속. 페이지별 15초 관측 × 3회, 전후 총 48회.',
'- 측정과 이미지 인코딩을 동시에 실행하지 않았다. 스크린샷 촬영 전 측정값을 고정했다.',
'- 로컬 Apache의 전송 조건을 제한한 결과다. 실제 Cloudflare/R2 캐시, 실사용 기기, 운영 인증 상태의 성능은 별도 검증이 필요하다.',
'- 원시 기록·소스 스냅샷: `artifacts/performance/latest-20260915/`의 `before.json`, `after.json`, `baseline-meta.json`, `source-before.zip`, `worktree-before.patch`.','',
'## 병목과 적용한 변경','',
'1. 배경 사진이 수 MB인 데다 CSS 파싱 이후 요청되어 첫 화면 표시가 늦었다. 사진 배경은 WebP 품질 90·최대 1920px로 축소하고, 측정한 첫 화면 배경을 preload/high 우선순위로 요청했다.',
'2. 도면·UI 캡처 PNG와 SVG 안의 base64 PNG도 초기 다운로드에 포함됐다. 도면·UI는 해상도와 RGBA 픽셀을 보존하는 무손실 WebP로 변경했다. SVG의 도형·좌표는 유지하고 내장 래스터만 무손실 변환했다.',
'3. 초기 화면에서 display:none으로 확인된 이미지에만 native lazy loading을 적용했다. 임의로 전체 하단 이미지에 지연 로딩을 걸거나 레이아웃·스크롤 코드를 바꾸지 않았다.',
'4. 닫힌 KNGIL 가이드 모달의 video preload를 metadata에서 none으로 변경했다. 영상 파일 누락 자체는 별도 미해결 항목이다.',
f"5. 총 {len(manifest['assets'])}개 이미지 복사본: {total_before/1e6:.2f} MB → {total_after/1e6:.2f} MB ({pct(total_before,total_after)} 감소). 이는 파일 집합의 합계이며 페이지 하나의 전송량이 아니다. 원본을 남겼으므로 로컬 디스크 사용량은 줄지 않는다.",
'   - 브라우저 비교에서 차이가 남은 `ko/egbim/img/interface_img_02.svg`, `interface_img_03.svg`는 원본 참조를 유지했다. 속도 측정 8페이지의 요청 목록에 없는 파일이므로 비교 수치에는 영향이 없다.',
f"6. 패키지 HTML/CSS {len(manifest['files'])}개 파일에 참조 변경·로딩 힌트를 적용했다. hero preload {sum(x['heroPreload'] for x in manifest['files'])}페이지, 숨김 이미지 lazy {sum(x['hiddenImagesLazy'] for x in manifest['files'])}개. 기존 백업 CSS는 수정 대상에서 제외했다.",
'7. Git 제외한 `assets/media/`도 배포 workflow의 업로드·전체 동기화 제외 목록에 맞췄다. 전체 sync --delete가 별도 관리 미디어를 지우는 일을 방지하기 위한 변경이다.','',
'### 15초 관측 동안 받은 데이터','',
'CDP Network.dataReceived의 encodedDataLength 합계 중앙값이다. 지연 로딩으로 뒤로 미뤄진 이미지, 스크롤 이후 요청, 관측 종료 이후 데이터는 포함하지 않는다.','',
'| 페이지 | 전 → 후 (MB, 10⁶ bytes) | 감소 | DCL 전 → 후 (초) | CLS 전 → 후 |',
'|---|---:|---:|---:|---:|']
for r in summary:
    lines.append(f"| `{r['route']}` | {r['bytesBefore']/1e6:.2f} → {r['bytesAfter']/1e6:.2f} | {pct(r['bytesBefore'],r['bytesAfter'])} | {sec(r['dclBefore'])} → {sec(r['dclAfter'])} | {r['clsBefore']:.4f} → {r['clsAfter']:.4f} |")
lines += ['', 'DCL(HTML 파싱과 초기 스크립트 준비) 중앙값은 0.02~0.45초 증가했다. 첫 화면 우선 로딩을 적용한 상태에서 함께 관측된 변화이며, LCP 개선을 모든 지표의 개선으로 해석하면 안 된다. GAIA 주요기능은 전후 모두 15초 안에 load가 끝나지 않아 전체 로딩 단축량을 확정하지 못했다.']
lines += ['', '### 실제 요청에서 확인한 대형 파일 예시','',
'개선 전 2회차의 완료된 리소스 중 encodedBodySize가 큰 항목이다. 관측 종료 시 미완료였던 요청은 이 표에 없을 수 있다.','',
'| 페이지 | 파일 | 개선 전 bytes |','|---|---|---:|']
for r in before:
    if r['run']!=2: continue
    for resource in sorted(r['metrics']['resources'],key=lambda x:x.get('encodedBodySize',0),reverse=True)[:2]:
        lines.append(f"| `{r['route']}` | `{urlsplit(resource['name']).path}` | {resource['encodedBodySize']} |")
lines += ['', '## 검증 범위와 결과','',
f"- 개선 전 파일 인벤토리 {len(inventory['files']):,}개 / HTML {len(inventory['pages'])}개: 크기, 로컬·외부 참조, 차단 스크립트, 이미지·영상 태그를 기계적으로 조사했다. 모든 파일을 수동 코드 리뷰했다는 뜻은 아니다.",
f"- 최신 전체 HTML smoke {len(smoke)}개: include 조각과 CKEditor 내부 페이지 제외. 공급자 데모·백업도 포함하므로 모두 운영 메뉴 페이지인 것은 아니다.",
f"- 패키지 데스크톱·모바일 탐색 {len(delivery['pages'])}건: 최초 화면, 메뉴 버튼(존재할 때), 스크롤 중 이미지 노출과 JavaScript 오류 기록. 결제·문의 제출·외부 프로그램 실행은 하지 않았다.",
'- 모바일 검사는 동일 Edge 엔진의 390×844 뷰포트다. 실제 휴대폰·iOS Safari 검증은 포함하지 않는다.',
f"- 새 이미지 HTTP 확인 {len(delivery['assets'])}개: 상태/응답 크기 불일치 {len(bad_assets)}개.",
f"- 최종 적용 SVG {len(active_svg)}개: 애니메이션을 같은 6개 시점에 고정한 최초 뷰포트 픽셀 불일치 {len(svg_bad)}개. 내장 이미지 전체 RGBA 일치도 변환 시 검증했다.",
'- 최초 SVG 단순 촬영에서 5개가 불일치했다. 시간을 통제한 재검사로 3개는 일치를 확인했고, 차이가 남은 2개는 최종 적용에서 제외했다. `svg-render-check.json`에는 제외된 시도도 기록되어 있다.',
'- 원본 SVG 참조로 되돌린 인터페이스 페이지는 `smoke-interface-final.json`으로 다시 확인했다. 위 전체 smoke 요약은 이 최종 재검사를 우선한다.',
f"- 자체 JS 중심 Node 문법 검사 {len(syntax)}개: 실패 {sum(not x['ok'] for x in syntax)}개. 기존 오류를 속도 개선과 구분해 [이상 항목 목록](performance-latest-issues.md)에 기록했다.",
'- 인증으로 다른 페이지로 이동한 경우 원래 화면의 기능 검증 성공으로 계산하지 않았다. smoke는 짧은 탐색 검사이므로 기능 전체 보장을 뜻하지 않는다.',
'- 상세 검증: `delivery-check.json`, `smoke-after.json`, `js-syntax.json`; 최신 스크린샷은 `after-*`, `delivery-*`.','',
'## 로컬 확인 및 배포 조건','',
'- 브라우저에서 `http://baron.test/ko/index.html` 또는 위 표의 경로를 연다. `baron.test`는 Laragon의 프로젝트 루트용 가상 호스트다.',
'- `localhost/baron/...`에서는 `/assets/...`가 `localhost/assets/...`로 해석돼 404가 날 수 있다. 이 문제는 R2 버킷 연결과 별개다.',
f"- 최종 적용 이미지 {len(manifest['assets'])}개는 모두 기존 `img/` 아래에 생성되어 Git 제외 상태다. **HTML/CSS만 배포하면 새 이미지가 404가 된다.** [별도 업로드 목록](package-asset-upload.md)을 따라 같은 키로 이미지를 먼저 올려야 한다.",
'- 앞서 만든 `assets/media/index-web.mp4`, 포스터, 채용 WebP도 Git 제외되어 별도 업로드가 필요하다. 원본 파일은 삭제하지 않았다.',
'- 현재 Worker 소스의 SITE_BUCKET은 `baron-hompage-test`다. GitHub secret `CF_R2_BUCKET` 실제 값과 운영 연결은 이번 로컬 테스트로 확인되지 않았다.',
'- 커밋·push·R2 업로드·운영 배포는 실행하지 않았다. 발견된 기존 오류가 있으므로 무조건 즉시 배포 가능하다는 판정은 하지 않는다.','',
'## 재현 명령 (프로젝트 루트 PowerShell)','',
'`.perf-tools`에 Playwright/Pillow 및 Edge가 준비된 현재 환경 기준이다. 기존 결과를 보존하려면 label을 바꾼다. 원본 기준을 재측정하려면 작업 파일을 임의로 덮어쓰지 말고 별도 검증 복사본에 source-before.zip과 보존 원본 이미지를 사용한다.','',
'```powershell',
'python scripts/performance_audit.py --output-dir artifacts/performance/latest-20260915 --base http://baron.test --label recheck --runs 3 --seconds 15 --routes /ko/egbim/value.html,/ko/egbim/primary.html,/ko/tova/value.html,/ko/tova/public.html,/ko/gaia/value.html,/ko/gaia/primary.html,/ko/kngil/value.html,/ko/kngil/primary.html',
'python scripts/performance_audit.py --output-dir artifacts/performance/latest-20260915 --base http://baron.test --smoke --label smoke-recheck',
'python scripts/package_delivery_check.py',
'```','',
'## 회차별 원시 지표 요약','',
'| 구분 | 페이지 | 회차 | LCP (초) | load (초) | 수신 MB | JS 오류 |',
'|---|---|---:|---:|---:|---:|---:|']
for label,data in [('전',before),('후',after)]:
    for r in data:
        lines.append(f"| {label} | `{r['route']}` | {r['run']} | {sec((r['metrics'].get('lcp') or {}).get('ms',0))} | {sec(r['metrics']['navigation']['loadEventEnd'])} | {r['receivedBytes']/1e6:.2f} | {len(r['errors'])} |")
(DOC/'performance-latest-20260915.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

issues=['# 최신 소스 이상 항목 및 후속 확인 — 2026-09-15','',
'이번 작업은 속도 개선에 한정했다. 별도 기능 오류와 환경 관련 진단을 아래에 기록했다.','',
'## 배포 전 확인할 항목','',
'| 우선순위 | 항목 | 영향 / 확인 방법 |','|---|---|---|',
'| 높음 | 새 WebP/SVG·assets/media가 Git 제외 | HTML/CSS 배포 전에 [업로드 목록](package-asset-upload.md)의 파일을 동일 경로로 별도 배포해야 한다. |',
'| 높음 | R2 대상 일치 여부 미확인 | Worker 소스 SITE_BUCKET=`baron-hompage-test`. CI의 CF_R2_BUCKET 실제 값은 확인하지 못했다. |',
'| 높음 | KNGIL 가이드 파일 누락 | `ko/kngil/img/video/kngil_guide.mp4`와 poster가 로컬에 없다. preload=none은 초기 요청만 줄이며 재생 문제를 해결하지 않는다. |',
'| 높음 | 채용 지원 스크립트 문법 오류 | `assets/js/apply.js:400` 파싱 실패. recruit_apply 브라우저에서도 오류 확인. |',
'| 높음 | TOVA 과거 index 진입 페이지 오류 | ko/en `js/common.js:993`의 style 중복 선언. `img/main_1.mp4`, `some_api_endpoint`도 404. |',
'| 중간 | EG-BIM buy/forbim 오류 | buy.js 파일 404, forbim에서 null.style 접근 오류. 현재 속도 측정의 value/primary와 구분해야 한다. |',
'| 중간 | DX·채용 상세 include 실행 오류 | urlParams 중복 선언으로 appendChild 실행 실패. 별도 코드 정리가 필요하다. |',
'| 중간 | TOVA public 가로 넘침 | 원본/최적화본 모두 데스크톱 1365px에서 문서 1567px, 모바일 390px에서 983px. SVG object의 고정 너비가 남아 있다. |',
'| 중간 | 로그인 필요 페이지의 로컬 SSO 이동 | 최종 URL이 달라진 페이지는 원래 콘텐츠의 기능 검증 미완료. 인증된 브라우저에서 확인이 필요하다. |',
'| 중간 | 백업·데모·과거 진입 페이지 존재 | 실제 메뉴에서 사용하는 경로와 분리해 관리할 후보. 이번에 삭제·이동하지 않았다. |','',
'## JavaScript 문법 검사 실패','',
'| 파일 | 진단 |','|---|---|']
for x in syntax:
    if not x['ok']:
        detail=next((s for s in x['output'].splitlines() if 'SyntaxError:' in s),x['output'])
        issues.append(f"| `{x['file']}` | {clean(detail)} |")
issues += ['', '이 검사는 파일 자체의 파싱 결과다. 현재 페이지에서 로드되지 않는 구버전 스크립트 오류와 실제 브라우저 오류를 구분해야 한다.','',
'## 브라우저 smoke에서 발견한 경로별 증상','',
'include 조각·CKEditor 내부를 제외한 HTML 전체를 탐색했다. `load=0`만으로 오류 판정하지 않았다. JS 오류, 4xx/5xx, 요청 실패, 최종 URL 변경을 아래에 기록한다. 네트워크 실패는 외부 서비스·로컬 환경 영향일 수 있으며 원인을 단정하지 않는다.','',
'| 경로 | 증상 |','|---|---|']
for r in smoke:
    notes=[]
    actual=r['metrics'].get('actualUrl','')
    expected=r['base']+r['route']
    if actual and unquote(actual)!=unquote(expected):
        notes.append('이동: '+short_url(actual)+(' (SSO redirect_uri 등록 불일치)' if 'sso.hmac.kr' in actual and 'error=' in actual else ''))
    if r.get('timeout'): notes.append('탐색: '+r['timeout'])
    if r['errors']: notes.append('JS: '+'; '.join(dict.fromkeys(r['errors'])))
    http=list(dict.fromkeys(f"{x['status']} {short_url(x['url'])}" for x in r['responses'] if x['status']>=400))
    if http: notes.append('HTTP: '+'; '.join(http[:6]))
    failures=list(dict.fromkeys(f"{x['error']} {short_url(x['url'])}" for x in r['failures']))
    if failures: notes.append('요청 실패: '+'; '.join(failures[:2]))
    if notes: issues.append(f"| `{r['route']}` | {' / '.join(clean(s) for s in notes)} |")
issues += ['', '## 스크롤·모바일 검증에서 발견한 증상','',
'| 경로 / 너비 | 증상 |','|---|---|']
for r in delivery['pages']:
    notes=[]
    if r.get('checkError'): notes.append(r['checkError'])
    if r.get('errors'): notes+=r['errors']
    if r.get('brokenCompleteImages'): notes.append('실패한 img: '+'; '.join(r['brokenCompleteImages']))
    if r.get('badResponses'): notes.append('HTTP: '+'; '.join(f"{x['status']} {urlsplit(x['url']).path}" for x in r['badResponses']))
    if r.get('top',{}).get('scrollWidth',0)>r['viewport'][0]+2: notes.append(f"가로 넘침: {r['top']['scrollWidth']}px / viewport {r['viewport'][0]}px")
    if r.get('menuOpened') is False or r.get('menuClosed') is False: notes.append('메뉴 열기/닫기 검사 실패')
    if notes: issues.append(f"| `{r['route']}` / {r['viewport'][0]} | {' / '.join(clean(s) for s in notes)} |")
issues += ['', '## 추가 진단 및 정적 참조 검사의 해석','',
'TOVA 가로 넘침은 원본 스냅샷과 현재 소스를 별도 로컬 HTTP 서버에서 비교했다. 양쪽 모두 SVG object 6개가 정상 로드되고 같은 너비였다(`tova-overflow-check.json`). 요청 가로채기 방식의 초기 진단은 object 로드를 막았으므로 판정에서 제외했다.',
'',
'`inventory.json`은 모든 HTML/CSS/JS의 로컬·외부 참조 후보를 보존한다. CKEditor 스킨, 사용하지 않는 CSS, JavaScript 내부 문자열, 과거 백업 경로도 포함하므로 `exists=false` 건수를 실제 사용자 화면의 404 건수로 해석하면 안 된다. 실제 요청 여부는 위 브라우저 결과를 우선한다.',
'','## 다음 속도 개선 후보','',
'- 여전히 load가 오래 걸리는 페이지의 화면 아래 대형 이미지를 섹션별로 측정해 지연 로딩 확대 검토. 현재 GSAP가 이미지 높이에 의존할 수 있어 레이아웃 검증을 동반해야 한다.',
'- 외부 CDN 스크립트와 광고·분석 요청의 지연은 실제 운영 환경에서 따로 측정.',
'- 데스크톱/모바일용 화면 크기에 맞는 추가 이미지 변형은 고해상도 모니터 시각 검수 후 적용.',
'- SSO가 필요한 페이지는 인증된 테스트 계정·운영과 같은 도메인 조건에서 별도 검증.','']
(DOC/'performance-latest-issues.md').write_text('\n'.join(issues),encoding='utf-8')

uploads=['# 패키지 속도 개선 이미지 — 별도 업로드 목록','',
'생성 위치는 프로젝트 루트 기준이며 R2 객체 키도 같은 상대 경로를 사용한다. 아래 파일은 모두 Git 제외 대상이다. **이미지를 먼저 올리고 HTTP 200을 확인한 뒤 참조 HTML/CSS를 배포해야 한다.** 이번 작업에서 업로드는 하지 않았다.','',
f"총 {len(manifest['assets'])}개 / {total_after:,} bytes. 보존된 원본은 삭제하지 않는다. 목록은 `artifacts/performance/latest-20260915/asset-optimizations.json`에서 생성했다.",
'','## 이번 패키지 이미지','',
'| 업로드 경로 / 객체 키 | 개선 전 bytes | 업로드 bytes | 방식 |','|---|---:|---:|---|']
for a in manifest['assets']:
    uploads.append(f"| `{a['output']}` | {a['beforeBytes']} | {a['afterBytes']} | {a['mode']} |")
uploads += ['', '## 앞선 메인·채용 개선의 별도 미디어','',
'아래 파일도 Git에서 제외된다. 이번 패키지 비교의 개선 전부터 사용되고 있었다.','',
'| 경로 | bytes |','|---|---:|']
for p in sorted((ROOT/'assets/media').glob('*')):
    if p.is_file(): uploads.append(f'| `{p.relative_to(ROOT).as_posix()}` | {p.stat().st_size} |')
(DOC/'package-asset-upload.md').write_text('\n'.join(uploads)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
