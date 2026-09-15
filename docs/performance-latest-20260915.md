# 최신 소스 로딩 속도 개선 및 재검증 — 2026-09-15

## 결론

패키지 S/W의 페이지 구조·메뉴·애니메이션 로직을 리팩토링하지 않고, 이미지 전송량과 요청 우선순위를 조정했다. 아래 수치는 최신 소스에서 새로 수집한 동일 조건 3회 중앙값이다. 운영 서버 실측값은 아니다.

| 페이지 | LCP 개선 전 → 후 (초) | LCP 단축 | 전체 load 개선 전 → 후 (초) | load 단축 |
|---|---:|---:|---:|---:|
| `/ko/egbim/value.html` | 13.90 → 1.63 | 88.3% | 13.81 → 8.08 | 41.5% |
| `/ko/egbim/primary.html` | 4.53 → 1.95 | 56.9% | 7.93 → 5.20 | 34.4% |
| `/ko/tova/value.html` | 8.10 → 1.96 | 75.8% | 8.36 → 6.50 | 22.2% |
| `/ko/tova/public.html` | 6.57 → 1.73 | 73.7% | 12.14 → 8.39 | 30.9% |
| `/ko/gaia/value.html` | 11.35 → 2.55 | 77.5% | 11.29 → 6.15 | 45.6% |
| `/ko/gaia/primary.html` | 7.36 → 2.72 | 63.1% | >15 (미완료) → >15 (미완료) | 관측 한계로 정확한 비율 제외 |
| `/ko/kngil/value.html` | 7.97 → 2.77 | 65.3% | 8.03 → 5.90 | 26.5% |
| `/ko/kngil/primary.html` | 6.72 → 2.66 | 60.4% | >15 (미완료) → 14.02 | 관측 한계로 정확한 비율 제외 |

- LCP: 첫 화면에서 가장 큰 콘텐츠가 표시된 시점. 사용자가 화면이 나타났다고 느끼는 속도에 가깝다.
- load: 일반 이미지 등 페이지의 초기 리소스 로딩 완료 이벤트. 지연 로딩 이미지까지 전부 본 시간은 아니다.
- `>15 (미완료)`는 15초 관측 종료까지 load 이벤트를 관측하지 못했다는 뜻이다. 원시값 0을 0초로 계산하지 않았다.
- 표의 단축률은 각 페이지의 개선 전후 중앙값으로 계산했다. 파일 용량 감소율과 페이지 속도 개선율은 다르다.

## 측정 기준

- 저장소: `baron-consultant/homepage_test`, HEAD `cebb14baf73cf2302c9d53a5df827e9de53f27f5`.
- 작업 브랜치: `bff-integration`; 기준 수집 당시 HEAD가 `origin/main`과 같았다. 로컬 미커밋 변경을 포함한다.
- 이전 메인 영상·폰트·include 개선과 복원된 로컬 이미지를 이미 포함한 상태가 **이번 개선 전**이다. 과거 `90c1cc9` 측정과 혼합하지 않았다.
- Playwright 1.62 / Edge 153.0.4234.32, `http://baron.test`, 데스크톱 1365×768, 캐시 비활성화, 매번 새 브라우저 컨텍스트, 서비스 워커 차단.
- 다운로드 10 Mbps / 업로드 5 Mbps / 지연 40 ms / CPU 4배 감속. 페이지별 15초 관측 × 3회, 전후 총 48회.
- 측정과 이미지 인코딩을 동시에 실행하지 않았다. 스크린샷 촬영 전 측정값을 고정했다.
- 로컬 Apache의 전송 조건을 제한한 결과다. 실제 Cloudflare/R2 캐시, 실사용 기기, 운영 인증 상태의 성능은 별도 검증이 필요하다.
- 원시 기록·소스 스냅샷: `artifacts/performance/latest-20260915/`의 `before.json`, `after.json`, `baseline-meta.json`, `source-before.zip`, `worktree-before.patch`.

## 병목과 적용한 변경

1. 배경 사진이 수 MB인 데다 CSS 파싱 이후 요청되어 첫 화면 표시가 늦었다. 사진 배경은 WebP 품질 90·최대 1920px로 축소하고, 측정한 첫 화면 배경을 preload/high 우선순위로 요청했다.
2. 도면·UI 캡처 PNG와 SVG 안의 base64 PNG도 초기 다운로드에 포함됐다. 도면·UI는 해상도와 RGBA 픽셀을 보존하는 무손실 WebP로 변경했다. SVG의 도형·좌표는 유지하고 내장 래스터만 무손실 변환했다.
3. 초기 화면에서 display:none으로 확인된 이미지에만 native lazy loading을 적용했다. 임의로 전체 하단 이미지에 지연 로딩을 걸거나 레이아웃·스크롤 코드를 바꾸지 않았다.
4. 닫힌 KNGIL 가이드 모달의 video preload를 metadata에서 none으로 변경했다. 영상 파일 누락 자체는 별도 미해결 항목이다.
5. 총 383개 이미지 복사본: 373.76 MB → 230.04 MB (38.5% 감소). 이는 파일 집합의 합계이며 페이지 하나의 전송량이 아니다. 원본을 남겼으므로 로컬 디스크 사용량은 줄지 않는다.
   - 브라우저 비교에서 차이가 남은 `ko/egbim/img/interface_img_02.svg`, `interface_img_03.svg`는 원본 참조를 유지했다. 속도 측정 8페이지의 요청 목록에 없는 파일이므로 비교 수치에는 영향이 없다.
6. 패키지 HTML/CSS 38개 파일에 참조 변경·로딩 힌트를 적용했다. hero preload 14페이지, 숨김 이미지 lazy 21개. 기존 백업 CSS는 수정 대상에서 제외했다.
7. Git 제외한 `assets/media/`도 배포 workflow의 업로드·전체 동기화 제외 목록에 맞췄다. 전체 sync --delete가 별도 관리 미디어를 지우는 일을 방지하기 위한 변경이다.

### 15초 관측 동안 받은 데이터

CDP Network.dataReceived의 encodedDataLength 합계 중앙값이다. 지연 로딩으로 뒤로 미뤄진 이미지, 스크롤 이후 요청, 관측 종료 이후 데이터는 포함하지 않는다.

| 페이지 | 전 → 후 (MB, 10⁶ bytes) | 감소 | DCL 전 → 후 (초) | CLS 전 → 후 |
|---|---:|---:|---:|---:|
| `/ko/egbim/value.html` | 16.65 → 9.73 | 41.6% | 1.61 → 1.63 | 0.0028 → 0.0028 |
| `/ko/egbim/primary.html` | 9.55 → 6.05 | 36.6% | 1.87 → 2.32 | 0.0035 → 0.0025 |
| `/ko/tova/value.html` | 10.15 → 7.77 | 23.5% | 1.89 → 2.01 | 0.0003 → 0.0003 |
| `/ko/tova/public.html` | 8.44 → 5.61 | 33.6% | 1.74 → 2.14 | 0.0032 → 0.0032 |
| `/ko/gaia/value.html` | 13.65 → 6.58 | 51.8% | 2.70 → 2.82 | 0.0000 → 0.0000 |
| `/ko/gaia/primary.html` | 18.40 → 18.34 | 0.3% | 2.76 → 3.11 | 0.0021 → 0.0021 |
| `/ko/kngil/value.html` | 9.15 → 6.22 | 32.0% | 3.20 → 3.60 | 0.0000 → 0.0000 |
| `/ko/kngil/primary.html` | 18.24 → 17.09 | 6.3% | 3.23 → 3.35 | 0.0023 → 0.0023 |

DCL(HTML 파싱과 초기 스크립트 준비) 중앙값은 0.02~0.45초 증가했다. 첫 화면 우선 로딩을 적용한 상태에서 함께 관측된 변화이며, LCP 개선을 모든 지표의 개선으로 해석하면 안 된다. GAIA 주요기능은 전후 모두 15초 안에 load가 끝나지 않아 전체 로딩 단축량을 확정하지 못했다.

### 실제 요청에서 확인한 대형 파일 예시

개선 전 2회차의 완료된 리소스 중 encodedBodySize가 큰 항목이다. 관측 종료 시 미완료였던 요청은 이 표에 없을 수 있다.

| 페이지 | 파일 | 개선 전 bytes |
|---|---|---:|
| `/ko/egbim/value.html` | `/ko/egbim/img/value_introbg.png` | 4678800 |
| `/ko/egbim/value.html` | `/ko/egbim/img/dia_valuebg02.png` | 3809536 |
| `/ko/egbim/primary.html` | `/ko/egbim/img/primary_style_bg.png` | 1043595 |
| `/ko/egbim/primary.html` | `/ko/egbim/img/printarea_img_01.png` | 1019373 |
| `/ko/tova/value.html` | `/ko/tova/img/value_intro_bg.jpg` | 1954590 |
| `/ko/tova/value.html` | `/ko/tova/img/value_intro_summary2.jpg` | 1375068 |
| `/ko/tova/public.html` | `/ko/tova/img/public_process_01.svg` | 2558063 |
| `/ko/tova/public.html` | `/ko/tova/img/slide_img_subway.png` | 1996522 |
| `/ko/gaia/value.html` | `/ko/gaia/img/value_intro_bg_top.png` | 4500150 |
| `/ko/gaia/value.html` | `/ko/gaia/img/value_screen_bg.png` | 1713477 |
| `/ko/gaia/primary.html` | `/ko/gaia/img/location_img_03_01.png` | 1704772 |
| `/ko/gaia/primary.html` | `/ko/gaia/img/model_img_03_01.png` | 1490067 |
| `/ko/kngil/value.html` | `/ko/kngil/img/value/bg_value_visual.jpg` | 1747713 |
| `/ko/kngil/value.html` | `/ko/kngil/img/value/bg_value_custom.jpg` | 1049641 |
| `/ko/kngil/primary.html` | `/ko/kngil/img/primary/img_progress_01.png` | 1439904 |
| `/ko/kngil/primary.html` | `/ko/kngil/img/primary/img_report_01.png` | 1351236 |

## 검증 범위와 결과

- 개선 전 파일 인벤토리 4,210개 / HTML 249개: 크기, 로컬·외부 참조, 차단 스크립트, 이미지·영상 태그를 기계적으로 조사했다. 모든 파일을 수동 코드 리뷰했다는 뜻은 아니다.
- 최신 전체 HTML smoke 155개: include 조각과 CKEditor 내부 페이지 제외. 공급자 데모·백업도 포함하므로 모두 운영 메뉴 페이지인 것은 아니다.
- 패키지 데스크톱·모바일 탐색 22건: 최초 화면, 메뉴 버튼(존재할 때), 스크롤 중 이미지 노출과 JavaScript 오류 기록. 결제·문의 제출·외부 프로그램 실행은 하지 않았다.
- 모바일 검사는 동일 Edge 엔진의 390×844 뷰포트다. 실제 휴대폰·iOS Safari 검증은 포함하지 않는다.
- 새 이미지 HTTP 확인 385개: 상태/응답 크기 불일치 0개.
- 최종 적용 SVG 18개: 애니메이션을 같은 6개 시점에 고정한 최초 뷰포트 픽셀 불일치 0개. 내장 이미지 전체 RGBA 일치도 변환 시 검증했다.
- 최초 SVG 단순 촬영에서 5개가 불일치했다. 시간을 통제한 재검사로 3개는 일치를 확인했고, 차이가 남은 2개는 최종 적용에서 제외했다. `svg-render-check.json`에는 제외된 시도도 기록되어 있다.
- 원본 SVG 참조로 되돌린 인터페이스 페이지는 `smoke-interface-final.json`으로 다시 확인했다. 위 전체 smoke 요약은 이 최종 재검사를 우선한다.
- 자체 JS 중심 Node 문법 검사 204개: 실패 3개. 기존 오류를 속도 개선과 구분해 [이상 항목 목록](performance-latest-issues.md)에 기록했다.
- 인증으로 다른 페이지로 이동한 경우 원래 화면의 기능 검증 성공으로 계산하지 않았다. smoke는 짧은 탐색 검사이므로 기능 전체 보장을 뜻하지 않는다.
- 상세 검증: `delivery-check.json`, `smoke-after.json`, `js-syntax.json`; 최신 스크린샷은 `after-*`, `delivery-*`.

## 로컬 확인 및 배포 조건

- 브라우저에서 `http://baron.test/ko/index.html` 또는 위 표의 경로를 연다. `baron.test`는 Laragon의 프로젝트 루트용 가상 호스트다.
- `localhost/baron/...`에서는 `/assets/...`가 `localhost/assets/...`로 해석돼 404가 날 수 있다. 이 문제는 R2 버킷 연결과 별개다.
- 최종 적용 이미지 383개는 모두 기존 `img/` 아래에 생성되어 Git 제외 상태다. **HTML/CSS만 배포하면 새 이미지가 404가 된다.** [별도 업로드 목록](package-asset-upload.md)을 따라 같은 키로 이미지를 먼저 올려야 한다.
- 앞서 만든 `assets/media/index-web.mp4`, 포스터, 채용 WebP도 Git 제외되어 별도 업로드가 필요하다. 원본 파일은 삭제하지 않았다.
- 현재 Worker 소스의 SITE_BUCKET은 `baron-hompage-test`다. GitHub secret `CF_R2_BUCKET` 실제 값과 운영 연결은 이번 로컬 테스트로 확인되지 않았다.
- 커밋·push·R2 업로드·운영 배포는 실행하지 않았다. 발견된 기존 오류가 있으므로 무조건 즉시 배포 가능하다는 판정은 하지 않는다.

## 재현 명령 (프로젝트 루트 PowerShell)

`.perf-tools`에 Playwright/Pillow 및 Edge가 준비된 현재 환경 기준이다. 기존 결과를 보존하려면 label을 바꾼다. 원본 기준을 재측정하려면 작업 파일을 임의로 덮어쓰지 말고 별도 검증 복사본에 source-before.zip과 보존 원본 이미지를 사용한다.

```powershell
python scripts/performance_audit.py --output-dir artifacts/performance/latest-20260915 --base http://baron.test --label recheck --runs 3 --seconds 15 --routes /ko/egbim/value.html,/ko/egbim/primary.html,/ko/tova/value.html,/ko/tova/public.html,/ko/gaia/value.html,/ko/gaia/primary.html,/ko/kngil/value.html,/ko/kngil/primary.html
python scripts/performance_audit.py --output-dir artifacts/performance/latest-20260915 --base http://baron.test --smoke --label smoke-recheck
python scripts/package_delivery_check.py
```

## 회차별 원시 지표 요약

| 구분 | 페이지 | 회차 | LCP (초) | load (초) | 수신 MB | JS 오류 |
|---|---|---:|---:|---:|---:|---:|
| 전 | `/ko/egbim/value.html` | 1 | 13.82 | 13.76 | 16.65 | 0 |
| 전 | `/ko/egbim/value.html` | 2 | 13.90 | 13.81 | 16.65 | 0 |
| 전 | `/ko/egbim/value.html` | 3 | 13.95 | 13.88 | 16.65 | 0 |
| 전 | `/ko/egbim/primary.html` | 1 | 4.53 | 7.94 | 9.55 | 0 |
| 전 | `/ko/egbim/primary.html` | 2 | 4.63 | 7.90 | 9.55 | 0 |
| 전 | `/ko/egbim/primary.html` | 3 | 4.53 | 7.93 | 9.55 | 0 |
| 전 | `/ko/tova/value.html` | 1 | 8.10 | 8.35 | 10.15 | 0 |
| 전 | `/ko/tova/value.html` | 2 | 8.11 | 8.36 | 10.15 | 0 |
| 전 | `/ko/tova/value.html` | 3 | 8.10 | 8.38 | 10.15 | 0 |
| 전 | `/ko/tova/public.html` | 1 | 6.57 | 12.14 | 8.45 | 0 |
| 전 | `/ko/tova/public.html` | 2 | 6.49 | 12.12 | 8.44 | 0 |
| 전 | `/ko/tova/public.html` | 3 | 6.59 | 12.30 | 8.44 | 0 |
| 전 | `/ko/gaia/value.html` | 1 | 11.34 | 11.27 | 13.65 | 0 |
| 전 | `/ko/gaia/value.html` | 2 | 11.35 | 11.29 | 13.64 | 0 |
| 전 | `/ko/gaia/value.html` | 3 | 11.40 | 11.34 | 13.65 | 0 |
| 전 | `/ko/gaia/primary.html` | 1 | 8.08 | >15 (미완료) | 18.33 | 0 |
| 전 | `/ko/gaia/primary.html` | 2 | 7.36 | >15 (미완료) | 18.40 | 0 |
| 전 | `/ko/gaia/primary.html` | 3 | 7.28 | >15 (미완료) | 18.40 | 0 |
| 전 | `/ko/kngil/value.html` | 1 | 7.74 | 7.80 | 9.15 | 0 |
| 전 | `/ko/kngil/value.html` | 2 | 8.07 | 8.18 | 9.16 | 0 |
| 전 | `/ko/kngil/value.html` | 3 | 7.97 | 8.03 | 9.15 | 0 |
| 전 | `/ko/kngil/primary.html` | 1 | 5.79 | >15 (미완료) | 18.28 | 0 |
| 전 | `/ko/kngil/primary.html` | 2 | 6.72 | >15 (미완료) | 18.24 | 0 |
| 전 | `/ko/kngil/primary.html` | 3 | 6.92 | >15 (미완료) | 18.16 | 0 |
| 후 | `/ko/egbim/value.html` | 1 | 1.64 | 8.08 | 9.73 | 0 |
| 후 | `/ko/egbim/value.html` | 2 | 1.57 | 8.12 | 9.73 | 0 |
| 후 | `/ko/egbim/value.html` | 3 | 1.63 | 8.08 | 9.73 | 0 |
| 후 | `/ko/egbim/primary.html` | 1 | 2.04 | 5.20 | 6.05 | 0 |
| 후 | `/ko/egbim/primary.html` | 2 | 1.95 | 5.15 | 6.05 | 0 |
| 후 | `/ko/egbim/primary.html` | 3 | 1.86 | 5.21 | 6.05 | 0 |
| 후 | `/ko/tova/value.html` | 1 | 1.96 | 6.50 | 7.78 | 0 |
| 후 | `/ko/tova/value.html` | 2 | 1.88 | 6.51 | 7.76 | 0 |
| 후 | `/ko/tova/value.html` | 3 | 1.98 | 6.44 | 7.77 | 0 |
| 후 | `/ko/tova/public.html` | 1 | 1.67 | 8.36 | 5.61 | 0 |
| 후 | `/ko/tova/public.html` | 2 | 1.73 | 8.39 | 5.61 | 0 |
| 후 | `/ko/tova/public.html` | 3 | 1.79 | 8.39 | 5.59 | 0 |
| 후 | `/ko/gaia/value.html` | 1 | 2.75 | 6.20 | 6.58 | 0 |
| 후 | `/ko/gaia/value.html` | 2 | 2.51 | 6.15 | 6.58 | 0 |
| 후 | `/ko/gaia/value.html` | 3 | 2.55 | 6.12 | 6.59 | 0 |
| 후 | `/ko/gaia/primary.html` | 1 | 2.72 | >15 (미완료) | 18.34 | 0 |
| 후 | `/ko/gaia/primary.html` | 2 | 2.78 | >15 (미완료) | 18.29 | 0 |
| 후 | `/ko/gaia/primary.html` | 3 | 2.71 | >15 (미완료) | 18.35 | 0 |
| 후 | `/ko/kngil/value.html` | 1 | 2.81 | 5.90 | 6.23 | 0 |
| 후 | `/ko/kngil/value.html` | 2 | 2.77 | 6.04 | 6.22 | 0 |
| 후 | `/ko/kngil/value.html` | 3 | 2.58 | 5.86 | 6.16 | 0 |
| 후 | `/ko/kngil/primary.html` | 1 | 2.79 | 14.03 | 17.10 | 0 |
| 후 | `/ko/kngil/primary.html` | 2 | 2.65 | 14.01 | 17.09 | 0 |
| 후 | `/ko/kngil/primary.html` | 3 | 2.66 | 14.02 | 17.09 | 0 |
