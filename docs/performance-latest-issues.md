# 최신 소스 이상 항목 및 후속 확인 — 2026-09-15

이번 작업은 속도 개선에 한정했다. 별도 기능 오류와 환경 관련 진단을 아래에 기록했다.

## 배포 전 확인할 항목

| 우선순위 | 항목 | 영향 / 확인 방법 |
|---|---|---|
| 높음 | 새 WebP/SVG·assets/media가 Git 제외 | HTML/CSS 배포 전에 [업로드 목록](package-asset-upload.md)의 파일을 동일 경로로 별도 배포해야 한다. |
| 높음 | R2 대상 일치 여부 미확인 | Worker 소스 SITE_BUCKET=`baron-hompage-test`. CI의 CF_R2_BUCKET 실제 값은 확인하지 못했다. |
| 높음 | KNGIL 가이드 파일 누락 | `ko/kngil/img/video/kngil_guide.mp4`와 poster가 로컬에 없다. preload=none은 초기 요청만 줄이며 재생 문제를 해결하지 않는다. |
| 높음 | 채용 지원 스크립트 문법 오류 | `assets/js/apply.js:400` 파싱 실패. recruit_apply 브라우저에서도 오류 확인. |
| 높음 | TOVA 과거 index 진입 페이지 오류 | ko/en `js/common.js:993`의 style 중복 선언. `img/main_1.mp4`, `some_api_endpoint`도 404. |
| 중간 | EG-BIM buy/forbim 오류 | buy.js 파일 404, forbim에서 null.style 접근 오류. 현재 속도 측정의 value/primary와 구분해야 한다. |
| 중간 | DX·채용 상세 include 실행 오류 | urlParams 중복 선언으로 appendChild 실행 실패. 별도 코드 정리가 필요하다. |
| 중간 | TOVA public 가로 넘침 | 원본/최적화본 모두 데스크톱 1365px에서 문서 1567px, 모바일 390px에서 983px. SVG object의 고정 너비가 남아 있다. |
| 중간 | 로그인 필요 페이지의 로컬 SSO 이동 | 최종 URL이 달라진 페이지는 원래 콘텐츠의 기능 검증 미완료. 인증된 브라우저에서 확인이 필요하다. |
| 중간 | 백업·데모·과거 진입 페이지 존재 | 실제 메뉴에서 사용하는 경로와 분리해 관리할 후보. 이번에 삭제·이동하지 않았다. |

## JavaScript 문법 검사 실패

| 파일 | 진단 |
|---|---|
| `assets/js/apply.js` | SyntaxError: Invalid or unexpected token |
| `en/tova/js/common.js` | SyntaxError: Identifier 'style' has already been declared |
| `ko/tova/js/common.js` | SyntaxError: Identifier 'style' has already been declared |

이 검사는 파일 자체의 파싱 결과다. 현재 페이지에서 로드되지 않는 구버전 스크립트 오류와 실제 브라우저 오류를 구분해야 한다.

## 브라우저 smoke에서 발견한 경로별 증상

include 조각·CKEditor 내부를 제외한 HTML 전체를 탐색했다. `load=0`만으로 오류 판정하지 않았다. JS 오류, 4xx/5xx, 요청 실패, 최종 URL 변경을 아래에 기록한다. 네트워크 실패는 외부 서비스·로컬 환경 영향일 수 있으며 원인을 단정하지 않는다.

| 경로 | 증상 |
|---|---|
| `/callback.html` | 이동: sso.hmac.kr/ko/error (SSO redirect_uri 등록 불일치) / HTTP: 401 sso.hmac.kr/api/v1/user/me |
| `/index.html` | 이동: /ko/index.html |
| `/callback/index.html` | 이동: sso.hmac.kr/ko/error (SSO redirect_uri 등록 불일치) / HTTP: 401 sso.hmac.kr/api/v1/user/me |
| `/en/dt_explain.html` | 요청 실패: net::ERR_ABORTED /assets/img/dt/explain_bim_obj.mp4 |
| `/en/dt_sw.html` | 요청 실패: net::ERR_ABORTED /assets/img/dt/sw_toDT_obj.mp4; net::ERR_ABORTED /assets/img/dt/sw_need_obj.mp4 |
| `/en/dx.html` | JS: Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared / HTTP: 403 /assets/css/eng/<path-to-image>; 404 img.youtube.com/vi/TRVL7Rtn08E/hqdefault.jpg; 404 img.youtube.com/vi/wAKT5PQgdgA/hqdefault.jpg; 404 img.youtube.com/vi/a_dWqOR3s98/hqdefault.jpg; 404 img.youtube.com/vi/omL383gPRXg/hqdefault… |
| `/en/dx_250612.html` | JS: Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared / HTTP: 403 /assets/css/<path-to-image>; 404 img.youtube.com/vi/bs0tqiY8H4E/hqdefault.jpg; 404 img.youtube.com/vi/TWUD65ivJiY/hqdefault.jpg; 404 img.youtube.com/vi/jnw_Ji8ojow/hqdefault.jpg; 404 img.youtube.com/vi/Q2SWEAv5h2g/hqdefault.jpg… / 요청 실패: net::ERR_BLOCKED_BY_RESPONSE ogs.google.com/widget/callout |
| `/en/hosting_index1.html` | HTTP: 404 /en/warning.png; 404 /en/traffic_image.jpg |
| `/en/video_ex.html` | 요청 실패: net::ERR_ABORTED www.youtube.com/api/stats/qoe |
| `/ko/br_future.html` | 요청 실패: net::ERR_ABORTED /assets/img/br/future_intro_bg.mp4 |
| `/ko/br_future_bak_251103.html` | 요청 실패: net::ERR_ABORTED /assets/img/br/future_intro_bg.mp4 |
| `/ko/dt_explain.html` | 요청 실패: net::ERR_ABORTED /assets/img/dt/explain_bim_obj.mp4 |
| `/ko/dx.html` | JS: Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared / HTTP: 403 /assets/css/<path-to-image>; 404 img.youtube.com/vi/a_dWqOR3s98/hqdefault.jpg; 404 img.youtube.com/vi/TRVL7Rtn08E/hqdefault.jpg; 404 img.youtube.com/vi/wAKT5PQgdgA/hqdefault.jpg; 404 img.youtube.com/vi/omL383gPRXg/hqdefault.jpg… |
| `/ko/dx_250612.html` | JS: Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared / HTTP: 403 /assets/css/<path-to-image>; 404 img.youtube.com/vi/Q2SWEAv5h2g/hqdefault.jpg; 404 img.youtube.com/vi/bs0tqiY8H4E/hqdefault.jpg; 404 img.youtube.com/vi/TWUD65ivJiY/hqdefault.jpg; 404 img.youtube.com/vi/jnw_Ji8ojow/hqdefault.jpg… / 요청 실패: net::ERR_BLOCKED_BY_RESPONSE ogs.google.com/widget/callout |
| `/ko/hosting_index1.html` | HTTP: 404 /ko/warning.png; 404 /ko/traffic_image.jpg |
| `/ko/video_ex.html` | 요청 실패: net::ERR_ABORTED www.youtube.com/api/stats/qoe |
| `/portfolio/compilation.html` | 요청 실패: net::ERR_ABORTED www.youtube.com/api/stats/qoe; net::ERR_ABORTED www.youtube.com/api/stats/playback |
| `/portfolio/ux.html` | 요청 실패: net::ERR_ABORTED i.ytimg.com/vi/m2SH3-V9chY/default.jpg; net::ERR_ABORTED www.youtube.com/api/stats/qoe |
| `/recruit/br_recruit.html` | 이동: sso.hmac.kr/ko/error (SSO redirect_uri 등록 불일치) / HTTP: 401 sso.hmac.kr/api/v1/user/me |
| `/recruit/recruit_apply.html` | 이동: sso.hmac.kr/ko/error (SSO redirect_uri 등록 불일치) / JS: Invalid or unexpected token |
| `/recruit/recruit_faq.html` | 이동: sso.hmac.kr/ko/error (SSO redirect_uri 등록 불일치) / HTTP: 401 sso.hmac.kr/api/v1/user/me |
| `/recruit/recruit_view.html` | 이동: sso.hmac.kr/ko/error (SSO redirect_uri 등록 불일치) / JS: Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared / HTTP: 401 sso.hmac.kr/api/v1/user/me |
| `/ko/egbim/buy.html` | HTTP: 404 /ko/egbim/js/buy.js / 요청 실패: net::ERR_ABORTED /ko/egbim/js/buy.js |
| `/ko/egbim/forbim.html` | JS: Cannot read properties of null (reading 'style') |
| `/ko/egbim/interface.html` | 요청 실패: net::ERR_ABORTED /ko/egbim/img/interface_img_01.svg |
| `/ko/gaia/buy.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/gaia/further.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/gaia/index.html` | JS: The play() request was interrupted by a call to pause(). / 요청 실패: net::ERR_ABORTED /ko/gaia/img/main_1.mp4; net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/gaia/primary.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/gaia/results.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/gaia/value.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/kngil/analysis.html` | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg / 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/kngil/buy.html` | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg / 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/kngil/primary.html` | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg / 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/kngil/provided.html` | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg / 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/kngil/results.html` | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg / 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/kngil/value.html` | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg / 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/tova/buy.html` | 요청 실패: net::ERR_ABORTED /ko/tova/img/buy_vdieo.mp4; net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/tova/index.html` | JS: Identifier 'style' has already been declared; The play() request was interrupted by a call to pause(). / HTTP: 404 /ko/tova/img/main_1.mp4; 404 /ko/tova/some_api_endpoint / 요청 실패: net::ERR_ABORTED /ko/tova/img/main_01.mp4; net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/tova/primary.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/tova/public.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/tova/road.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/ko/tova/value.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/egbim/buy.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/egbim/floorplan.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/egbim/forbim.html` | JS: Cannot read properties of null (reading 'style') / 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/egbim/interface.html` | 요청 실패: net::ERR_ABORTED /en/egbim/img/interface_img_01.svg; net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/egbim/primary.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/egbim/value.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/gaia/buy.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/gaia/further.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/gaia/index.html` | JS: The play() request was interrupted by a call to pause(). / 요청 실패: net::ERR_ABORTED /en/gaia/img/main_1.mp4; net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/gaia/primary.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/gaia/results.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/gaia/value.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/tova/buy.html` | 요청 실패: net::ERR_ABORTED /en/tova/img/buy_vdieo.mp4; net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/tova/index.html` | JS: Identifier 'style' has already been declared; Failed to load because no supported source was found. / HTTP: 404 /en/tova/theme/basic/skin/qa/basic/style.css; 404 /en/tova/img/main_1_T.mp4; 404 /en/tova/img/main_1_O.mp4; 404 /en/tova/img/main_1_V.mp4; 404 /en/tova/img/main_1_A.mp4; 404 /en/tova/img/main_1.mp4 / 요청 실패: net::ERR_ABORTED /en/tova/theme/basic/skin/qa/basic/style.css; net::ERR_ABORTED /en/tova/img/main_1_T.mp4 |
| `/en/tova/primary.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/tova/public.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/tova/road.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/en/tova/value.html` | 요청 실패: net::ERR_ABORTED www.google-analytics.com/g/collect |
| `/assets/img/dt_use.html` | 이동: sso.hmac.kr/ko/error (SSO redirect_uri 등록 불일치) / HTTP: 404 /assets/assets/img/dt/use_end_obj3.json; 401 sso.hmac.kr/api/v1/user/me |

## 스크롤·모바일 검증에서 발견한 증상

| 경로 / 너비 | 증상 |
|---|---|
| `/ko/tova/public.html` / 1365 | 가로 넘침: 1567px / viewport 1365px |
| `/ko/kngil/value.html` / 1365 | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg |
| `/ko/kngil/primary.html` / 1365 | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg |
| `/ko/tova/public.html` / 390 | 가로 넘침: 983px / viewport 390px |
| `/ko/kngil/value.html` / 390 | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg |
| `/ko/kngil/primary.html` / 390 | HTTP: 404 /ko/kngil/img/video/kngil_guide_poster.jpg |

## 추가 진단 및 정적 참조 검사의 해석

TOVA 가로 넘침은 원본 스냅샷과 현재 소스를 별도 로컬 HTTP 서버에서 비교했다. 양쪽 모두 SVG object 6개가 정상 로드되고 같은 너비였다(`tova-overflow-check.json`). 요청 가로채기 방식의 초기 진단은 object 로드를 막았으므로 판정에서 제외했다.

`inventory.json`은 모든 HTML/CSS/JS의 로컬·외부 참조 후보를 보존한다. CKEditor 스킨, 사용하지 않는 CSS, JavaScript 내부 문자열, 과거 백업 경로도 포함하므로 `exists=false` 건수를 실제 사용자 화면의 404 건수로 해석하면 안 된다. 실제 요청 여부는 위 브라우저 결과를 우선한다.

## 다음 속도 개선 후보

- 여전히 load가 오래 걸리는 페이지의 화면 아래 대형 이미지를 섹션별로 측정해 지연 로딩 확대 검토. 현재 GSAP가 이미지 높이에 의존할 수 있어 레이아웃 검증을 동반해야 한다.
- 외부 CDN 스크립트와 광고·분석 요청의 지연은 실제 운영 환경에서 따로 측정.
- 데스크톱/모바일용 화면 크기에 맞는 추가 이미지 변형은 고해상도 모니터 시각 검수 후 적용.
- SSO가 필요한 페이지는 인증된 테스트 계정·운영과 같은 도메인 조건에서 별도 검증.
