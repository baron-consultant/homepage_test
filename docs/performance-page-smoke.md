# 전체 HTML 페이지 브라우저 점검

> `90c1cc9` 기반 성능 개선 작업 당시의 검사 기록입니다. 이후 `homepage_test/main`의 `cebb14b`를 반영했으므로 아래 오류를 최신 코드에서도 재현되는 문제로 단정하지 마세요.

개선 후 147개 경로를 실제 Playwright/Edge로 각각 탐색했습니다. include HTML 조각과 CKEditor 샘플은 제외하며 백업 HTML과 폰트 데모는 포함합니다.

JS 오류가 관측된 경로 11개, HTTP 400 이상 응답이 관측된 경로 13개, 탐색 시간초과 0개입니다. 항목 간 경로는 중복될 수 있습니다.

성능 비교 실험과 별도입니다. 네트워크/CPU 감속 없이 새 컨텍스트·캐시 비활성화로 실행했습니다. 탐색 시작부터 최소 2초 관측하며 DOMContentLoaded를 최대 15초 기다립니다. load가 관측되지 않은 것은 0ms 로딩이 아닙니다.

초기 탐색 검사만 수행합니다. 폼 제출·다운로드·모든 버튼/스크롤은 시험하지 않았습니다. 아래 오류는 이 로컬 복사본에서 관측한 결과이며 운영 환경과 다를 수 있습니다. 기존 오류와 이번 변경의 회귀 여부는 주요 페이지 전후 비교 및 별도 메뉴 테스트를 함께 확인해야 합니다.

| 페이지 | DCL ms | load ms | JS 오류 | HTTP ≥400 | 요청 실패 | 탐색 시간초과 |
|---|---:|---:|---:|---:|---:|---|
| `/callback.html` | 114.1 | 114.3 | 0 | 0 | 0 | — |
| `/index.html` | 124.0 | 211.3 | 0 | 0 | 0 | — |
| `/callback/index.html` | 16.0 | 16.4 | 0 | 0 | 0 | — |
| `/en/br_future.html` | 72.4 | 72.5 | 0 | 0 | 0 | — |
| `/en/br_future_bak_250610.html` | 197.3 | 434.0 | 0 | 0 | 4 | — |
| `/en/br_future_bak_251103.html` | 320.4 | 723.8 | 0 | 0 | 0 | — |
| `/en/br_tech.html` | 104.6 | 104.6 | 0 | 0 | 0 | — |
| `/en/br_tech_bak_251103.html` | 306.6 | 314.9 | 0 | 0 | 0 | — |
| `/en/br_value.html` | 86.6 | 86.7 | 0 | 0 | 0 | — |
| `/en/dt_explain.html` | 121.3 | 121.6 | 0 | 0 | 0 | — |
| `/en/dt_sw.html` | 79.2 | 79.3 | 0 | 0 | 0 | — |
| `/en/dt_use.html` | 89.0 | 89.1 | 0 | 0 | 0 | — |
| `/en/dx.html` | 91.7 | 91.8 | 0 | 0 | 0 | — |
| `/en/dx_250612.html` | 317.5 | 미관측 | 1 | 6 | 0 | — |
| `/en/faq.html` | 135.1 | 155.8 | 0 | 0 | 0 | — |
| `/en/hosting_index1.html` | 21.6 | 53.0 | 0 | 2 | 0 | — |
| `/en/index.html` | 86.8 | 153.5 | 0 | 0 | 0 | — |
| `/en/pr_brochure.html` | 141.7 | 145.2 | 0 | 0 | 0 | — |
| `/en/pr_ci.html` | 287.5 | 369.5 | 0 | 0 | 0 | — |
| `/en/pr_news.html` | 195.3 | 196.6 | 0 | 0 | 0 | — |
| `/en/pr_news_view_251127.html` | 154.4 | 155.1 | 0 | 0 | 0 | — |
| `/en/pr_news_view_260121.html` | 120.8 | 133.1 | 0 | 0 | 0 | — |
| `/en/pr_news_view_260519.html` | 128.7 | 129.4 | 0 | 0 | 0 | — |
| `/en/pr_news_view_260527.html` | 138.1 | 138.5 | 0 | 0 | 0 | — |
| `/en/sv_bigroom.html` | 103.5 | 103.6 | 0 | 0 | 0 | — |
| `/en/sv_solution.html` | 81.4 | 81.4 | 0 | 0 | 0 | — |
| `/en/sv_solution_construction.html` | 76.4 | 76.5 | 0 | 0 | 0 | — |
| `/en/sv_solution_operation.html` | 108.3 | 108.4 | 0 | 0 | 0 | — |
| `/en/sv_sw.html` | 371.6 | 372.6 | 0 | 0 | 0 | — |
| `/en/sv_sw_egbim.html` | 326.0 | 335.5 | 0 | 0 | 0 | — |
| `/en/sv_sw_gaia.html` | 340.3 | 352.2 | 0 | 0 | 0 | — |
| `/en/sv_sw_ipipes.html` | 389.9 | 407.3 | 0 | 0 | 0 | — |
| `/en/sv_sw_kngil.html` | 352.1 | 394.9 | 0 | 0 | 0 | — |
| `/en/sv_sw_pq_program.html` | 328.0 | 428.5 | 0 | 0 | 0 | — |
| `/en/video_ex.html` | 88.1 | 1369.0 | 0 | 0 | 2 | — |
| `/ko/br_future.html` | 79.0 | 79.2 | 0 | 0 | 0 | — |
| `/ko/br_future_bak_250610.html` | 238.5 | 374.2 | 0 | 0 | 2 | — |
| `/ko/br_future_bak_251103.html` | 239.8 | 376.8 | 0 | 0 | 0 | — |
| `/ko/br_tech.html` | 80.1 | 80.6 | 0 | 0 | 0 | — |
| `/ko/br_tech_bak_251103.html` | 279.8 | 290.3 | 0 | 0 | 0 | — |
| `/ko/br_value.html` | 107.7 | 108.0 | 0 | 0 | 0 | — |
| `/ko/dt_explain.html` | 98.0 | 98.1 | 0 | 0 | 0 | — |
| `/ko/dt_sw.html` | 84.7 | 84.9 | 0 | 0 | 0 | — |
| `/ko/dt_use.html` | 78.3 | 78.4 | 0 | 0 | 0 | — |
| `/ko/dx.html` | 80.4 | 80.6 | 0 | 0 | 0 | — |
| `/ko/dx_250612.html` | 460.0 | 미관측 | 1 | 6 | 1 | — |
| `/ko/faq.html` | 126.5 | 145.3 | 0 | 0 | 0 | — |
| `/ko/hosting_index1.html` | 17.9 | 49.6 | 0 | 2 | 0 | — |
| `/ko/index.html` | 93.4 | 159.4 | 0 | 0 | 0 | — |
| `/ko/pr_brochure.html` | 157.3 | 158.1 | 0 | 0 | 0 | — |
| `/ko/pr_ci.html` | 347.4 | 412.5 | 0 | 0 | 0 | — |
| `/ko/pr_news.html` | 183.1 | 183.4 | 0 | 0 | 0 | — |
| `/ko/pr_news_view_251127.html` | 164.8 | 191.2 | 0 | 0 | 0 | — |
| `/ko/pr_news_view_260121.html` | 159.5 | 160.0 | 0 | 0 | 0 | — |
| `/ko/pr_news_view_260519.html` | 171.0 | 208.8 | 0 | 0 | 0 | — |
| `/ko/pr_news_view_260527.html` | 163.4 | 164.0 | 0 | 0 | 0 | — |
| `/ko/sv_bigroom.html` | 77.9 | 78.0 | 0 | 0 | 0 | — |
| `/ko/sv_solution copy.html` | 16.4 | 16.7 | 0 | 0 | 0 | — |
| `/ko/sv_solution.html` | 130.3 | 130.5 | 0 | 0 | 0 | — |
| `/ko/sv_solution_construction.html` | 87.3 | 87.4 | 0 | 0 | 0 | — |
| `/ko/sv_solution_operation.html` | 93.6 | 93.8 | 0 | 0 | 0 | — |
| `/ko/sv_sw.html` | 373.9 | 374.1 | 0 | 0 | 0 | — |
| `/ko/sv_sw_egbim.html` | 1029.3 | 1172.2 | 0 | 0 | 0 | — |
| `/ko/sv_sw_gaia.html` | 446.8 | 446.9 | 0 | 0 | 0 | — |
| `/ko/sv_sw_ipipes.html` | 378.0 | 383.0 | 0 | 0 | 0 | — |
| `/ko/sv_sw_kngil.html` | 354.9 | 359.3 | 0 | 0 | 0 | — |
| `/ko/sv_sw_pq_program.html` | 321.1 | 365.1 | 3 | 0 | 5 | — |
| `/ko/video_ex.html` | 138.1 | 1301.7 | 0 | 0 | 2 | — |
| `/portfolio/compilation.html` | 445.5 | 미관측 | 0 | 0 | 0 | — |
| `/portfolio/ux.html` | 208.5 | 1898.6 | 0 | 0 | 0 | — |
| `/portfolio/video.html` | 204.8 | 미관측 | 0 | 0 | 0 | — |
| `/recruit/br_recruit.html` | 318.9 | 339.8 | 0 | 0 | 0 | — |
| `/recruit/recruit_apply.html` | 141.1 | 152.4 | 1 | 0 | 0 | — |
| `/recruit/recruit_faq.html` | 201.5 | 202.0 | 0 | 0 | 0 | — |
| `/recruit/recruit_view.html` | 178.8 | 179.2 | 1 | 0 | 0 | — |
| `/ko/egbim/buy.html` | 216.9 | 347.3 | 0 | 1 | 1 | — |
| `/ko/egbim/floorplan.html` | 320.4 | 401.1 | 0 | 0 | 0 | — |
| `/ko/egbim/forbim.html` | 259.2 | 319.2 | 1 | 0 | 0 | — |
| `/ko/egbim/interface.html` | 344.7 | 420.9 | 0 | 1 | 0 | — |
| `/ko/egbim/primary.html` | 260.1 | 277.5 | 0 | 0 | 0 | — |
| `/ko/egbim/value.html` | 268.6 | 353.6 | 0 | 0 | 0 | — |
| `/ko/gaia/buy.html` | 174.3 | 434.2 | 0 | 0 | 1 | — |
| `/ko/gaia/further.html` | 291.7 | 377.0 | 0 | 0 | 1 | — |
| `/ko/gaia/index.html` | 171.0 | 392.9 | 1 | 0 | 2 | — |
| `/ko/gaia/primary.html` | 386.4 | 471.6 | 0 | 0 | 1 | — |
| `/ko/gaia/results.html` | 237.2 | 392.0 | 0 | 0 | 1 | — |
| `/ko/gaia/value.html` | 360.6 | 525.6 | 0 | 0 | 1 | — |
| `/ko/tova/buy.html` | 183.0 | 432.3 | 0 | 0 | 2 | — |
| `/ko/tova/index.html` | 270.7 | 391.3 | 1 | 0 | 5 | — |
| `/ko/tova/primary.html` | 497.6 | 941.4 | 0 | 0 | 1 | — |
| `/ko/tova/public.html` | 277.0 | 825.6 | 0 | 0 | 1 | — |
| `/ko/tova/road.html` | 346.4 | 581.8 | 0 | 0 | 1 | — |
| `/ko/tova/value.html` | 312.1 | 456.9 | 0 | 0 | 1 | — |
| `/ko/gaia/font/NotoKR-Black/notokr-black-demo.html` | 718.0 | 719.4 | 0 | 0 | 0 | — |
| `/ko/gaia/font/NotoKR-Bold/notokr-bold-demo.html` | 845.9 | 847.3 | 0 | 0 | 0 | — |
| `/ko/gaia/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 834.0 | 835.3 | 0 | 0 | 0 | — |
| `/ko/gaia/font/NotoKR-Light/notokr-light-demo.html` | 782.3 | 786.5 | 0 | 0 | 0 | — |
| `/ko/gaia/font/NotoKR-Medium/notokr-medium-demo.html` | 798.3 | 800.8 | 0 | 0 | 0 | — |
| `/ko/gaia/font/NotoKR-Regular/notokr-regular-demo.html` | 818.2 | 819.5 | 0 | 0 | 0 | — |
| `/ko/gaia/font/NotoKR-Thin/notokr-thin-demo.html` | 740.5 | 742.3 | 0 | 0 | 0 | — |
| `/ko/egbim/font/NotoKR-Black/notokr-black-demo.html` | 712.2 | 716.1 | 0 | 0 | 0 | — |
| `/ko/egbim/font/NotoKR-Bold/notokr-bold-demo.html` | 745.2 | 746.5 | 0 | 0 | 0 | — |
| `/ko/egbim/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 841.6 | 843.1 | 0 | 0 | 0 | — |
| `/ko/egbim/font/NotoKR-Light/notokr-light-demo.html` | 712.2 | 713.7 | 0 | 0 | 0 | — |
| `/ko/egbim/font/NotoKR-Medium/notokr-medium-demo.html` | 751.7 | 754.4 | 0 | 0 | 0 | — |
| `/ko/egbim/font/NotoKR-Regular/notokr-regular-demo.html` | 767.5 | 768.9 | 0 | 0 | 0 | — |
| `/ko/egbim/font/NotoKR-Thin/notokr-thin-demo.html` | 848.6 | 850.0 | 0 | 0 | 0 | — |
| `/en/egbim/buy.html` | 199.3 | 501.6 | 0 | 0 | 1 | — |
| `/en/egbim/floorplan.html` | 232.9 | 549.5 | 0 | 0 | 1 | — |
| `/en/egbim/forbim.html` | 240.2 | 509.1 | 1 | 0 | 1 | — |
| `/en/egbim/interface.html` | 275.2 | 585.6 | 0 | 0 | 1 | — |
| `/en/egbim/primary.html` | 304.6 | 501.7 | 0 | 0 | 1 | — |
| `/en/egbim/value.html` | 171.7 | 492.4 | 0 | 0 | 1 | — |
| `/en/gaia/buy.html` | 163.7 | 408.6 | 0 | 0 | 1 | — |
| `/en/gaia/further.html` | 301.2 | 660.7 | 0 | 0 | 1 | — |
| `/en/gaia/index.html` | 151.3 | 438.3 | 1 | 0 | 1 | — |
| `/en/gaia/primary.html` | 242.7 | 734.0 | 0 | 0 | 1 | — |
| `/en/gaia/results.html` | 197.9 | 494.1 | 0 | 0 | 1 | — |
| `/en/gaia/value.html` | 289.0 | 480.4 | 0 | 0 | 1 | — |
| `/en/tova/buy.html` | 207.8 | 444.5 | 0 | 1 | 2 | — |
| `/en/tova/index.html` | 155.5 | 359.6 | 1 | 7 | 7 | — |
| `/en/tova/primary.html` | 231.7 | 731.8 | 0 | 1 | 1 | — |
| `/en/tova/public.html` | 296.2 | 909.1 | 0 | 1 | 1 | — |
| `/en/tova/road.html` | 353.8 | 592.7 | 0 | 1 | 1 | — |
| `/en/tova/value.html` | 204.5 | 523.0 | 0 | 1 | 1 | — |
| `/en/gaia/font/NotoKR-Black/notokr-black-demo.html` | 804.3 | 806.4 | 0 | 0 | 0 | — |
| `/en/gaia/font/NotoKR-Bold/notokr-bold-demo.html` | 834.5 | 835.8 | 0 | 0 | 0 | — |
| `/en/gaia/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 786.0 | 787.6 | 0 | 0 | 0 | — |
| `/en/gaia/font/NotoKR-Light/notokr-light-demo.html` | 818.6 | 823.7 | 0 | 0 | 0 | — |
| `/en/gaia/font/NotoKR-Medium/notokr-medium-demo.html` | 889.1 | 890.9 | 0 | 0 | 0 | — |
| `/en/gaia/font/NotoKR-Regular/notokr-regular-demo.html` | 810.1 | 811.7 | 0 | 0 | 0 | — |
| `/en/gaia/font/NotoKR-Thin/notokr-thin-demo.html` | 855.5 | 856.8 | 0 | 0 | 0 | — |
| `/en/egbim/font/NotoKR-Black/notokr-black-demo.html` | 856.4 | 857.8 | 0 | 0 | 0 | — |
| `/en/egbim/font/NotoKR-Bold/notokr-bold-demo.html` | 803.3 | 804.8 | 0 | 0 | 0 | — |
| `/en/egbim/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 723.0 | 725.2 | 0 | 0 | 0 | — |
| `/en/egbim/font/NotoKR-Light/notokr-light-demo.html` | 815.7 | 817.1 | 0 | 0 | 0 | — |
| `/en/egbim/font/NotoKR-Medium/notokr-medium-demo.html` | 806.1 | 807.4 | 0 | 0 | 0 | — |
| `/en/egbim/font/NotoKR-Regular/notokr-regular-demo.html` | 811.1 | 813.0 | 0 | 0 | 0 | — |
| `/en/egbim/font/NotoKR-Thin/notokr-thin-demo.html` | 768.5 | 769.8 | 0 | 0 | 0 | — |
| `/assets/img/dt_use.html` | 403.9 | 583.3 | 0 | 1 | 0 | — |
| `/assets/font/NotoKR-Black/notokr-black-demo.html` | 901.8 | 903.0 | 0 | 0 | 0 | — |
| `/assets/font/NotoKR-Bold/notokr-bold-demo.html` | 872.9 | 874.5 | 0 | 0 | 0 | — |
| `/assets/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 856.1 | 857.5 | 0 | 0 | 0 | — |
| `/assets/font/NotoKR-Light/notokr-light-demo.html` | 719.9 | 721.2 | 0 | 0 | 0 | — |
| `/assets/font/NotoKR-Medium/notokr-medium-demo.html` | 1146.9 | 1149.3 | 0 | 0 | 0 | — |
| `/assets/font/NotoKR-Regular/notokr-regular-demo.html` | 1112.9 | 1114.5 | 0 | 0 | 0 | — |
| `/assets/font/NotoKR-Thin/notokr-thin-demo.html` | 914.5 | 916.1 | 0 | 0 | 0 | — |

## 관측 오류 상세

ERR_ABORTED는 영상 소스 교체·페이지 이동·분석 beacon 중단·테스트 컨텍스트 종료 등에서도 발생하므로 모두 사용자에게 보이는 장애로 단정하지 않습니다.

### /en/br_future_bak_250610.html

- net::ERR_ABORTED: /assets/img/br/future_intro_bg.mp4

### /en/dx_250612.html

- Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared
- HTTP 404: /assets/css/%3Cpath-to-image%3E
- HTTP 404: img.youtube.com/vi/jnw_Ji8ojow/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/TWUD65ivJiY/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/bs0tqiY8H4E/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/Q2SWEAv5h2g/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/ZNKk3W5Wy5o/hqdefault.jpg

### /en/hosting_index1.html

- HTTP 404: /en/warning.png
- HTTP 404: /en/traffic_image.jpg

### /en/video_ex.html

- net::ERR_ABORTED: www.youtube.com/api/stats/qoe

### /ko/br_future_bak_250610.html

- net::ERR_ABORTED: /assets/img/br/future_intro_bg.mp4

### /ko/dx_250612.html

- Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared
- HTTP 404: /assets/css/%3Cpath-to-image%3E
- HTTP 404: img.youtube.com/vi/ZNKk3W5Wy5o/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/TWUD65ivJiY/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/Q2SWEAv5h2g/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/jnw_Ji8ojow/hqdefault.jpg
- HTTP 404: img.youtube.com/vi/bs0tqiY8H4E/hqdefault.jpg
- net::ERR_ABORTED: ogs.google.com/widget/callout

### /ko/hosting_index1.html

- HTTP 404: /ko/traffic_image.jpg
- HTTP 404: /ko/warning.png

### /ko/sv_sw_pq_program.html

- jQuery is not defined
- $ is not defined
- net::ERR_CONNECTION_REFUSED: /assets/js/lib/lenis.min.js
- net::ERR_CONNECTION_REFUSED: /assets/css/layout.css
- net::ERR_CONNECTION_REFUSED: /assets/js/lib/jquery-3.6.1.min.js
- net::ERR_CONNECTION_REFUSED: /assets/js/lib/gsap.min.js
- net::ERR_CONNECTION_REFUSED: /assets/js/lib/scrolltrigger.min.js

### /ko/video_ex.html

- net::ERR_ABORTED: www.youtube.com/api/stats/qoe

### /recruit/recruit_apply.html

- Invalid or unexpected token

### /recruit/recruit_view.html

- Failed to execute 'appendChild' on 'Node': Identifier 'urlParams' has already been declared

### /ko/egbim/buy.html

- HTTP 404: /ko/egbim/js/buy.js
- net::ERR_ABORTED: /ko/egbim/js/buy.js

### /ko/egbim/forbim.html

- Cannot read properties of null (reading 'style')

### /ko/egbim/interface.html

- HTTP 404: /ko/img/com_img/comp_1.png

### /ko/gaia/buy.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/gaia/further.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/gaia/index.html

- The play() request was interrupted by a call to pause().
- net::ERR_ABORTED: /ko/gaia/img/main_1.mp4
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/gaia/primary.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/gaia/results.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/gaia/value.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/tova/buy.html

- net::ERR_ABORTED: /ko/tova/img/buy_vdieo.mp4
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/tova/index.html

- The play() request was interrupted by a call to pause().
- net::ERR_ABORTED: /ko/tova/img/main_01.mp4
- net::ERR_CONNECTION_REFUSED: /ko/tova/img/main_1.mp4
- net::ERR_CONNECTION_REFUSED: /_include/footer.html
- net::ERR_CONNECTION_REFUSED: /_include/nav.html
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/tova/primary.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/tova/public.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/tova/road.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /ko/tova/value.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/egbim/buy.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/egbim/floorplan.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/egbim/forbim.html

- Cannot read properties of null (reading 'style')
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/egbim/interface.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/egbim/primary.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/egbim/value.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/gaia/buy.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/gaia/further.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/gaia/index.html

- The play() request was interrupted by a call to pause().
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/gaia/primary.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/gaia/results.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/gaia/value.html

- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/tova/buy.html

- HTTP 404: /en/tova/some_api_endpoint
- net::ERR_ABORTED: /en/tova/img/buy_vdieo.mp4
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/tova/index.html

- Failed to load because no supported source was found.
- HTTP 404: /en/tova/theme/basic/skin/qa/basic/style.css
- HTTP 404: /en/tova/img/main_1_T.mp4
- HTTP 404: /en/tova/img/main_1_O.mp4
- HTTP 404: /en/tova/img/main_1_V.mp4
- HTTP 404: /en/tova/img/main_1_A.mp4
- HTTP 404: /en/tova/img/main_1.mp4
- HTTP 404: /en/tova/some_api_endpoint
- net::ERR_ABORTED: /en/tova/theme/basic/skin/qa/basic/style.css
- net::ERR_ABORTED: /en/tova/img/main_1_T.mp4
- net::ERR_ABORTED: /en/tova/img/main_1_O.mp4
- net::ERR_ABORTED: /en/tova/img/main_1_V.mp4
- net::ERR_ABORTED: /en/tova/img/main_1_A.mp4
- net::ERR_ABORTED: /en/tova/img/main_01.mp4
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/tova/primary.html

- HTTP 404: /en/tova/some_api_endpoint
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/tova/public.html

- HTTP 404: /en/tova/some_api_endpoint
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/tova/road.html

- HTTP 404: /en/tova/some_api_endpoint
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /en/tova/value.html

- HTTP 404: /en/tova/some_api_endpoint
- net::ERR_ABORTED: www.google-analytics.com/g/collect

### /assets/img/dt_use.html

- HTTP 404: /assets/assets/img/dt/use_end_obj3.json

## 로컬 연결 실패 경로 재검증

최초 순회에서 일부 로컬 리소스에 ERR_CONNECTION_REFUSED가 관측되어 테스트 서버의 연결 대기열을 128로 늘린 뒤 해당 경로만 재검증했습니다. 최초 기록은 위에 보존했으며 아래는 별도 실행 결과입니다. 전후 성능 48회 측정에서는 이 변경 이전의 동일 서버 설정을 사용했습니다.

| 경로 | JS 오류 | HTTP ≥400 | 요청 실패 |
|---|---:|---:|---:|
| `/ko/sv_sw_pq_program.html` | 0 | 0 | 0 |
| `/ko/tova/index.html` | 1 | 1 | 2 |

## 메뉴·미디어 기능 확인

| 경로 | 화면 | 메뉴 열기/닫기 | 영상/사진 | JS 오류 |
|---|---|---|---|---:|
| `/ko/index.html` | 1365×768 | pass | pass | 0 |
| `/en/index.html` | 1365×768 | pass | pass | 0 |
| `/recruit/br_recruit.html` | 1365×768 | pass | pass | 0 |
| `/ko/index.html` | 390×844 | pass | pass | 0 |
| `/en/index.html` | 390×844 | pass | pass | 0 |
| `/recruit/br_recruit.html` | 390×844 | pass | pass | 0 |

채용 페이지는 common.js 요청이 한 번인지도 검증했습니다. 국문·영문 메인은 실제 재생 시간이 1초 이상 증가하는지 확인했습니다.
