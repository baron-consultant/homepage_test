# 이미지 참조 경로 검사

## 결론

새 이미지의 정적 참조 513건은 모두 현재 위치 기준 상대경로다. 전체 기존 소스에는 루트 기준 경로 후보 411건과 외부 URL 후보 45건도 있다. 동적 문자열 27건은 실행 결과에 따라 달라질 수 있다.

이미지 참조를 수정하지 않고 현재 HTML·CSS·JavaScript·SVG를 검사했다. 라이브러리·데모·백업 파일도 포함한다. scripts/docs/artifacts 및 도구 설치 폴더는 제외했다.

검사 파일 1,987개. 정적 참조와 JS 문자열 후보를 파일·행·URL 기준으로 중복 제거했다. 주석과 일부 동적 문자열은 정적 분석 한계가 있어 실제 요청 여부와 구분해야 한다.

| 분류 | 전체 참조 후보 | 새로 생성한 이미지 참조 |
|---|---:|---:|
| relative | 3790 | 513 |
| root-relative | 411 | 0 |
| external | 45 | 0 |
| embedded | 137 | 0 |
| fragment | 34 | 0 |
| dynamic | 27 | 0 |
| other-scheme | 0 | 0 |

- `relative`: `img/a.webp`, `../assets/img/a.svg`처럼 현재 기준 URL에서 해석되는 경로.
- `root-relative`: `/assets/img/a.svg`처럼 현재 도메인의 루트 기준 경로. 도메인을 고정한 절대 URL은 아니지만 현재 폴더 기준 상대경로와 다르다.
- `external`: https:// 또는 //로 시작하는 도메인 지정 URL.
- CSS 파일의 url()은 CSS 파일 위치, HTML src는 문서 위치를 기준으로 해석된다. JS 문자열은 실제 대입 대상·실행 문서에 따라 기준이 달라진다.
- SVG 내부 data:image는 파일 경로가 아닌 내장 데이터다. 동적 연결·API가 반환하는 URL은 이 검사만으로 모두 확정할 수 없다.

## 현재 폴더 기준 상대경로가 아닌 참조

아래는 root-relative/external/dynamic/other-scheme 후보의 전체 목록이다. 라이브러리 또는 사용하지 않는 파일의 문자열도 포함하며, 실제 화면 요청임을 뜻하지 않는다.

| 파일:행 | 분류 | 참조 |
|---|---|---|
| `en/br_future.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/br_future_bak_250610.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/br_future_bak_250610.html:57` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `en/br_future_bak_250610.html:108` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `en/br_future_bak_250610.html:114` | root-relative | `/assets/img/br/future_sub2_process_bg.png` |
| `en/br_future_bak_250610.html:115` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `en/br_future_bak_250610.html:128` | root-relative | `/assets/img/br/future_sub2_product_bg.png` |
| `en/br_future_bak_250610.html:129` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `en/br_future_bak_250610.html:176` | root-relative | `/assets/img/br/future_sub3_easy.jpg` |
| `en/br_future_bak_250610.html:186` | root-relative | `/assets/img/br/future_sub3_convenient.jpg` |
| `en/br_future_bak_250610.html:196` | root-relative | `/assets/img/br/future_sub3_quality.jpg` |
| `en/br_future_bak_250610.html:206` | root-relative | `/assets/img/br/future_sub3_cost.jpg` |
| `en/br_future_bak_250610.html:216` | root-relative | `/assets/img/br/future_sub3_fast.jpg` |
| `en/br_future_bak_250610.html:111` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `en/br_future_bak_250610.html:117` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `en/br_future_bak_250610.html:131` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `en/br_future_bak_251103.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/br_future_bak_251103.html:62` | root-relative | `/assets/img/br/future_sub1_m_bg.png` |
| `en/br_future_bak_251103.html:66` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `en/br_future_bak_251103.html:70` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `en/br_future_bak_251103.html:109` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `en/br_future_bak_251103.html:116` | root-relative | `/assets/img/br/future_sub2_process_bg.png` |
| `en/br_future_bak_251103.html:117` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `en/br_future_bak_251103.html:135` | root-relative | `/assets/img/br/future_sub2_product_bg.png` |
| `en/br_future_bak_251103.html:136` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `en/br_future_bak_251103.html:215` | root-relative | `/assets/img/br/future_sub3_easy.jpg` |
| `en/br_future_bak_251103.html:225` | root-relative | `/assets/img/br/future_sub3_convenient.jpg` |
| `en/br_future_bak_251103.html:235` | root-relative | `/assets/img/br/future_sub3_quality.jpg` |
| `en/br_future_bak_251103.html:245` | root-relative | `/assets/img/br/future_sub3_cost.jpg` |
| `en/br_future_bak_251103.html:255` | root-relative | `/assets/img/br/future_sub3_fast.jpg` |
| `en/br_future_bak_251103.html:64` | root-relative | `/assets/img/br/future_sub1_m_bg.png` |
| `en/br_future_bak_251103.html:68` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `en/br_future_bak_251103.html:112` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `en/br_future_bak_251103.html:119` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `en/br_future_bak_251103.html:138` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `en/br_tech.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/br_tech_bak_251103.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/br_tech_bak_251103.html:75` | root-relative | `/assets/img/br/tech_sub1_sw_bg.jpg` |
| `en/br_tech_bak_251103.html:82` | root-relative | `/assets/img/br/tech_sub1_hw_bg.jpg` |
| `en/br_tech_bak_251103.html:146` | root-relative | `/assets/img/br/tech_sub3_step1_1.jpg` |
| `en/br_tech_bak_251103.html:151` | root-relative | `/assets/img/br/tech_sub3_step1_2.jpg` |
| `en/br_tech_bak_251103.html:156` | root-relative | `/assets/img/br/tech_sub3_step1_3.jpg` |
| `en/br_tech_bak_251103.html:161` | root-relative | `/assets/img/br/tech_sub3_step1_4.jpg` |
| `en/br_tech_bak_251103.html:166` | root-relative | `/assets/img/br/tech_sub3_step1_5.jpg` |
| `en/br_tech_bak_251103.html:182` | root-relative | `/assets/img/br/tech_sub3_step2_1.jpg` |
| `en/br_tech_bak_251103.html:187` | root-relative | `/assets/img/br/tech_sub3_step2_2.jpg` |
| `en/br_tech_bak_251103.html:192` | root-relative | `/assets/img/br/tech_sub3_step2_3.jpg` |
| `en/br_tech_bak_251103.html:197` | root-relative | `/assets/img/br/tech_sub3_step2_4.jpg` |
| `en/br_tech_bak_251103.html:202` | root-relative | `/assets/img/br/tech_sub3_step2_5.jpg` |
| `en/br_tech_bak_251103.html:217` | root-relative | `/assets/img/br/tech_sub3_step3_1.jpg` |
| `en/br_tech_bak_251103.html:222` | root-relative | `/assets/img/br/tech_sub3_step3_2.jpg` |
| `en/br_tech_bak_251103.html:227` | root-relative | `/assets/img/br/tech_sub3_step3_3.jpg` |
| `en/br_tech_bak_251103.html:232` | root-relative | `/assets/img/br/tech_sub3_step3_4.jpg` |
| `en/br_tech_bak_251103.html:237` | root-relative | `/assets/img/br/tech_sub3_step3_5.jpg` |
| `en/br_tech_bak_251103.html:242` | root-relative | `/assets/img/br/tech_sub3_step3_6.jpg` |
| `en/br_tech_bak_251103.html:258` | root-relative | `/assets/img/br/tech_sub3_step4_1.jpg` |
| `en/br_tech_bak_251103.html:263` | root-relative | `/assets/img/br/tech_sub3_step4_2.jpg` |
| `en/br_tech_bak_251103.html:268` | root-relative | `/assets/img/br/tech_sub3_step4_3.jpg` |
| `en/br_tech_bak_251103.html:307` | root-relative | `/assets/img/br/tech_sub4_ico1.svg` |
| `en/br_tech_bak_251103.html:312` | root-relative | `/assets/img/br/tech_sub4_ico2.svg` |
| `en/br_tech_bak_251103.html:317` | root-relative | `/assets/img/br/tech_sub4_ico3.svg` |
| `en/br_tech_bak_251103.html:322` | root-relative | `/assets/img/br/tech_sub4_ico4.svg` |
| `en/br_tech_bak_251103.html:327` | root-relative | `/assets/img/br/tech_sub4_ico5.svg` |
| `en/br_tech_bak_251103.html:332` | root-relative | `/assets/img/br/tech_sub4_ico6.svg` |
| `en/br_tech_bak_251103.html:337` | root-relative | `/assets/img/br/tech_sub4_ico7.svg` |
| `en/br_value.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/dt_explain.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/dt_sw.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/dt_use.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/dx.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/dx_250612.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/faq.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/hosting_index1.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/index.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/pr_brochure.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/pr_ci.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/pr_news.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/pr_news_view_251127.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/pr_news_view_260121.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/pr_news_view_260519.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/pr_news_view_260527.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_bigroom.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_solution.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_solution.html:82` | root-relative | `/assets/img/sv/eng/solution_design_obj_point.png` |
| `en/sv_solution.html:147` | root-relative | `/assets/img/sv/solution_construction_obj_point.png` |
| `en/sv_solution.html:208` | root-relative | `/assets/img/sv/solution_op_obj_point.png` |
| `en/sv_solution.html:274` | root-relative | `/assets/img/sv/eng/solution_end_obj.png` |
| `en/sv_solution.html:83` | root-relative | `/assets/img/sv/eng/solution_design_obj_point.png` |
| `en/sv_solution.html:148` | root-relative | `/assets/img/sv/solution_construction_obj_point.png` |
| `en/sv_solution_construction.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_solution_operation.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_sw.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_sw_egbim.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_sw_gaia.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_sw_ipipes.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_sw_kngil.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/sv_sw_pq_program.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/video_ex.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/br_future.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/br_future_bak_250610.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/br_future_bak_250610.html:57` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `ko/br_future_bak_250610.html:108` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `ko/br_future_bak_250610.html:114` | root-relative | `/assets/img/br/future_sub2_process_bg.png` |
| `ko/br_future_bak_250610.html:115` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `ko/br_future_bak_250610.html:128` | root-relative | `/assets/img/br/future_sub2_product_bg.png` |
| `ko/br_future_bak_250610.html:129` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `ko/br_future_bak_250610.html:176` | root-relative | `/assets/img/br/future_sub3_easy.jpg` |
| `ko/br_future_bak_250610.html:186` | root-relative | `/assets/img/br/future_sub3_convenient.jpg` |
| `ko/br_future_bak_250610.html:196` | root-relative | `/assets/img/br/future_sub3_quality.jpg` |
| `ko/br_future_bak_250610.html:206` | root-relative | `/assets/img/br/future_sub3_cost.jpg` |
| `ko/br_future_bak_250610.html:216` | root-relative | `/assets/img/br/future_sub3_fast.jpg` |
| `ko/br_future_bak_250610.html:111` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `ko/br_future_bak_250610.html:117` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `ko/br_future_bak_250610.html:131` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `ko/br_future_bak_251103.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/br_future_bak_251103.html:62` | root-relative | `/assets/img/br/future_sub1_m_bg.png` |
| `ko/br_future_bak_251103.html:66` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `ko/br_future_bak_251103.html:70` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `ko/br_future_bak_251103.html:109` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `ko/br_future_bak_251103.html:116` | root-relative | `/assets/img/br/future_sub2_process_bg.png` |
| `ko/br_future_bak_251103.html:117` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `ko/br_future_bak_251103.html:135` | root-relative | `/assets/img/br/future_sub2_product_bg.png` |
| `ko/br_future_bak_251103.html:136` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `ko/br_future_bak_251103.html:215` | root-relative | `/assets/img/br/future_sub3_easy.jpg` |
| `ko/br_future_bak_251103.html:225` | root-relative | `/assets/img/br/future_sub3_convenient.jpg` |
| `ko/br_future_bak_251103.html:235` | root-relative | `/assets/img/br/future_sub3_quality.jpg` |
| `ko/br_future_bak_251103.html:245` | root-relative | `/assets/img/br/future_sub3_cost.jpg` |
| `ko/br_future_bak_251103.html:255` | root-relative | `/assets/img/br/future_sub3_fast.jpg` |
| `ko/br_future_bak_251103.html:64` | root-relative | `/assets/img/br/future_sub1_m_bg.png` |
| `ko/br_future_bak_251103.html:68` | root-relative | `/assets/img/br/future_sub1_bg.png` |
| `ko/br_future_bak_251103.html:112` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `ko/br_future_bak_251103.html:119` | root-relative | `/assets/img/br/future_sub2_process_point.png` |
| `ko/br_future_bak_251103.html:138` | root-relative | `/assets/img/br/future_sub2_product_point.png` |
| `ko/br_tech.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/br_tech_bak_251103.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/br_tech_bak_251103.html:75` | root-relative | `/assets/img/br/tech_sub1_sw_bg.jpg` |
| `ko/br_tech_bak_251103.html:82` | root-relative | `/assets/img/br/tech_sub1_hw_bg.jpg` |
| `ko/br_tech_bak_251103.html:146` | root-relative | `/assets/img/br/tech_sub3_step1_1.jpg` |
| `ko/br_tech_bak_251103.html:151` | root-relative | `/assets/img/br/tech_sub3_step1_2.jpg` |
| `ko/br_tech_bak_251103.html:156` | root-relative | `/assets/img/br/tech_sub3_step1_3.jpg` |
| `ko/br_tech_bak_251103.html:161` | root-relative | `/assets/img/br/tech_sub3_step1_4.jpg` |
| `ko/br_tech_bak_251103.html:166` | root-relative | `/assets/img/br/tech_sub3_step1_5.jpg` |
| `ko/br_tech_bak_251103.html:182` | root-relative | `/assets/img/br/tech_sub3_step2_1.jpg` |
| `ko/br_tech_bak_251103.html:187` | root-relative | `/assets/img/br/tech_sub3_step2_2.jpg` |
| `ko/br_tech_bak_251103.html:192` | root-relative | `/assets/img/br/tech_sub3_step2_3.jpg` |
| `ko/br_tech_bak_251103.html:197` | root-relative | `/assets/img/br/tech_sub3_step2_4.jpg` |
| `ko/br_tech_bak_251103.html:202` | root-relative | `/assets/img/br/tech_sub3_step2_5.jpg` |
| `ko/br_tech_bak_251103.html:217` | root-relative | `/assets/img/br/tech_sub3_step3_1.jpg` |
| `ko/br_tech_bak_251103.html:222` | root-relative | `/assets/img/br/tech_sub3_step3_2.jpg` |
| `ko/br_tech_bak_251103.html:227` | root-relative | `/assets/img/br/tech_sub3_step3_3.jpg` |
| `ko/br_tech_bak_251103.html:232` | root-relative | `/assets/img/br/tech_sub3_step3_4.jpg` |
| `ko/br_tech_bak_251103.html:237` | root-relative | `/assets/img/br/tech_sub3_step3_5.jpg` |
| `ko/br_tech_bak_251103.html:242` | root-relative | `/assets/img/br/tech_sub3_step3_6.jpg` |
| `ko/br_tech_bak_251103.html:258` | root-relative | `/assets/img/br/tech_sub3_step4_1.jpg` |
| `ko/br_tech_bak_251103.html:263` | root-relative | `/assets/img/br/tech_sub3_step4_2.jpg` |
| `ko/br_tech_bak_251103.html:268` | root-relative | `/assets/img/br/tech_sub3_step4_3.jpg` |
| `ko/br_tech_bak_251103.html:307` | root-relative | `/assets/img/br/tech_sub4_ico1.svg` |
| `ko/br_tech_bak_251103.html:312` | root-relative | `/assets/img/br/tech_sub4_ico2.svg` |
| `ko/br_tech_bak_251103.html:317` | root-relative | `/assets/img/br/tech_sub4_ico3.svg` |
| `ko/br_tech_bak_251103.html:322` | root-relative | `/assets/img/br/tech_sub4_ico4.svg` |
| `ko/br_tech_bak_251103.html:327` | root-relative | `/assets/img/br/tech_sub4_ico5.svg` |
| `ko/br_tech_bak_251103.html:332` | root-relative | `/assets/img/br/tech_sub4_ico6.svg` |
| `ko/br_tech_bak_251103.html:337` | root-relative | `/assets/img/br/tech_sub4_ico7.svg` |
| `ko/br_value.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/dt_explain.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/dt_sw.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/dt_use.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/dx.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/dx_250612.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/faq.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/GitUpload_test_staging_ok.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/hosting_index1.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/index.html:31` | external | `http://baroncs.co.kr/assets/img/og-main-thumb_baron.JPG` |
| `ko/pr_brochure.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/pr_ci.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/pr_news.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/pr_news_view_251127.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/pr_news_view_260121.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/pr_news_view_260519.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/pr_news_view_260527.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_bigroom.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_solution.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_solution.html:64` | root-relative | `/assets/img/sv/solution_design_obj_point.png` |
| `ko/sv_solution.html:129` | root-relative | `/assets/img/sv/solution_construction_obj_point.png` |
| `ko/sv_solution.html:194` | root-relative | `/assets/img/sv/solution_op_obj_point.png` |
| `ko/sv_solution.html:261` | root-relative | `/assets/img/sv/solution_end_obj.png` |
| `ko/sv_solution.html:65` | root-relative | `/assets/img/sv/solution_design_obj_point.png` |
| `ko/sv_solution.html:130` | root-relative | `/assets/img/sv/solution_construction_obj_point.png` |
| `ko/sv_solution_construction.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_solution_operation.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_sw.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_sw_egbim.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_sw_gaia.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_sw_ipipes.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_sw_kngil.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/sv_sw_pq_program.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/video_ex.html:6` | root-relative | `/assets/img/favicon.ico` |
| `_include/header.html:131` | root-relative | `/assets/img/ico_user.svg` |
| `_include/eng/footer.html:3` | root-relative | `/assets/img/eng/logo_w.svg` |
| `_include/eng/header.html:60` | root-relative | `/assets/img/ico_user.svg` |
| `_include/eng/header.html:3` | root-relative | `/assets/img/eng/logo_w.svg` |
| `ko/egbim/buy.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/egbim/floorplan.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/egbim/forbim.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/egbim/interface.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/egbim/primary.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/egbim/value.html:6` | root-relative | `/assets/img/favicon.ico` |
| `ko/gaia/buy.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/gaia/further.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/gaia/index.html:21` | root-relative | `/assets/img/favicon.ico` |
| `ko/gaia/index.html:30` | external | `http://k-gaia.co.kr/gaia/img/og-main-thumb.JPG` |
| `ko/gaia/index.html:37` | root-relative | `/assets/img/favicon.ico` |
| `ko/gaia/primary.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/gaia/results.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/gaia/value.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/kngil/analysis.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/kngil/buy.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/kngil/primary.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/kngil/provided.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/kngil/results.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/kngil/value.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/buy.html:15` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/index.html:15` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/index.html:20` | external | `http://k-tova.com/tova/img/og-main-thumb.JPG` |
| `ko/tova/index.html:27` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/primary.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/public.html:19` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/road.html:15` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/value.html:15` | root-relative | `/assets/img/favicon.ico` |
| `ko/tova/js/common.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `ko/tova/js/common.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `ko/egbim/js/common.js:456` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `ko/egbim/js/common.js:506` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `ko/egbim/js/common_240813.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `ko/egbim/js/common_240813.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `ko/egbim/js/common_250204.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `ko/egbim/js/common_250204.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `ko/egbim/js/common_250307.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `ko/egbim/js/common_250307.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `ko/egbim/js/common_bak.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `ko/egbim/js/common_bak.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `ko/egbim/js/common_OR.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `ko/egbim/js/common_OR.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `ko/egbim/js/interface.js:140` | dynamic | `img/com_img/comp_${i}.png` |
| `ko/egbim/js/owlcarousel/owl.carousel.js:2366` | root-relative | `/hqdefault.jpg` |
| `ko/egbim/js/owlcarousel/owl.carousel.min.js:6` | root-relative | `/hqdefault.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:2` | external | `https://ckeditor.com/img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:2` | external | `https://ckeditor.com/img/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | external | `https://ckeditor.com/img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | external | `https://ckeditor.com/img/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | root-relative | `/img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | root-relative | `/img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/../img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/../../img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/../img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/../../img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:6` | root-relative | `/img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:6` | root-relative | `/img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:7` | root-relative | `/img/image1.jpg` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:7` | root-relative | `/img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:8` | root-relative | `/img/big/image2.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integration.html:2` | external | `https://ckeditor.com/docs/ckeditor4/latest/examples/assets/image/bilancino-logo.png` |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integration.html:22` | external | `https://ckeditor.com/docs/ckeditor4/latest/examples/assets/image/signature.png` |
| `en/egbim/buy.html:5` | root-relative | `/assets/img/favicon.ico` |
| `en/egbim/floorplan.html:7` | root-relative | `/assets/img/favicon.ico` |
| `en/egbim/forbim.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/egbim/interface.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/egbim/primary.html:6` | root-relative | `/assets/img/favicon.ico` |
| `en/egbim/value.html:5` | root-relative | `/assets/img/favicon.ico` |
| `en/gaia/buy.html:19` | root-relative | `/assets/img/favicon.ico` |
| `en/gaia/further.html:19` | root-relative | `/assets/img/favicon.ico` |
| `en/gaia/index.html:21` | root-relative | `/assets/img/favicon.ico` |
| `en/gaia/index.html:30` | external | `http://k-gaia.co.kr/eng/img/og-main-thumb.JPG` |
| `en/gaia/primary.html:19` | root-relative | `/assets/img/favicon.ico` |
| `en/gaia/results.html:19` | root-relative | `/assets/img/favicon.ico` |
| `en/gaia/value.html:19` | root-relative | `/assets/img/favicon.ico` |
| `en/tova/buy.html:15` | root-relative | `/assets/img/favicon.ico` |
| `en/tova/index.html:15` | root-relative | `/assets/img/favicon.ico` |
| `en/tova/index.html:20` | external | `http://k-tova.com/eng/img/og-main-thumb.JPG` |
| `en/tova/primary.html:19` | root-relative | `/assets/img/favicon.ico` |
| `en/tova/public.html:19` | root-relative | `/assets/img/favicon.ico` |
| `en/tova/road.html:15` | root-relative | `/assets/img/favicon.ico` |
| `en/tova/value.html:15` | root-relative | `/assets/img/favicon.ico` |
| `en/tova/js/common.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `en/tova/js/common.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `en/egbim/js/common.js:456` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `en/egbim/js/common.js:506` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `en/egbim/js/common_240813.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `en/egbim/js/common_240813.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `en/egbim/js/common_250204.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `en/egbim/js/common_250204.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `en/egbim/js/common_250307.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `en/egbim/js/common_250307.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `en/egbim/js/common_bak.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `en/egbim/js/common_bak.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `en/egbim/js/common_OR.js:426` | external | `//t1.daumcdn.net/postcode/resource/images/close.png` |
| `en/egbim/js/common_OR.js:470` | external | `//i1.daumcdn.net/localimg/localimages/07/postcode/320/close.png` |
| `en/egbim/js/interface.js:139` | dynamic | `img/com_img/eng/comp_${i}.png` |
| `en/egbim/js/interface_251226.js:128` | dynamic | `../img/com_img/comp_${i}.png` |
| `en/egbim/js/owlcarousel/owl.carousel.js:2366` | root-relative | `/hqdefault.jpg` |
| `en/egbim/js/owlcarousel/owl.carousel.min.js:6` | root-relative | `/hqdefault.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:2` | external | `https://ckeditor.com/img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:2` | external | `https://ckeditor.com/img/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | external | `https://ckeditor.com/img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | external | `https://ckeditor.com/img/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | root-relative | `/img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:3` | root-relative | `/img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/../img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/../../img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:4` | root-relative | `/img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/../img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:5` | root-relative | `/../../img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:6` | root-relative | `/img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:6` | root-relative | `/img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:7` | root-relative | `/img/image1.jpg` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:7` | root-relative | `/img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js:8` | root-relative | `/img/big/image2.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integration.html:2` | external | `https://ckeditor.com/docs/ckeditor4/latest/examples/assets/image/bilancino-logo.png` |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integration.html:22` | external | `https://ckeditor.com/docs/ckeditor4/latest/examples/assets/image/signature.png` |
| `cloudflare-worker/src/index.js:44` | root-relative | `/assets/img/favicon.ico` |
| `cloudflare-worker/src/index.js:45` | root-relative | `/assets/img/og-main-thumb_baron.JPG` |
| `cloudflare-worker/src/index.js:46` | root-relative | `/assets/img/logo_c.svg` |
| `cloudflare-worker/src/index.js:47` | root-relative | `/assets/img/logo_w.svg` |
| `cloudflare-worker/src/index.js:48` | root-relative | `/assets/img/logo.svg` |
| `cloudflare-worker/src/index.js:49` | root-relative | `/assets/img/ico_language.svg` |
| `cloudflare-worker/src/index.js:50` | root-relative | `/assets/img/ico_language_w.svg` |
| `cloudflare-worker/src/index.js:51` | root-relative | `/assets/img/ico_more.svg` |
| `cloudflare-worker/src/index.js:52` | root-relative | `/assets/img/ico_more_hover.svg` |
| `cloudflare-worker/src/index.js:53` | root-relative | `/assets/img/ico_angle.svg` |
| `cloudflare-worker/src/index.js:54` | root-relative | `/assets/img/ico_home.svg` |
| `cloudflare-worker/src/index.js:55` | root-relative | `/assets/img/ico_close.svg` |
| `cloudflare-worker/src/index.js:56` | root-relative | `/assets/img/flipbook_corner.png` |
| `cloudflare-worker/src/index.js:57` | root-relative | `/assets/img/eng/logo_c.svg` |
| `cloudflare-worker/src/index.js:58` | root-relative | `/assets/img/eng/logo_w.svg` |
| `assets/css/style copy.css:174` | root-relative | `/assets/img/flipbook_corner.png` |
| `assets/css/style copy.css:263` | root-relative | `/assets/img/logo_c.svg` |
| `assets/css/style copy.css:267` | root-relative | `/assets/img/logo_w.svg` |
| `assets/css/style copy.css:329` | root-relative | `/assets/img/logo_c.svg` |
| `assets/css/style copy.css:384` | root-relative | `/assets/img/ico_more.svg` |
| `assets/css/style copy.css:479` | root-relative | `/assets/img/logo_c.svg` |
| `assets/css/style copy.css:582` | root-relative | `/assets/img/ico_more.svg` |
| `assets/css/style copy.css:591` | root-relative | `/assets/img/ico_more_hover.svg` |
| `assets/css/style copy.css:674` | root-relative | `/assets/img/ico_more.svg` |
| `assets/css/style copy.css:726` | root-relative | `/assets/img/ico_angle.svg` |
| `assets/css/style copy.css:779` | root-relative | `/assets/img/logo_w.svg` |
| `assets/css/style copy.css:1091` | root-relative | `/assets/img/flipbook_corner.png` |
| `assets/css/style copy.css:1238` | root-relative | `/assets/img/ico_more.svg` |
| `assets/css/style copy.css:1290` | root-relative | `/assets/img/ico_angle.svg` |
| `assets/css/style copy.css:1343` | root-relative | `/assets/img/logo_w.svg` |
| `assets/css/style copy.css:1444` | root-relative | `/assets/img/ico_home.svg` |
| `assets/css/style copy.css:1520` | root-relative | `/assets/img/ico_more.svg` |
| `assets/css/style copy.css:1532` | root-relative | `/assets/img/ico_more_hover.svg` |
| `assets/css/style copy.css:1708` | root-relative | `/assets/img/br/future_sub1_cut1.png` |
| `assets/css/style copy.css:1711` | root-relative | `/assets/img/br/future_sub1_cut2.png` |
| `assets/css/style copy.css:1714` | root-relative | `/assets/img/br/future_sub1_cut3.png` |
| `assets/css/style copy.css:1717` | root-relative | `/assets/img/br/future_sub1_cut4.png` |
| `assets/css/style copy.css:1840` | root-relative | `/assets/img/br/future_sub2_line.svg` |
| `assets/css/style copy.css:1907` | root-relative | `/assets/img/br/future_sub2_process_ico.svg` |
| `assets/css/style copy.css:1936` | root-relative | `/assets/img/br/future_sub2_product_ico.svg` |
| `assets/css/style copy.css:1991` | root-relative | `/assets/img/br/future_sub3_bg.png` |
| `assets/css/style copy.css:2098` | root-relative | `/assets/img/br/tech_intro_bg.jpg` |
| `assets/css/style copy.css:2461` | root-relative | `/assets/img/br/tech_sub3_step1_ico_k.svg` |
| `assets/css/style copy.css:2465` | root-relative | `/assets/img/br/tech_sub3_step2_ico_k.svg` |
| `assets/css/style copy.css:2468` | root-relative | `/assets/img/br/tech_sub3_step3_ico_k.svg` |
| `assets/css/style copy.css:2471` | root-relative | `/assets/img/br/tech_sub3_step4_ico_k.svg` |
| `assets/css/style copy.css:2525` | root-relative | `/assets/img/br/tech_sub3_step1_ico_c.svg` |
| `assets/css/style copy.css:2529` | root-relative | `/assets/img/br/tech_sub3_step2_ico_c.svg` |
| `assets/css/style copy.css:2533` | root-relative | `/assets/img/br/tech_sub3_step3_ico_c.svg` |
| `assets/css/style copy.css:2537` | root-relative | `/assets/img/br/tech_sub3_step4_ico_c.svg` |
| `assets/css/style copy.css:2558` | root-relative | `/assets/img/br/tech_sub4_bigroom.jpg` |
| `assets/css/style copy.css:2583` | root-relative | `/assets/img/mask_tail.svg` |
| `assets/css/style copy.css:2811` | root-relative | `/assets/img/common_bg_left.jpg` |
| `assets/css/style copy.css:2815` | root-relative | `/assets/img/common_bg_right.jpg` |
| `assets/css/style copy.css:2831` | root-relative | `/assets/img/br/value_intro_bg_left.png` |
| `assets/css/style copy.css:2832` | root-relative | `/assets/img/br/value_intro_bg_right.png` |
| `assets/css/style copy.css:3038` | root-relative | `/assets/img/br/value_sub2_our1.jpg` |
| `assets/css/style copy.css:3042` | root-relative | `/assets/img/br/value_sub2_our2.jpg` |
| `assets/css/style copy.css:3047` | root-relative | `/assets/img/br/value_sub2_our3.jpg` |
| `assets/css/style copy.css:3271` | root-relative | `/assets/img/common_bg_left.jpg` |
| `assets/css/style copy.css:3275` | root-relative | `/assets/img/common_bg_right.jpg` |
| `assets/css/style copy.css:3436` | root-relative | `/assets/img/dt/common_end_bg.jpg` |
| `assets/css/style copy.css:3462` | root-relative | `/assets/img/dt/explain_intro_bg.jpg` |
| `assets/css/style copy.css:3588` | root-relative | `/assets/img/dt/sw_intro_bg.jpg` |
| `assets/css/style copy.css:3672` | root-relative | `/assets/img/dt/use_intro_bg.jpg` |
| `assets/css/style copy.css:3740` | root-relative | `/assets/img/dt/use_end_obj1.jpg` |
| `assets/css/style copy.css:3743` | root-relative | `/assets/img/dt/use_end_obj2.jpg` |
| `assets/css/style copy.css:3828` | root-relative | `/assets/img/dt/explain_gis_obj1.jpg` |
| `assets/css/style copy.css:3831` | root-relative | `/assets/img/dt/explain_gis_obj1.jpg` |
| `assets/css/style copy.css:3834` | root-relative | `/assets/img/dt/explain_gis_obj2.jpg` |
| `assets/css/style copy.css:3837` | root-relative | `/assets/img/dt/explain_gis_obj2.jpg` |
| `assets/css/style copy.css:3840` | root-relative | `/assets/img/dt/explain_gis_obj1.jpg` |
| `assets/css/style copy.css:3884` | root-relative | `/assets/img/dt/use_process_obj1.jpg` |
| `assets/css/style copy.css:3887` | root-relative | `/assets/img/dt/use_process_obj1.jpg` |
| `assets/css/style copy.css:3890` | root-relative | `/assets/img/dt/use_process_obj2.jpg` |
| `assets/css/style copy.css:3893` | root-relative | `/assets/img/dt/use_process_obj2.jpg` |
| `assets/css/style copy.css:3896` | root-relative | `/assets/img/dt/use_process_obj1.jpg` |
| `assets/css/style copy.css:3901` | root-relative | `/assets/img/dt/use_cycle_obj1.jpg` |
| `assets/css/style copy.css:3904` | root-relative | `/assets/img/dt/use_cycle_obj1.jpg` |
| `assets/css/style copy.css:3907` | root-relative | `/assets/img/dt/use_cycle_obj2.jpg` |
| `assets/css/style copy.css:3910` | root-relative | `/assets/img/dt/use_cycle_obj2.jpg` |
| `assets/css/style copy.css:3913` | root-relative | `/assets/img/dt/use_cycle_obj3.jpg` |
| `assets/css/style copy.css:3916` | root-relative | `/assets/img/dt/use_cycle_obj3.jpg` |
| `assets/css/style copy.css:3919` | root-relative | `/assets/img/dt/use_cycle_obj4.jpg` |
| `assets/css/style copy.css:3922` | root-relative | `/assets/img/dt/use_cycle_obj4.jpg` |
| `assets/css/style copy.css:3925` | root-relative | `/assets/img/dt/use_cycle_obj1.jpg` |
| `assets/css/style copy.css:3959` | root-relative | `/assets/img/sv/common_bg_grid.png` |
| `assets/css/style copy.css:3964` | root-relative | `/assets/img/sv/common_bg_grid.png` |
| `assets/css/style copy.css:4009` | root-relative | `/assets/img/sv/common_obj_mask_left.svg` |
| `assets/css/style copy.css:4029` | root-relative | `/assets/img/sv/common_obj_bg.png` |
| `assets/css/style copy.css:4048` | root-relative | `/assets/img/sv/common_intro_mask.svg` |
| `assets/css/style copy.css:4067` | root-relative | `/assets/img/sv/common_obj_mask_right.svg` |
| `assets/css/style copy.css:4152` | root-relative | `/assets/img/ico_close.svg` |
| `assets/css/style copy.css:4247` | root-relative | `/assets/img/sv/solution_intro_bg.jpg` |
| `assets/css/style copy.css:4454` | root-relative | `/assets/img/sv/sw_intro_bg.jpg` |
| `assets/css/style copy.css:4470` | root-relative | `/assets/img/sv/common_intro_mask.svg` |
| `assets/css/style copy.css:4489` | root-relative | `/assets/img/sv/sw_list_bg1.jpg` |
| `assets/css/style copy.css:4494` | root-relative | `/assets/img/sv/sw_list_bg2.png` |
| `assets/css/style copy.css:4589` | root-relative | `/assets/img/sv/sw_end_bg.jpg` |
| `assets/css/style copy.css:4635` | root-relative | `/assets/img/ico_arrow.svg` |
| `assets/css/style copy.css:4662` | root-relative | `/assets/img/sv/bg_sw_package.png` |
| `assets/css/style copy.css:4757` | root-relative | `/assets/img/sv/bigroom_intro_bg.jpg` |
| `assets/css/style copy.css:4771` | root-relative | `/assets/img/sv/bigroom_infra_obj1.jpg` |
| `assets/css/style copy.css:4834` | root-relative | `/assets/img/sv/solution_construction_obj1.jpg` |
| `assets/css/style copy.css:4837` | root-relative | `/assets/img/sv/solution_construction_obj1.jpg` |
| `assets/css/style copy.css:4840` | root-relative | `/assets/img/sv/solution_construction_obj2.jpg` |
| `assets/css/style copy.css:4843` | root-relative | `/assets/img/sv/solution_construction_obj2.jpg` |
| `assets/css/style copy.css:4846` | root-relative | `/assets/img/sv/solution_construction_obj1.jpg` |
| `assets/css/style copy.css:4851` | root-relative | `/assets/img/sv/solution_op_obj1.jpg` |
| `assets/css/style copy.css:4854` | root-relative | `/assets/img/sv/solution_op_obj1.jpg` |
| `assets/css/style copy.css:4857` | root-relative | `/assets/img/sv/solution_op_obj2.jpg` |
| `assets/css/style copy.css:4860` | root-relative | `/assets/img/sv/solution_op_obj2.jpg` |
| `assets/css/style copy.css:4863` | root-relative | `/assets/img/sv/solution_op_obj1.jpg` |
| `assets/css/style copy.css:4899` | root-relative | `/assets/img/sv/bigroom_real_obj1.jpg` |
| `assets/css/style copy.css:4902` | root-relative | `/assets/img/sv/bigroom_real_obj1.jpg` |
| `assets/css/style copy.css:4905` | root-relative | `/assets/img/sv/bigroom_real_obj2.jpg` |
| `assets/css/style copy.css:4908` | root-relative | `/assets/img/sv/bigroom_real_obj2.jpg` |
| `assets/css/style copy.css:4911` | root-relative | `/assets/img/sv/bigroom_real_obj3.jpg` |
| `assets/css/style copy.css:4914` | root-relative | `/assets/img/sv/bigroom_real_obj3.jpg` |
| `assets/css/style copy.css:4917` | root-relative | `/assets/img/sv/bigroom_real_obj4.jpg` |
| `assets/css/style copy.css:4920` | root-relative | `/assets/img/sv/bigroom_real_obj4.jpg` |
| `assets/css/style copy.css:4934` | root-relative | `/assets/img/dx/intro_bg.jpg` |
| `assets/css/style copy.css:5000` | root-relative | `/assets/img/dx/contents_bg.jpg` |
| `assets/css/style copy.css:5322` | root-relative | `/asset/img/pr/pr_intro_bg.png` |
| `assets/css/style.css:5322` | root-relative | `/asset/img/pr/pr_intro_bg.png` |
| `assets/img/dt_use.html:75` | root-relative | `/assets/img/dt/use_overview_obj.jpg` |
| `assets/img/dt_use.html:106` | root-relative | `/assets/img/dt/use_process_obj_point.png` |
| `assets/img/dt_use.html:140` | root-relative | `/assets/img/dt/use_system_obj_point.png` |
| `assets/img/dt_use.html:169` | root-relative | `/assets/img/dt/use_cycle_obj_point.png` |
| `assets/js/dt.js:24` | dynamic | `../assets/img/dt/m_${pageType}_${value}.jpg` |
| `assets/js/dt.js:28` | dynamic | `../assets/img/dt/${pageType}_${value}.jpg` |
| `assets/js/dt.js:30` | dynamic | `../assets/img/dt/${pageType}_${value}.jpg` |
| `assets/js/dx.js:544` | dynamic | `https://img.youtube.com/vi/${videoId}/hqdefault.jpg` |
| `assets/js/dx_250612.js:351` | dynamic | `https://img.youtube.com/vi/${videoId}/hqdefault.jpg` |
| `assets/js/recruit.js:67` | dynamic | `../assets/img/recruit/m_recruit_${value}.jpg` |
| `assets/js/recruit.js:71` | dynamic | `../assets/img/recruit/recruit_${value}.jpg` |
| `assets/js/recruit.js:73` | dynamic | `../assets/img/recruit/m_recruit_${value}.jpg` |
| `assets/js/sv.js:28` | dynamic | `../assets/img/sv/m_${pageType}_${value}.jpg` |
| `assets/js/sv.js:32` | dynamic | `../assets/img/sv/${pageType}_${value}.jpg` |
| `assets/js/sv.js:34` | dynamic | `../assets/img/sv/${pageType}_${value}.jpg` |
| `assets/js/sv.js:129` | dynamic | `../assets/img/sv/m_${pageType}_op_more.jpg` |
| `assets/js/sv.js:133` | dynamic | `../assets/img/sv/${pageType}_op_more.jpg` |
| `assets/js/sv.js:135` | dynamic | `../assets/img/sv/${pageType}_op_more.jpg` |
| `assets/js/eng/dt.js:24` | dynamic | `../assets/img/dt/eng/m_${pageType}_${value}.jpg` |
| `assets/js/eng/dt.js:28` | dynamic | `../assets/img/dt/eng/${pageType}_${value}.jpg` |
| `assets/js/eng/dt.js:30` | dynamic | `../assets/img/dt/eng/${pageType}_${value}.jpg` |
| `assets/js/eng/dx.js:544` | dynamic | `https://img.youtube.com/vi/${videoId}/hqdefault.jpg` |
| `assets/js/eng/sv.js:28` | dynamic | `../assets/img/sv/eng/m_${pageType}_${value}.jpg` |
| `assets/js/eng/sv.js:32` | dynamic | `../assets/img/sv/eng/${pageType}_${value}.jpg` |
| `assets/js/eng/sv.js:34` | dynamic | `../assets/img/sv/eng/${pageType}_${value}.jpg` |
| `assets/js/eng/sv.js:129` | dynamic | `../assets/img/sv/eng/m_${pageType}_op_more.jpg` |
| `assets/js/eng/sv.js:133` | dynamic | `../assets/img/sv/eng/${pageType}_op_more.jpg` |
| `assets/js/eng/sv.js:135` | dynamic | `../assets/img/sv/eng/${pageType}_op_more.jpg` |
| `assets/js/gaia/common.js:387` | root-relative | `/assets/img/eng/logo_c.svg` |
| `assets/js/gaia/common.js:387` | root-relative | `/assets/img/logo_c.svg` |
| `assets/js/gaia/common.js:388` | root-relative | `/assets/img/eng/logo_w.svg` |
| `assets/js/gaia/common.js:388` | root-relative | `/assets/img/logo_w.svg` |
