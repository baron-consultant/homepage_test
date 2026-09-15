"""Write Unicode audit reports from the captured HTTP evidence."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/performance/latest-20260915'
refs=json.loads((OUT/'missing-asset-source-references.json').read_text(encoding='utf-8'))
md=['# 이미지 21개 404 원인 조사','',
'## 결론','',
'새 HTML/CSS가 요청하는 최적화 파일 경로에서 서버가 HTTP 404 / Not Found를 반환한다. 21개 모두 대응하는 기존 원본 URL은 200이고, 새 파일의 로컬 URL도 200이다. 서버가 새 파일명에 해당하는 리소스를 제공하지 못하는 상태다.','',
'예: `ko/tova/public.html:196`의 `./img/public_process_01.perf.svg`는 `/ko/tova/img/public_process_01.perf.svg`로 해석된다. 기존 `/ko/tova/img/public_process_01.svg`는 다른 객체 키이므로 새 파일을 대신 제공하지 않는다.','',
'## 검사 근거','',
'- 고유 쿼리를 붙인 GET: 새 파일 21개 모두 404, 대응 원본 21개 모두 200.',
'- 같은 새 파일 21개를 로컬 baron.test에서 요청하면 모두 200.',
'- 기존 SVG 18개는 image/svg+xml로 정상 제공된다. 다른 .perf.webp도 200이다. SVG 전체 차단이나 모든 최적화 파일명의 차단을 뒷받침하는 증거는 없다.',
'- 응답은 이미지 디코딩 오류가 아니라 HTTP 404 / text/plain / Not Found다.',
'- 상대경로를 HTML/CSS 위치 기준으로 계산한 결과가 검사한 운영 URL과 일치한다.',
'- 현재 Worker 소스는 SVG/WebP를 지원한다. URL의 선행 /를 제거한 키로 SITE_BUCKET.get을 호출하고, 객체를 찾지 못하면 404를 반환한다. 운영 Worker 배포본을 원격으로 읽어 비교한 것은 아니다.',
'- 중첩 폴더가 빠진 몇 가지 대체 경로도 404였다. 모든 가능한 업로드 위치를 탐색한 것은 아니다.','',
'## 아직 확정할 수 없는 부분','',
'R2 객체 목록과 업로드 로그는 조회하지 않았다. 따라서 업로드 누락, 다른 폴더 업로드, 파일명 변경 중 정확히 어느 과정에서 발생했는지는 확정할 수 없다. 변수·엔드포인트·버킷은 사용자가 정상으로 확인한 상태를 기준으로 한다.','',
'누락 분포는 새 SVG 18개 전체와 WebP 3개다. 업로드 선택에서 SVG가 빠졌거나 일부 파일·하위 폴더가 누락되었을 가능성이 있으나, 이는 분포에 근거한 추정이다.','',
'## 필요한 객체 키와 참조 위치','',
'키는 버킷 루트 기준이며 앞에 /를 붙이지 않는다. ZIP 이름의 상위 폴더를 추가하면 요청 경로와 달라진다.','',
'| 객체 키 | 참조 위치 |','|---|---|']
for key,locations in refs.items():
    md.append(f"| `{key}` | {', '.join('`'+p+'`' for p in locations)} |")
md+=['','[21개 경로 목록](missing-upload-assets.txt). 폴더 구조를 유지한 압축본: `artifacts/performance/latest-20260915/missing-upload-assets.zip`.','',
'원시 기록: `missing-asset-diagnosis.json`, `missing-asset-source-references.json`, `missing-asset-local-check.json`. 경로 변경·업로드·배포는 실행하지 않았다.','']
(ROOT/'docs/missing-asset-diagnosis.md').write_text('\n'.join(md),encoding='utf-8')

ready='''# 배포 전 최종 점검 — 업로드 후 재확인

## 판정: 새 파일 21개가 아직 404

사용자가 변수·엔드포인트·버킷을 정상으로 확인한 상태에서 운영 주소 https://baroncs.co.kr 에 GET 검사를 수행했다.

| 검사 | 결과 |
|---|---|
| 전체 대상 | 이미지 388개 + 영상 1개 = 389개 |
| 정상 응답 | 368개 HTTP 200, 형식 정상, 로컬 파일 첫 1KB 일치 |
| 접근 불가 | SVG 18개 + WebP 3개 = 21개 HTTP 404 |
| 캐시 구분 재검사 | 고유 쿼리를 붙여도 21개 모두 404 |
| 기존 원본과 비교 | 대응 원본 21개 모두 HTTP 200 |
| 새 파일 로컬 검사 | 같은 21개 경로 모두 HTTP 200 |

정상 파일의 전체 해시를 비교한 것은 아니다. 검사에서 읽은 본문은 최대 1KB다. 이전에 누락됐던 메인 영상과 EG-BIM 소개 배경은 현재 200이다.

요청 URL의 파일명과 운영에서 제공되는 객체 키가 일치해야 한다. [원인 조사](missing-asset-diagnosis.md)와 [추가 확인할 21개 경로](missing-upload-assets.txt)를 참조한다.

## 기존 검증과 남은 기능 문제

- 변경 JS 5개 문법 검사와 git diff --check 통과.
- Playwright 전후 48회 성능 측정, HTML 155개 smoke, 데스크톱/모바일 22건 검사 결과는 기존 보고서 참조.
- 채용 apply.js 문법 오류, TOVA 구형 common.js 중복 선언, KNGIL 가이드 누락 등 기존 기능 문제는 미해결이다. [이상 항목 목록](performance-latest-issues.md) 참조.
- 현재 브랜치는 bff-integration이며 자동 배포는 main push로 실행된다.

21개 URL의 정상 응답을 확인한 뒤 코드 배포와 배포 후 화면 검증을 진행해야 한다. 이 점검에서 업로드·커밋·push·배포는 실행하지 않았다.

근거: artifacts/performance/latest-20260915/deployment-upload-verification.json 및 missing-asset-diagnosis.json.
'''
(ROOT/'docs/deployment-readiness.md').write_text(ready,encoding='utf-8')

# Repair earlier PowerShell stdin text encoding without modifying inventory tables.
p=ROOT/'docs/package-asset-upload.md'
s=p.read_text(encoding='utf-8')
start=s.index('생성 위치는')
prefix='# 패키지 속도 개선 이미지 — 별도 업로드 목록\n\n기존에 운영 주소에서 받은 원본은 다시 올릴 대상이 아니다. 새 이미지 388개(패키지 383개 + 메인 포스터 1개 + 채용 4개)는 [새 이미지 목록](new-generated-images.txt)을 따른다. 영상 assets/media/index-web.mp4 1개도 별도 업로드 대상이다.\n\n'
p.write_text(prefix+s[start:],encoding='utf-8')
p=ROOT/'docs/image-reference-audit.md'
s=p.read_text(encoding='utf-8');start=s.index('이미지 참조를 수정하지 않고')
prefix='# 이미지 참조 경로 검사\n\n## 결론\n\n새 이미지의 정적 참조 513건은 모두 현재 위치 기준 상대경로다. 전체 기존 소스에는 루트 기준 경로 후보 411건과 외부 URL 후보 45건도 있다. 동적 문자열 27건은 실행 결과에 따라 달라질 수 있다.\n\n'
p.write_text(prefix+s[start:],encoding='utf-8')
print('Wrote UTF-8 diagnosis and readiness reports.')
