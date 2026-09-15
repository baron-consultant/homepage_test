# 이미지 21개 404 원인 조사

## main push 이후 재확인

`41ce755` push 이후 `https://baroncs.co.kr/ko/index.html`에서 index-web.mp4 참조, `/ko/tova/public.html`에서 public_process_01.perf.svg 참조, `/ko/tova/css/style.css`에서 새 .perf. 참조 17건을 확인했다. 코드 반영은 확인됐지만 해당 21개 이미지의 GET 응답은 여전히 404였다.

이 결과는 R2 업로드 실패 자체를 증명하지 않는다. 업로드된 객체의 전체 키와 실제 제공 도메인을 대조해야 업로드 경로 불일치 또는 제공 경로 문제를 확정할 수 있다. 원시 기록은 `post-push-missing-assets.json`, `post-push-public-source.json`이다.

## 결론

새 HTML/CSS가 요청하는 최적화 파일 경로에서 서버가 HTTP 404 / Not Found를 반환한다. 21개 모두 대응하는 기존 원본 URL은 200이고, 새 파일의 로컬 URL도 200이다. 서버가 새 파일명에 해당하는 리소스를 제공하지 못하는 상태다.

예: `ko/tova/public.html:196`의 `./img/public_process_01.perf.svg`는 `/ko/tova/img/public_process_01.perf.svg`로 해석된다. 기존 `/ko/tova/img/public_process_01.svg`는 다른 객체 키이므로 새 파일을 대신 제공하지 않는다.

## 검사 근거

- 고유 쿼리를 붙인 GET: 새 파일 21개 모두 404, 대응 원본 21개 모두 200.
- 같은 새 파일 21개를 로컬 baron.test에서 요청하면 모두 200.
- 기존 SVG 18개는 image/svg+xml로 정상 제공된다. 다른 .perf.webp도 200이다. SVG 전체 차단이나 모든 최적화 파일명의 차단을 뒷받침하는 증거는 없다.
- 응답은 이미지 디코딩 오류가 아니라 HTTP 404 / text/plain / Not Found다.
- 상대경로를 HTML/CSS 위치 기준으로 계산한 결과가 검사한 운영 URL과 일치한다.
- 현재 Worker 소스는 SVG/WebP를 지원한다. URL의 선행 /를 제거한 키로 SITE_BUCKET.get을 호출하고, 객체를 찾지 못하면 404를 반환한다. 운영 Worker 배포본을 원격으로 읽어 비교한 것은 아니다.
- 중첩 폴더가 빠진 몇 가지 대체 경로도 404였다. 모든 가능한 업로드 위치를 탐색한 것은 아니다.

## 아직 확정할 수 없는 부분

R2 객체 목록과 업로드 로그는 조회하지 않았다. 따라서 업로드 누락, 다른 폴더 업로드, 파일명 변경 중 정확히 어느 과정에서 발생했는지는 확정할 수 없다. 변수·엔드포인트·버킷은 사용자가 정상으로 확인한 상태를 기준으로 한다.

누락 분포는 새 SVG 18개 전체와 WebP 3개다. 업로드 선택에서 SVG가 빠졌거나 일부 파일·하위 폴더가 누락되었을 가능성이 있으나, 이는 분포에 근거한 추정이다.

## 필요한 객체 키와 참조 위치

키는 버킷 루트 기준이며 앞에 /를 붙이지 않는다. ZIP 이름의 상위 폴더를 추가하면 요청 경로와 달라진다.

| 객체 키 | 참조 위치 |
|---|---|
| `en/egbim/img/com_img/eng/comp_1.perf.webp` | `en/egbim/interface.html:134` |
| `en/egbim/img/find_img_01_01.perf.svg` | `en/egbim/floorplan.html:130` |
| `en/egbim/img/interface_img_03.perf.svg` | `en/egbim/interface.html:115` |
| `en/tova/img/pub_01_01.perf.svg` | `en/tova/primary.html:695` |
| `en/tova/img/pub_03_01.perf.svg` | `en/tova/primary.html:744` |
| `en/tova/img/public_process_01.perf.svg` | `en/tova/public.html:192` |
| `en/tova/img/public_process_02.perf.svg` | `en/tova/public.html:209` |
| `en/tova/img/public_process_03.perf.svg` | `en/tova/public.html:224` |
| `en/tova/img/road_proportionality_fig1.perf.svg` | `en/tova/road.html:706` |
| `ko/egbim/img/com_img/comp_1.perf.webp` | `ko/egbim/interface.html:120` |
| `ko/egbim/img/find_img_01_01.perf.svg` | `ko/egbim/floorplan.html:105` |
| `ko/kngil/img/bg_pop.perf.webp` | `ko/kngil/css/common.css:2888`, `ko/kngil/css/common.css:3274` |
| `ko/tova/img/primary_02_04.perf.svg` | `ko/tova/primary.html:142` |
| `ko/tova/img/pub_01_01.perf.svg` | `ko/tova/primary.html:206` |
| `ko/tova/img/pub_03_01.perf.svg` | `ko/tova/primary.html:254` |
| `ko/tova/img/public_process_01.perf.svg` | `ko/tova/public.html:196` |
| `ko/tova/img/public_process_02.perf.svg` | `ko/tova/public.html:212` |
| `ko/tova/img/public_process_03.perf.svg` | `ko/tova/public.html:227` |
| `ko/tova/img/road_proportionality_fig1.perf.svg` | `ko/tova/road.html:220` |
| `ko/tova/img/zone_01_01.perf.svg` | `ko/tova/primary.html:309` |
| `ko/tova/img/zone_01_02.perf.svg` | `ko/tova/primary.html:314` |

[21개 경로 목록](missing-upload-assets.txt). 폴더 구조를 유지한 압축본: `artifacts/performance/latest-20260915/missing-upload-assets.zip`.

원시 기록: `missing-asset-diagnosis.json`, `missing-asset-source-references.json`, `missing-asset-local-check.json`. 경로 변경·업로드·배포는 실행하지 않았다.
