# 전체 파일 로딩 감사 목록

> `90c1cc9` 기반 작업 당시의 목록입니다. 이후 반영한 `homepage_test/main`의 `cebb14b` 파일 목록과는 다를 수 있습니다.

개선 전 저장소 스캔. `.git`, 설치 도구, node_modules, 측정 산출물은 제외했습니다.

HTML/CSS/JS는 주석을 제거한 뒤 정적 URL 참조를 검사했습니다. 바이너리는 크기와 참조 관계를 검사했습니다. 모든 소스의 업무 로직을 수동 검증한 목록은 아닙니다.

외부 참조에는 링크도 포함됩니다. 존재하지 않는 참조도 동적 경로·앵커·템플릿 해석의 한계가 있으므로 실제 네트워크 오류로 단정하지 않습니다. 실행 시 오류는 별도 Playwright 보고서를 확인하세요.

총 3,932개 파일, 239개 HTML, 5.105 GB.

| 파일 | 크기 (bytes) | 검사 내용 |
|---|---:|---|
| `.github/workflows/deploy-r2.yml` | 8,387 | 파일 크기/참조 검사 |
| `.gitignore` | 175 | 파일 크기/참조 검사 |
| `.htaccess` | 65 | 파일 크기/참조 검사 |
| `LICENSE` | 11,558 | 파일 크기/참조 검사 |
| `_include/eng/footer.html` | 5,102 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 2 |
| `_include/eng/header.html` | 2,071 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 4 |
| `_include/eng/header_bak_250609.html` | 1,293 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 5; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `_include/eng/header_recruit.html` | 1,443 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 7 |
| `_include/eng/nav.html` | 2,364 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 23 |
| `_include/eng/nav_recruit.html` | 303 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 3 |
| `_include/footer.html` | 4,947 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0 |
| `_include/header.html` | 1,070 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `_include/header_bak_250609.html` | 1,293 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 5; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `_include/header_recruit.html` | 1,443 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 5 |
| `_include/nav.html` | 2,403 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `_include/nav_recruit.html` | 303 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 3 |
| `assets/assets_img.zip` | 1,209,498,030 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/css/baron.css` | 65,640 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/common.css` | 13,114 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/digital.css` | 23,022 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/dx.css` | 15,777 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `assets/css/eng/baron.css` | 66,204 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/eng/common.css` | 14,319 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/eng/digital.css` | 23,181 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/eng/dx.css` | 15,842 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `assets/css/eng/pr.css` | 22,873 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/eng/sevice.css` | 36,788 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `assets/css/faq.css` | 5,475 | 텍스트 리소스 참조 검사 |
| `assets/css/font.css` | 4,054 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `assets/css/layout.css` | 32,335 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/lib/aos.min.css` | 26,053 | 텍스트 리소스 참조 검사 |
| `assets/css/lib/lenis.min.css` | 244 | 텍스트 리소스 참조 검사 |
| `assets/css/lib/swiper11.min.css` | 18,466 | 텍스트 리소스 참조 검사 |
| `assets/css/pr.css` | 21,868 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/css/recruit.css` | 96,181 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 10 |
| `assets/css/reset.css` | 2,252 | 텍스트 리소스 참조 검사 |
| `assets/css/sevice.css` | 36,793 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `assets/css/style copy.css` | 125,830 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 3 |
| `assets/css/style.css` | 125,289 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 3 |
| `assets/file/baron_bro.pdf` | 3,623,108 | 파일 크기/참조 검사 |
| `assets/file/baron_bro_en.pdf` | 3,537,892 | 파일 크기/참조 검사 |
| `assets/file/baron_bro_kr.pdf` | 3,666,828 | 파일 크기/참조 검사 |
| `assets/file/baron_ci.zip` | 2,730,295 | 파일 크기/참조 검사 |
| `assets/file/hanmac_bro.pdf` | 37,495,201 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/file/hanmac_bro_en.pdf` | 37,252,257 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/file/입사지원서_바론_경력.hwp` | 727,552 | 파일 크기/참조 검사 |
| `assets/file/입사지원서_바론_신입.hwp` | 735,744 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Bold/NanumSquareNeoOTF-Bd.otf` | 1,643,528 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Bold/NanumSquareNeoTTF-cBd.woff` | 741,752 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Bold/NanumSquareNeoTTF-cBd.woff2` | 384,992 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-ExtraBold/NanumSquareNeoOTF-Eb.otf` | 1,681,436 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-ExtraBold/NanumSquareNeoTTF-dEb.woff` | 750,328 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-ExtraBold/NanumSquareNeoTTF-dEb.woff2` | 388,128 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Heavy/NanumSquareNeoOTF-Hv.otf` | 1,673,844 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Heavy/NanumSquareNeoTTF-eHv.woff` | 722,332 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Heavy/NanumSquareNeoTTF-eHv.woff2` | 361,340 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Light/NanumSquareNeoOTF-Lt.otf` | 1,670,640 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Light/NanumSquareNeoTTF-aLt.woff` | 697,280 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Light/NanumSquareNeoTTF-aLt.woff2` | 339,380 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Regular/NanumSquareNeoOTF-Rg.otf` | 1,669,400 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Regular/NanumSquareNeoTTF-bRg.woff` | 743,272 | 파일 크기/참조 검사 |
| `assets/font/NanumSquareNeo-Regular/NanumSquareNeoTTF-bRg.woff2` | 387,104 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Black/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Black/notokr-black-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `assets/font/NotoKR-Black/notokr-black.eot` | 149,951 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Black/notokr-black.svg` | 703,668 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Black/notokr-black.ttf` | 358,600 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Black/notokr-black.woff` | 180,348 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Black/notokr-black.woff2` | 128,720 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Black/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Black/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Black/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Black/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Bold/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Bold/notokr-bold-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `assets/font/NotoKR-Bold/notokr-bold.eot` | 156,008 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Bold/notokr-bold.svg` | 705,999 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Bold/notokr-bold.ttf` | 359,412 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Bold/notokr-bold.woff` | 185,412 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Bold/notokr-bold.woff2` | 134,968 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Bold/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Bold/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Bold/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Bold/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-DemiLight/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 173,863 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `assets/font/NotoKR-DemiLight/notokr-demilight.eot` | 155,464 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-DemiLight/notokr-demilight.svg` | 733,933 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-DemiLight/notokr-demilight.ttf` | 369,728 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-DemiLight/notokr-demilight.woff` | 187,464 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-DemiLight/notokr-demilight.woff2` | 133,772 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-DemiLight/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-DemiLight/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-DemiLight/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-DemiLight/stylesheet.css` | 547 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Light/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Light/notokr-light-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `assets/font/NotoKR-Light/notokr-light.eot` | 153,179 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Light/notokr-light.svg` | 748,368 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Light/notokr-light.ttf` | 373,820 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Light/notokr-light.woff` | 185,532 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Light/notokr-light.woff2` | 131,096 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Light/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Light/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Light/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Light/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Medium/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Medium/notokr-medium-demo.html` | 173,842 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `assets/font/NotoKR-Medium/notokr-medium.eot` | 155,800 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Medium/notokr-medium.svg` | 717,209 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Medium/notokr-medium.ttf` | 364,276 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Medium/notokr-medium.woff` | 185,440 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Medium/notokr-medium.woff2` | 133,836 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Medium/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Medium/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Medium/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Medium/stylesheet.css` | 523 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Regular/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Regular/notokr-regular-demo.html` | 173,868 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `assets/font/NotoKR-Regular/notokr-regular.eot` | 156,734 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Regular/notokr-regular.svg` | 727,332 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Regular/notokr-regular.ttf` | 367,940 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Regular/notokr-regular.woff` | 187,364 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Regular/notokr-regular.woff2` | 134,960 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Regular/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Regular/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Regular/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Regular/stylesheet.css` | 531 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Thin/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Thin/notokr-thin-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `assets/font/NotoKR-Thin/notokr-thin.eot` | 143,518 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Thin/notokr-thin.svg` | 761,397 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Thin/notokr-thin.ttf` | 377,440 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Thin/notokr-thin.woff` | 175,184 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Thin/notokr-thin.woff2` | 120,720 | 파일 크기/참조 검사 |
| `assets/font/NotoKR-Thin/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Thin/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `assets/font/NotoKR-Thin/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/font/NotoKR-Thin/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `assets/img/br/Thumbs.db` | 473,600 | 파일 크기/참조 검사 |
| `assets/img/br/bg_grid_left.png` | 58,761 | 파일 크기/참조 검사 |
| `assets/img/br/bg_grids.png` | 56,144 | 파일 크기/참조 검사 |
| `assets/img/br/future_intro_bg.jpg` | 1,355,339 | 파일 크기/참조 검사 |
| `assets/img/br/future_intro_bg.mp4` | 79,187,204 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/br/future_sub1_bg.png` | 1,613,704 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub1_cut1.png` | 1,310,146 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub1_cut2.png` | 540,947 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub1_cut3.png` | 471,528 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub1_cut4.png` | 1,669,666 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub1_m_bg.png` | 1,266,536 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub2_line.svg` | 324 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub2_process_bg.png` | 359,162 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub2_process_ico.svg` | 1,471 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub2_process_point.png` | 226,012 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub2_product_bg.png` | 734,589 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub2_product_ico.svg` | 1,710 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub2_product_point.png` | 800,954 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub3_bg.png` | 835,594 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub3_convenient.jpg` | 397,948 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub3_cost.jpg` | 200,637 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub3_easy.jpg` | 469,861 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub3_fast.jpg` | 576,268 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub3_line.svg` | 405 | 파일 크기/참조 검사 |
| `assets/img/br/future_sub3_quality.jpg` | 533,647 | 파일 크기/참조 검사 |
| `assets/img/br/m_bg_grids.png` | 14,118 | 파일 크기/참조 검사 |
| `assets/img/br/m_tech_intro_bg.jpg` | 879,761 | 파일 크기/참조 검사 |
| `assets/img/br/tech_intro_bg.jpg` | 1,593,503 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub1_hw_bg.jpg` | 816,431 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub1_sw_bg.jpg` | 781,693 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub2_circle.svg` | 6,312 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_line.svg` | 403 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_sphere.json` | 388,145 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step1_1.jpg` | 120,478 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step1_2.jpg` | 133,439 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step1_3.jpg` | 134,038 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step1_4.jpg` | 150,584 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step1_5.jpg` | 116,656 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step1_ico_c.svg` | 3,407 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step1_ico_k.svg` | 2,246 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step2_1.jpg` | 123,644 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step2_2.jpg` | 83,167 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step2_3.jpg` | 78,290 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step2_4.jpg` | 86,596 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step2_5.jpg` | 164,051 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step2_ico_c.svg` | 14,932 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step2_ico_k.svg` | 15,293 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_1.jpg` | 217,466 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_2.jpg` | 114,924 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_3.jpg` | 169,593 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_4.jpg` | 152,153 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_5.jpg` | 224,494 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_6.jpg` | 151,223 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_ico_c.svg` | 7,505 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step3_ico_k.svg` | 5,931 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step4_1.jpg` | 88,780 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step4_2.jpg` | 219,641 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step4_3.jpg` | 176,084 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step4_ico_c.svg` | 4,422 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub3_step4_ico_k.svg` | 4,428 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_bigroom.jpg` | 830,378 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_ico1.svg` | 584 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_ico2.svg` | 535 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_ico3.svg` | 722 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_ico4.svg` | 1,625 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_ico5.svg` | 1,491 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_ico6.svg` | 1,536 | 파일 크기/참조 검사 |
| `assets/img/br/tech_sub4_ico7.svg` | 1,138 | 파일 크기/참조 검사 |
| `assets/img/br/value_intro_bg_left.jpg` | 263,606 | 파일 크기/참조 검사 |
| `assets/img/br/value_intro_bg_left.png` | 760,862 | 파일 크기/참조 검사 |
| `assets/img/br/value_intro_bg_right.jpg` | 1,270,151 | 파일 크기/참조 검사 |
| `assets/img/br/value_intro_bg_right.png` | 3,016,010 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub1_ico1.svg` | 2,859 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub1_ico1_line.svg` | 20,235 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub1_ico2.svg` | 1,510 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub1_ico2_line.svg` | 20,235 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub1_ico3.svg` | 3,814 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub1_ico3_line.svg` | 20,240 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub2_our1.jpg` | 93,349 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub2_our2.jpg` | 54,231 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub2_our3.jpg` | 103,653 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub3_plan1.jpg` | 1,007,344 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub3_plan2.jpg` | 1,169,979 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub3_plan3.jpg` | 693,580 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub3_plan4.jpg` | 858,690 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub3_plan5.jpg` | 546,450 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub_bg_left.jpg` | 172,296 | 파일 크기/참조 검사 |
| `assets/img/br/value_sub_bg_right.jpg` | 443,277 | 파일 크기/참조 검사 |
| `assets/img/ci_sign_bg.png` | 29,735 | 파일 크기/참조 검사 |
| `assets/img/common_bg_left.jpg` | 130,764 | 파일 크기/참조 검사 |
| `assets/img/common_bg_right.jpg` | 474,447 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/explain_bim_more.jpg` | 2,479,314 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/explain_gis_more.jpg` | 3,977,513 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/explain_overview_more.jpg` | 1,874,289 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/explain_twin_more.jpg` | 3,001,585 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_explain_bim_more.jpg` | 1,718,508 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_explain_gis_more.jpg` | 1,807,798 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_explain_overview_more.jpg` | 829,001 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_explain_twin_more.jpg` | 1,794,016 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_sw_dir_more.jpg` | 1,197,393 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_sw_need_more.jpg` | 1,523,393 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_use_cycle_more.jpg` | 5,675,400 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/m_use_system_more.jpg` | 2,361,606 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/sw_dir_more.jpg` | 3,539,075 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/sw_need_more.jpg` | 3,529,134 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/use_cycle_more.jpg` | 6,199,916 | 파일 크기/참조 검사 |
| `assets/img/dt/bak_251103/use_end_more.jpg` | 10,000,055 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/dt/bak_251103/use_system_more.jpg` | 5,552,873 | 파일 크기/참조 검사 |
| `assets/img/dt/common_end_bg.jpg` | 170,614 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/explain_bim_more.jpg` | 2,911,085 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/explain_gis_more.jpg` | 4,341,446 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/explain_overview_more.jpg` | 1,988,842 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/explain_twin_more.jpg` | 3,370,227 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_explain_bim_more.jpg` | 2,013,567 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_explain_gis_more.jpg` | 2,121,291 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_explain_overview_more.jpg` | 899,752 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_explain_twin_more.jpg` | 2,038,347 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_sw_dir_more.jpg` | 1,356,923 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_sw_need_more.jpg` | 1,987,219 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_sw_overview_more.jpg` | 3,031,939 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_sw_toDT_more.jpg` | 1,874,848 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_use_cycle_more.jpg` | 5,409,953 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_use_end_more.jpg` | 6,902,072 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_use_overview_more.jpg` | 2,767,233 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_use_process_more.jpg` | 3,294,609 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/m_use_system_more.jpg` | 2,905,743 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/sw_dir_more.jpg` | 3,757,111 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/sw_end_obj1.png` | 2,288,169 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/sw_end_obj2.png` | 296,122 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/sw_need_more.jpg` | 3,939,758 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/sw_overview_more.jpg` | 5,420,308 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/sw_toDT_more.jpg` | 2,696,706 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/use_cycle_more.jpg` | 6,598,596 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/use_end_more.jpg` | 11,326,964 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/dt/eng/use_overview_more.jpg` | 5,486,690 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/use_process_more.jpg` | 5,620,400 | 파일 크기/참조 검사 |
| `assets/img/dt/eng/use_system_more.jpg` | 6,142,979 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_bim_more.jpg` | 2,481,660 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_bim_obj.mp4` | 7,380,528 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_bim_obj_point.png` | 254,983 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_end_obj.png` | 503,541 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_gis_more.jpg` | 4,013,742 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_gis_obj1.jpg` | 548,441 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_gis_obj2.jpg` | 545,567 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_gis_obj_point.png` | 315,498 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_intro_bg.jpg` | 5,753,170 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_line.svg` | 360 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_overview_more.jpg` | 1,824,181 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_overview_obj.jpg` | 921,702 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_twin_more.jpg` | 2,978,743 | 파일 크기/참조 검사 |
| `assets/img/dt/explain_twin_obj.mp4` | 91,177,785 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/dt/explain_twin_obj_point.png` | 345,915 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_bim_more-1.jpg` | 1,634,711 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_bim_more.jpg` | 1,709,321 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_gis_more-1.jpg` | 1,521,550 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_gis_more.jpg` | 1,822,340 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_intro_bg.jpg` | 986,566 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_overview_more-1.jpg` | 2,565,823 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_overview_more.jpg` | 791,458 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_twin_more-1.jpg` | 1,217,286 | 파일 크기/참조 검사 |
| `assets/img/dt/m_explain_twin_more.jpg` | 1,762,543 | 파일 크기/참조 검사 |
| `assets/img/dt/m_sw_dir_more.jpg` | 1,192,130 | 파일 크기/참조 검사 |
| `assets/img/dt/m_sw_intro_bg.jpg` | 529,697 | 파일 크기/참조 검사 |
| `assets/img/dt/m_sw_need_more.jpg` | 1,521,047 | 파일 크기/참조 검사 |
| `assets/img/dt/m_sw_overview_more.jpg` | 2,535,529 | 파일 크기/참조 검사 |
| `assets/img/dt/m_sw_toDT_more.jpg` | 1,630,390 | 파일 크기/참조 검사 |
| `assets/img/dt/m_use_cycle_more.jpg` | 5,017,857 | 파일 크기/참조 검사 |
| `assets/img/dt/m_use_end_more.jpg` | 5,676,112 | 파일 크기/참조 검사 |
| `assets/img/dt/m_use_intro_bg.jpg` | 604,940 | 파일 크기/참조 검사 |
| `assets/img/dt/m_use_overview_more.jpg` | 2,150,037 | 파일 크기/참조 검사 |
| `assets/img/dt/m_use_process_more.jpg` | 2,710,285 | 파일 크기/참조 검사 |
| `assets/img/dt/m_use_system_more.jpg` | 2,361,652 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_dir_more.jpg` | 3,445,342 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_dir_obj.mp4` | 10,159,393 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/dt/sw_end_obj1.png` | 687,233 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_end_obj1_bak.png` | 1,269,899 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `assets/img/dt/sw_end_obj2.png` | 212,919 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_end_obj3.png` | 77,379 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_end_obj4.png` | 25,924 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_intro_bg.jpg` | 2,467,446 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_line.svg` | 335 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_need_more.jpg` | 3,535,129 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_need_obj.mp4` | 13,515,356 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/dt/sw_need_obj_point.png` | 580,006 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_overview_more.jpg` | 4,833,865 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_overview_obj.jpg` | 1,271,708 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_toDT_more.jpg` | 2,451,665 | 파일 크기/참조 검사 |
| `assets/img/dt/sw_toDT_obj.mp4` | 8,186,380 | 파일 크기/참조 검사 |
| `assets/img/dt/use_cycle_more.jpg` | 6,199,398 | 파일 크기/참조 검사 |
| `assets/img/dt/use_cycle_obj1.jpg` | 742,876 | 파일 크기/참조 검사 |
| `assets/img/dt/use_cycle_obj2.jpg` | 707,744 | 파일 크기/참조 검사 |
| `assets/img/dt/use_cycle_obj3.jpg` | 803,547 | 파일 크기/참조 검사 |
| `assets/img/dt/use_cycle_obj4.jpg` | 715,602 | 파일 크기/참조 검사 |
| `assets/img/dt/use_cycle_obj_point.png` | 1,115,184 | 파일 크기/참조 검사 |
| `assets/img/dt/use_end_more.jpg` | 9,990,154 | 파일 크기/참조 검사 |
| `assets/img/dt/use_end_obj1.jpg` | 647,388 | 파일 크기/참조 검사 |
| `assets/img/dt/use_end_obj2.jpg` | 490,952 | 파일 크기/참조 검사 |
| `assets/img/dt/use_end_obj3.json` | 25,983 | 파일 크기/참조 검사 |
| `assets/img/dt/use_intro_bg.jpg` | 3,511,101 | 파일 크기/참조 검사 |
| `assets/img/dt/use_line.svg` | 344 | 파일 크기/참조 검사 |
| `assets/img/dt/use_overview_more.jpg` | 4,950,418 | 파일 크기/참조 검사 |
| `assets/img/dt/use_overview_obj.jpg` | 814,008 | 파일 크기/참조 검사 |
| `assets/img/dt/use_process_more.jpg` | 4,971,570 | 파일 크기/참조 검사 |
| `assets/img/dt/use_process_obj1.jpg` | 996,749 | 파일 크기/참조 검사 |
| `assets/img/dt/use_process_obj2.jpg` | 936,549 | 파일 크기/참조 검사 |
| `assets/img/dt/use_process_obj_point.png` | 785,536 | 파일 크기/참조 검사 |
| `assets/img/dt/use_system_more.jpg` | 5,550,641 | 파일 크기/참조 검사 |
| `assets/img/dt/use_system_obj.mp4` | 9,925,658 | 파일 크기/참조 검사 |
| `assets/img/dt/use_system_obj_point.png` | 320,495 | 파일 크기/참조 검사 |
| `assets/img/dt_use.html` | 9,464 | HTML: 동기 외부 스크립트 9, 이미지 4 (lazy 0), video 1, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `assets/img/dx/contents_bg.jpg` | 461,680 | 파일 크기/참조 검사 |
| `assets/img/dx/intro_bg.jpg` | 3,121,270 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p01.jpg` | 2,426,963 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p02.jpg` | 2,106,490 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p03.jpg` | 2,094,435 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p04.jpg` | 2,162,721 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p05.jpg` | 3,030,492 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p06.jpg` | 4,413,416 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p07.jpg` | 3,560,480 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p08.jpg` | 3,533,787 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p09.jpg` | 2,020,014 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p10.jpg` | 2,350,777 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p11.jpg` | 3,589,483 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p12.jpg` | 2,365,257 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p13.jpg` | 2,989,011 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p14.jpg` | 2,904,875 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p15.jpg` | 3,112,428 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p16.jpg` | 2,595,324 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p17.jpg` | 2,575,342 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p18.jpg` | 2,481,448 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p19.jpg` | 2,200,880 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p20.jpg` | 2,593,706 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p21.jpg` | 2,728,788 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p22.jpg` | 2,625,651 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p23.jpg` | 2,687,829 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p24.jpg` | 2,326,944 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p25.jpg` | 2,441,163 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p26.jpg` | 2,218,464 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p27.jpg` | 2,047,832 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p28.jpg` | 2,968,494 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p29.jpg` | 2,808,375 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p30.jpg` | 2,246,656 | 파일 크기/참조 검사 |
| `assets/img/dx/poster_p31.jpg` | 2,187,581 | 파일 크기/참조 검사 |
| `assets/img/eng/logo_c.svg` | 6,123 | 파일 크기/참조 검사 |
| `assets/img/eng/logo_w.svg` | 9,591 | 파일 크기/참조 검사 |
| `assets/img/favicon.ico` | 107,620 | 파일 크기/참조 검사 |
| `assets/img/flipbook_corner.png` | 83,702 | 파일 크기/참조 검사 |
| `assets/img/ico_angle.svg` | 243 | 파일 크기/참조 검사 |
| `assets/img/ico_arrow.svg` | 169 | 파일 크기/참조 검사 |
| `assets/img/ico_back.svg` | 668 | 파일 크기/참조 검사 |
| `assets/img/ico_blank.svg` | 473 | 파일 크기/참조 검사 |
| `assets/img/ico_close.svg` | 540 | 파일 크기/참조 검사 |
| `assets/img/ico_close_r.svg` | 856 | 파일 크기/참조 검사 |
| `assets/img/ico_home.svg` | 191 | 파일 크기/참조 검사 |
| `assets/img/ico_language.svg` | 1,533 | 파일 크기/참조 검사 |
| `assets/img/ico_language_w.svg` | 1,533 | 파일 크기/참조 검사 |
| `assets/img/ico_mail.svg` | 923 | 파일 크기/참조 검사 |
| `assets/img/ico_more.svg` | 2,111 | 파일 크기/참조 검사 |
| `assets/img/ico_more_hover.svg` | 2,114 | 파일 크기/참조 검사 |
| `assets/img/index.mp4` | 118,043,547 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/index_bak.mp4` | 122,325,602 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `assets/img/logo.svg` | 3,139 | 파일 크기/참조 검사 |
| `assets/img/logo_c.svg` | 5,994 | 파일 크기/참조 검사 |
| `assets/img/logo_w.svg` | 5,970 | 파일 크기/참조 검사 |
| `assets/img/mask_tail.svg` | 261 | 파일 크기/참조 검사 |
| `assets/img/og-main-thumb_baron.JPG` | 237,335 | 파일 크기/참조 검사 |
| `assets/img/pr/bro_baron.png` | 713,701 | 파일 크기/참조 검사 |
| `assets/img/pr/bro_hanmac.png` | 209,733 | 파일 크기/참조 검사 |
| `assets/img/pr/brochure_sub1_bg.png` | 5,841,607 | 파일 크기/참조 검사 |
| `assets/img/pr/ci_color_bg.png` | 304,045 | 파일 크기/참조 검사 |
| `assets/img/pr/ci_sec_bg.png` | 155,234 | 파일 크기/참조 검사 |
| `assets/img/pr/ci_sign_bg.png` | 29,735 | 파일 크기/참조 검사 |
| `assets/img/pr/ico_bro_btn.svg` | 2,089 | 파일 크기/참조 검사 |
| `assets/img/pr/ico_bro_hover_btn.svg` | 2,089 | 파일 크기/참조 검사 |
| `assets/img/pr/ico_ci_btn.svg` | 621 | 파일 크기/참조 검사 |
| `assets/img/pr/ico_next_view.svg` | 246 | 파일 크기/참조 검사 |
| `assets/img/pr/ico_prev_view.svg` | 246 | 파일 크기/참조 검사 |
| `assets/img/pr/logo_en_h.svg` | 10,307 | 파일 크기/참조 검사 |
| `assets/img/pr/logo_en_w.svg` | 10,146 | 파일 크기/참조 검사 |
| `assets/img/pr/logo_kr_h.svg` | 6,234 | 파일 크기/참조 검사 |
| `assets/img/pr/logo_kr_w.svg` | 6,051 | 파일 크기/참조 검사 |
| `assets/img/pr/mo/mo_bro_bg.png` | 683,085 | 파일 크기/참조 검사 |
| `assets/img/pr/mo/mo_news_bn_01.png` | 224,168 | 파일 크기/참조 검사 |
| `assets/img/pr/mo/news_intro_bg.svg` | 238 | 파일 크기/참조 검사 |
| `assets/img/pr/news_bn_01.png` | 133,539 | 파일 크기/참조 검사 |
| `assets/img/pr/news_bottom_bg.png` | 95,716 | 파일 크기/참조 검사 |
| `assets/img/pr/news_img_251127.jpg` | 98,986 | 파일 크기/참조 검사 |
| `assets/img/pr/news_img_260121.png` | 489,474 | 파일 크기/참조 검사 |
| `assets/img/pr/news_img_260519.jpg` | 365,358 | 파일 크기/참조 검사 |
| `assets/img/pr/news_img_260527.jpg` | 460,198 | 파일 크기/참조 검사 |
| `assets/img/pr/news_intro_line.png` | 608,674 | 파일 크기/참조 검사 |
| `assets/img/pr/news_intro_line.svg` | 11,766,600 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/pr/news_intro_mask.svg` | 378 | 파일 크기/참조 검사 |
| `assets/img/pr/pr_intro_bg.png` | 953,576 | 파일 크기/참조 검사 |
| `assets/img/recruit/Group 1171280821.svg` | 5,917 | 파일 크기/참조 검사 |
| `assets/img/recruit/bg_recruit_apply.png` | 755,513 | 파일 크기/참조 검사 |
| `assets/img/recruit/bg_recruit_faq.png` | 832,305 | 파일 크기/참조 검사 |
| `assets/img/recruit/bg_report_design.png` | 287,426 | 파일 크기/참조 검사 |
| `assets/img/recruit/bg_report_developer.png` | 286,664 | 파일 크기/참조 검사 |
| `assets/img/recruit/bg_report_engineer.png` | 264,323 | 파일 크기/참조 검사 |
| `assets/img/recruit/bg_report_management.png` | 257,881 | 파일 크기/참조 검사 |
| `assets/img/recruit/bg_review_grid.png` | 10,164 | 파일 크기/참조 검사 |
| `assets/img/recruit/img_apply_pop.png` | 18,093 | 파일 크기/참조 검사 |
| `assets/img/recruit/logo.svg` | 8,211 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_bg_recruit_apply.jpg` | 194,385 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_bg_recruit_faq.jpg` | 306,038 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_bg_report_design.png` | 435,065 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_bg_report_developer.png` | 406,183 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_bg_report_engineer.png` | 335,610 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_bg_report_management.png` | 381,474 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_recruit_sub1_wayobj.png` | 584,594 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_recruit_sub2_obj.png` | 153,296 | 파일 크기/참조 검사 |
| `assets/img/recruit/m_recruit_way_more.jpg` | 2,110,486 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_info_img01.png` | 55,900 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_info_img02.png` | 5,855 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_info_img02.svg` | 261,682 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_img01.jpg` | 3,757,612 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_img01.png` | 9,671,125 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_img02.jpg` | 4,212,157 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_img02.png` | 10,872,656 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/recruit/recruit_intro_img03.jpg` | 2,416,408 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_img03.png` | 6,704,687 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_img04.jpg` | 2,874,639 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_img04.png` | 9,395,020 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_intro_line.svg` | 475 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_bg.png` | 123,882 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_ico_arrow.svg` | 987 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live01_ico01.svg` | 1,264 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live01_ico02.svg` | 699 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live01_ico03.svg` | 4,150 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live01_ico04.svg` | 2,539 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live02_ico01.svg` | 1,376 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live02_ico02.svg` | 1,578 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live02_ico03.svg` | 1,528 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live03_ico01.svg` | 3,057 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live03_ico02.svg` | 3,683 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live03_ico03.svg` | 1,877 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live03_ico04.svg` | 2,828 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live_ico01.png` | 32,769 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live_ico01.svg` | 4,247 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live_ico02.png` | 30,386 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live_ico02.svg` | 4,135 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live_ico03.png` | 33,716 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_live_ico03.svg` | 7,125 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_livebg.png` | 1,852,542 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_waybg.png` | 244,121 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_wayobj.png` | 517,911 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub1_workbg.png` | 1,950,017 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_copybg.png` | 327,147 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_ico_wordclose.svg` | 1,470 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_ico_wordopen.svg` | 1,422 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_obj.png` | 159,577 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_profile01.png` | 10,123 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_profile02.png` | 12,354 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_profile03.png` | 11,857 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_profile04.png` | 12,147 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub2_profile05.png` | 10,424 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub3_bg_line.png` | 318 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub3_ico_step01.svg` | 3,213 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub3_ico_step02.svg` | 2,790 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub3_ico_step03.svg` | 2,968 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub3_ico_step04.svg` | 5,277 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_sub3_ico_step05.svg` | 2,579 | 파일 크기/참조 검사 |
| `assets/img/recruit/recruit_way_more.jpg` | 3,714,624 | 파일 크기/참조 검사 |
| `assets/img/sv/Frame 1171281754.jpg` | 12,216,699 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/bak_251103/m_solution_construction_more.jpg` | 5,937,159 | 파일 크기/참조 검사 |
| `assets/img/sv/bak_251103/solution_construction_more.jpg` | 6,109,828 | 파일 크기/참조 검사 |
| `assets/img/sv/bg_sw_package.png` | 503,025 | 파일 크기/참조 검사 |
| `assets/img/sv/bg_sw_package_1.png` | 45,594 | 파일 크기/참조 검사 |
| `assets/img/sv/bg_sw_package_2.png` | 42,675 | 파일 크기/참조 검사 |
| `assets/img/sv/bg_sw_package_3.png` | 26,755 | 파일 크기/참조 검사 |
| `assets/img/sv/bg_sw_package_4.png` | 38,025 | 파일 크기/참조 검사 |
| `assets/img/sv/bg_sw_package_5.png` | 48,704 | 파일 크기/참조 검사 |
| `assets/img/sv/bg_sw_package_6.png` | 32,830 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_infra_more.jpg` | 3,988,111 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_infra_obj1.jpg` | 733,754 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_infra_obj2.jpg` | 1,504,602 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_infra_obj_point.png` | 439,480 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_intro_bg.jpg` | 3,766,486 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_line.svg` | 319 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_overview_more.jpg` | 3,279,206 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_overview_obj.jpg` | 1,217,167 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_overview_obj_point.png` | 435,049 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_real_more.jpg` | 12,216,704 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/bigroom_real_obj1.jpg` | 1,222,833 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_real_obj2.jpg` | 1,194,928 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_real_obj3-1.jpg` | 1,341,649 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_real_obj3.jpg` | 1,178,461 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_real_obj4.jpg` | 1,341,649 | 파일 크기/참조 검사 |
| `assets/img/sv/bigroom_real_obj_point.png` | 582,096 | 파일 크기/참조 검사 |
| `assets/img/sv/common_bg_grid.png` | 265,676 | 파일 크기/참조 검사 |
| `assets/img/sv/common_intro_mask.svg` | 242 | 파일 크기/참조 검사 |
| `assets/img/sv/common_obj_bg.png` | 231,218 | 파일 크기/참조 검사 |
| `assets/img/sv/common_obj_bg.svg` | 11,766,461 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/common_obj_mask_left.svg` | 475 | 파일 크기/참조 검사 |
| `assets/img/sv/common_obj_mask_right.svg` | 480 | 파일 크기/참조 검사 |
| `assets/img/sv/common_road.svg` | 4,450 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/bigroom_infra_more.jpg` | 4,141,270 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/bigroom_infra_obj_point.png` | 1,426,676 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/bigroom_overview_more.jpg` | 3,715,474 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/bigroom_real_more.jpg` | 12,716,165 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/eng/m_bigroom_infra_more.jpg` | 1,741,017 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/m_bigroom_overview_more.jpg` | 2,355,891 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/m_bigroom_real_more.jpg` | 5,724,713 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/m_solution_construction_more.jpg` | 6,466,080 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/m_solution_design_more.jpg` | 6,910,592 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/m_solution_op_more.jpg` | 4,869,370 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/solution_construction_more.jpg` | 16,165,759 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/eng/solution_design_more.jpg` | 10,215,220 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/eng/solution_design_obj_point.png` | 275,935 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/solution_end_obj.png` | 3,078,965 | 파일 크기/참조 검사 |
| `assets/img/sv/eng/solution_op_more.jpg` | 11,896,048 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/img_apply_pop.png` | 6,151 | 파일 크기/참조 검사 |
| `assets/img/sv/m_bigroom_infra_more.jpg` | 1,546,994 | 파일 크기/참조 검사 |
| `assets/img/sv/m_bigroom_intro_bg.jpg` | 1,563,497 | 파일 크기/참조 검사 |
| `assets/img/sv/m_bigroom_overview_more.jpg` | 1,663,795 | 파일 크기/참조 검사 |
| `assets/img/sv/m_bigroom_real_more.jpg` | 4,909,441 | 파일 크기/참조 검사 |
| `assets/img/sv/m_common_intro_mask.svg` | 238 | 파일 크기/참조 검사 |
| `assets/img/sv/m_solution_construction_more.jpg` | 4,490,567 | 파일 크기/참조 검사 |
| `assets/img/sv/m_solution_design_more.jpg` | 6,268,857 | 파일 크기/참조 검사 |
| `assets/img/sv/m_solution_intro_bg.jpg` | 733,784 | 파일 크기/참조 검사 |
| `assets/img/sv/m_solution_op_more.jpg` | 5,920,368 | 파일 크기/참조 검사 |
| `assets/img/sv/m_sw_intro_bg.jpg` | 583,518 | 파일 크기/참조 검사 |
| `assets/img/sv/m_sw_intro_bg_bak_251103.jpg` | 539,959 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `assets/img/sv/solution_construction_more.jpg` | 15,356,842 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/solution_construction_obj1.jpg` | 1,589,621 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_construction_obj2.jpg` | 1,613,631 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_construction_obj_point.png` | 589,684 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_design_more.jpg` | 9,462,743 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_design_obj.mp4` | 5,611,529 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_design_obj_point.png` | 271,311 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_end_obj.png` | 1,459,389 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_intro_bg.jpg` | 1,778,359 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_line.svg` | 313 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_op_more.jpg` | 11,368,362 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `assets/img/sv/solution_op_more_v1.mp4` | 5,611,529 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_op_more_v2.mp4` | 5,611,529 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_op_more_v3.mp4` | 5,611,529 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_op_more_v4.mp4` | 5,611,529 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_op_obj1.jpg` | 1,458,233 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_op_obj2.jpg` | 1,423,261 | 파일 크기/참조 검사 |
| `assets/img/sv/solution_op_obj_point.png` | 523,992 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_egbim_obj.jpg` | 973,870 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_egbim_obj_point.png` | 321,838 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_end_bg.jpg` | 981,281 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_gaia_obj.jpg` | 1,236,386 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_gaia_obj_point.png` | 719,509 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_intro_bg.jpg` | 6,402,178 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_ipipe_obj.jpg` | 2,146,642 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_ipipe_obj_point.png` | 665,668 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_kngil_more.pdf` | 5,120,061 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_kngil_obj.jpg` | 1,809,577 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_kngil_obj_point.png` | 405,434 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_line.svg` | 393 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_bg1.jpg` | 173,195 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_bg2.png` | 1,165,971 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_egbim.jpg` | 167,039 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_gaia.jpg` | 180,847 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_ipipe.jpg` | 123,771 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_kngil.jpg` | 152,210 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_pq.jpg` | 86,264 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_list_tova.jpg` | 171,920 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_pq_obj.jpg` | 2,382,114 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_pq_obj_point.png` | 390,436 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_tova_obj.jpg` | 2,458,523 | 파일 크기/참조 검사 |
| `assets/img/sv/sw_tova_obj_point.png` | 485,074 | 파일 크기/참조 검사 |
| `assets/js/StickyOnTable.js` | 5,296 | 텍스트 리소스 참조 검사 |
| `assets/js/apply.js` | 13,732 | 텍스트 리소스 참조 검사 |
| `assets/js/br.js` | 19,953 | 텍스트 리소스 참조 검사 |
| `assets/js/common.js` | 12,289 | 텍스트 리소스 참조 검사 |
| `assets/js/common_eng.js` | 10,131 | 텍스트 리소스 참조 검사 |
| `assets/js/dt.js` | 22,720 | 텍스트 리소스 참조 검사 |
| `assets/js/dx.js` | 23,991 | 텍스트 리소스 참조 검사 |
| `assets/js/dx_250612.js` | 16,613 | 텍스트 리소스 참조 검사; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `assets/js/egbim-baron-shell.js` | 45,654 | 텍스트 리소스 참조 검사 |
| `assets/js/eng/common.js` | 9,886 | 텍스트 리소스 참조 검사 |
| `assets/js/eng/dt.js` | 22,013 | 텍스트 리소스 참조 검사 |
| `assets/js/eng/dx.js` | 24,093 | 텍스트 리소스 참조 검사 |
| `assets/js/eng/pr.js` | 5,701 | 텍스트 리소스 참조 검사 |
| `assets/js/eng/sv.js` | 12,599 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `assets/js/faq.js` | 4,915 | 텍스트 리소스 참조 검사 |
| `assets/js/gaia/common.js` | 28,463 | 텍스트 리소스 참조 검사; 외부 URL 5, 로컬 참조 확인 필요 0 |
| `assets/js/lib/MotionPathPlugin.min.js` | 21,624 | 텍스트 리소스 참조 검사 |
| `assets/js/lib/aos.min.js` | 14,239 | 텍스트 리소스 참조 검사 |
| `assets/js/lib/gsap.min.js` | 72,223 | 텍스트 리소스 참조 검사 |
| `assets/js/lib/jquery-3.6.1.min.js` | 89,664 | 텍스트 리소스 참조 검사 |
| `assets/js/lib/lenis.min.js` | 13,619 | 텍스트 리소스 참조 검사 |
| `assets/js/lib/lottie.min.js` | 256,032 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 14 |
| `assets/js/lib/scrollToPlugin.min.js` | 4,047 | 텍스트 리소스 참조 검사 |
| `assets/js/lib/scrolltrigger.min.js` | 43,389 | 텍스트 리소스 참조 검사 |
| `assets/js/lib/swiper11.min.js` | 153,623 | 텍스트 리소스 참조 검사 |
| `assets/js/pr.js` | 5,701 | 텍스트 리소스 참조 검사 |
| `assets/js/recruit.js` | 6,977 | 텍스트 리소스 참조 검사 |
| `assets/js/recruit_view.js` | 8,820 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 4 |
| `assets/js/sv.js` | 12,584 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `backup_commit.zip` | 165,702,048 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `callback.html` | 214 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0 |
| `callback/index.html` | 214 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0 |
| `cloudflare-r2-deployment-guide.md` | 15,230 | 파일 크기/참조 검사 |
| `en/.container {.css` | 1,344 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `en/br_future.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/br_future_bak_250610.html` | 9,673 | HTML: 동기 외부 스크립트 7, 이미지 10 (lazy 0), video 1, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/br_future_bak_251103.html` | 13,849 | HTML: 동기 외부 스크립트 7, 이미지 10 (lazy 0), video 1, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/br_tech.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/br_tech_bak_251103.html` | 14,135 | HTML: 동기 외부 스크립트 8, 이미지 28 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/br_value.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/dt_explain.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/dt_sw.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/dt_use.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/dx.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/dx_250612.html` | 4,186 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0 |
| `en/egbim/buy.html` | 4,105 | HTML: 동기 외부 스크립트 8, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 9, 로컬 참조 확인 필요 2 |
| `en/egbim/css/default.css` | 0 | 텍스트 리소스 참조 검사 |
| `en/egbim/css/default_shop.css` | 88,628 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `en/egbim/css/font.css` | 1,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `en/egbim/css/mobile.css` | 22,838 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `en/egbim/css/mobile_shop.css` | 74,767 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/css/reset.css` | 2,193 | 텍스트 리소스 참조 검사 |
| `en/egbim/css/slickslider/slick-theme.css` | 3,349 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `en/egbim/css/slickslider/slick.css` | 1,895 | 텍스트 리소스 참조 검사 |
| `en/egbim/css/stickyOnTable.css` | 497 | 텍스트 리소스 참조 검사 |
| `en/egbim/css/style.css` | 228,482 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `en/egbim/css/style_260526.css` | 228,038 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/floorplan.html` | 15,121 | HTML: 동기 외부 스크립트 9, 이미지 27 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Black/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Black/notokr-black-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/egbim/font/NotoKR-Black/notokr-black.eot` | 149,951 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Black/notokr-black.svg` | 703,668 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Black/notokr-black.ttf` | 358,600 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Black/notokr-black.woff` | 180,348 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Black/notokr-black.woff2` | 128,720 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Black/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Black/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Black/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Black/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Bold/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Bold/notokr-bold-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/egbim/font/NotoKR-Bold/notokr-bold.eot` | 156,008 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Bold/notokr-bold.svg` | 705,999 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Bold/notokr-bold.ttf` | 359,412 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Bold/notokr-bold.woff` | 185,412 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Bold/notokr-bold.woff2` | 134,968 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Bold/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Bold/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Bold/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Bold/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-DemiLight/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 173,863 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/egbim/font/NotoKR-DemiLight/notokr-demilight.eot` | 155,464 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/notokr-demilight.svg` | 733,933 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/notokr-demilight.ttf` | 369,728 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/notokr-demilight.woff` | 187,464 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/notokr-demilight.woff2` | 133,772 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-DemiLight/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-DemiLight/stylesheet.css` | 547 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Light/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Light/notokr-light-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/egbim/font/NotoKR-Light/notokr-light.eot` | 153,179 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Light/notokr-light.svg` | 748,368 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Light/notokr-light.ttf` | 373,820 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Light/notokr-light.woff` | 185,532 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Light/notokr-light.woff2` | 131,096 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Light/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Light/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Light/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Light/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Medium/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Medium/notokr-medium-demo.html` | 173,842 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/egbim/font/NotoKR-Medium/notokr-medium.eot` | 155,800 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Medium/notokr-medium.svg` | 717,209 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Medium/notokr-medium.ttf` | 364,276 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Medium/notokr-medium.woff` | 185,440 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Medium/notokr-medium.woff2` | 133,836 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Medium/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Medium/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Medium/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Medium/stylesheet.css` | 523 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Regular/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Regular/notokr-regular-demo.html` | 173,868 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/egbim/font/NotoKR-Regular/notokr-regular.eot` | 156,734 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Regular/notokr-regular.svg` | 727,332 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Regular/notokr-regular.ttf` | 367,940 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Regular/notokr-regular.woff` | 187,364 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Regular/notokr-regular.woff2` | 134,960 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Regular/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Regular/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Regular/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Regular/stylesheet.css` | 531 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Thin/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Thin/notokr-thin-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/egbim/font/NotoKR-Thin/notokr-thin.eot` | 143,518 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Thin/notokr-thin.svg` | 761,397 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Thin/notokr-thin.ttf` | 377,440 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Thin/notokr-thin.woff` | 175,184 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Thin/notokr-thin.woff2` | 120,720 | 파일 크기/참조 검사 |
| `en/egbim/font/NotoKR-Thin/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Thin/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/egbim/font/NotoKR-Thin/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/font/NotoKR-Thin/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/forbim.html` | 7,588 | HTML: 동기 외부 스크립트 9, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/egbim/img/EGBIM_buy.mp4` | 42,045,445 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/Subtract2.svg` | 1,693 | 파일 크기/참조 검사 |
| `en/egbim/img/Thumbs.db` | 338,944 | 파일 크기/참조 검사 |
| `en/egbim/img/arrow_r.svg` | 167 | 파일 크기/참조 검사 |
| `en/egbim/img/asset_search.svg` | 1,658 | 파일 크기/참조 검사 |
| `en/egbim/img/atom_line.svg` | 1,525 | 파일 크기/참조 검사 |
| `en/egbim/img/atom_obj.svg` | 1,936 | 파일 크기/참조 검사 |
| `en/egbim/img/baron_logo.svg` | 6,233 | 파일 크기/참조 검사 |
| `en/egbim/img/baron_logo_eng.svg` | 9,591 | 파일 크기/참조 검사 |
| `en/egbim/img/bg_close.png` | 898 | 파일 크기/참조 검사 |
| `en/egbim/img/bg_pop.png` | 1,795,801 | 파일 크기/참조 검사 |
| `en/egbim/img/block_img_01.png` | 51,252 | 파일 크기/참조 검사 |
| `en/egbim/img/block_img_02.png` | 76,112 | 파일 크기/참조 검사 |
| `en/egbim/img/block_img_ico.svg` | 4,910 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_end.gif` | 1,176 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_first.gif` | 1,885 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_idx_left.png` | 3,141 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_idx_right.png` | 442 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_next.gif` | 1,169 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_prev.gif` | 1,873 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_search.jpg` | 782 | 파일 크기/참조 검사 |
| `en/egbim/img/btn_top.gif` | 1,178 | 파일 크기/참조 검사 |
| `en/egbim/img/bullet.gif` | 1,165 | 파일 크기/참조 검사 |
| `en/egbim/img/buy_intro_bg.png` | 1,186,792 | 파일 크기/참조 검사 |
| `en/egbim/img/captcha.png` | 4,886 | 파일 크기/참조 검사 |
| `en/egbim/img/captcha2.png` | 4,886 | 파일 크기/참조 검사 |
| `en/egbim/img/chk.png` | 1,070 | 파일 크기/참조 검사 |
| `en/egbim/img/close_btn.gif` | 1,209 | 파일 크기/참조 검사 |
| `en/egbim/img/close_btn.png` | 1,147 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/Thumbs.db` | 522,752 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_1.png` | 729,470 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_10.png` | 361,340 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_100.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_101.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_102.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_103.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_104.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_11.png` | 145,644 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_12.png` | 14,091 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_13.png` | 17,110 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_14.png` | 92,527 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_15.png` | 144,244 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_16.png` | 188,767 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_17.png` | 221,944 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_18.png` | 254,233 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_19.png` | 317,194 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_2.png` | 727,547 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_20.png` | 397,369 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_21.png` | 468,221 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_22.png` | 502,992 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_23.png` | 503,362 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_24.png` | 500,551 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_25.png` | 500,422 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_26.png` | 503,390 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_27.png` | 502,812 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_28.png` | 503,077 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_29.png` | 541,028 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_3.png` | 729,358 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_30.png` | 549,525 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_31.png` | 549,041 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_32.png` | 550,112 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_33.png` | 554,641 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_34.png` | 559,102 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_35.png` | 558,365 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_36.png` | 559,487 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_37.png` | 560,431 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_38.png` | 558,668 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_39.png` | 558,298 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_4.png` | 728,233 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_40.png` | 559,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_41.png` | 607,476 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_42.png` | 662,486 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_43.png` | 720,297 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_44.png` | 780,145 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_45.png` | 851,441 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_46.png` | 914,471 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_47.png` | 953,623 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_48.png` | 962,638 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_49.png` | 962,638 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_5.png` | 705,944 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_50.png` | 962,638 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_51.png` | 962,638 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_52.png` | 1,049,340 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_53.png` | 1,138,471 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_54.png` | 1,197,889 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_55.png` | 1,233,019 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_56.png` | 1,259,825 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_57.png` | 1,311,789 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_58.png` | 1,357,885 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_59.png` | 1,366,900 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_6.png` | 662,210 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_60.png` | 1,350,101 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_61.png` | 1,288,616 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_62.png` | 1,223,769 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_63.png` | 1,232,384 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_64.png` | 1,240,668 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_65.png` | 1,241,184 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_66.png` | 1,240,533 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_67.png` | 1,239,298 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_68.png` | 1,240,688 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_69.png` | 1,241,242 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_7.png` | 607,289 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_70.png` | 1,243,732 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_71.png` | 1,252,218 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_72.png` | 1,252,668 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_73.png` | 1,251,460 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_74.png` | 1,248,539 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_75.png` | 1,243,890 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_76.png` | 1,239,844 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_77.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_78.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_79.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_8.png` | 543,705 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_80.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_81.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_82.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_83.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_84.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_85.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_86.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_87.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_88.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_89.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_9.png` | 451,356 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_90.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_91.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_92.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_93.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_94.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_95.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_96.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_97.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_98.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/comp_99.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_1.png` | 719,887 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_10.png` | 353,905 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_100.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_101.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_102.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_103.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_104.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_11.png` | 138,751 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_12.png` | 14,091 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_13.png` | 17,110 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_14.png` | 94,354 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_15.png` | 136,539 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_16.png` | 172,152 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_17.png` | 196,026 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_18.png` | 226,995 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_19.png` | 291,966 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_2.png` | 718,214 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_20.png` | 377,017 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_21.png` | 450,658 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_22.png` | 486,573 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_23.png` | 485,564 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_24.png` | 483,575 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_25.png` | 483,091 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_26.png` | 485,020 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_27.png` | 484,627 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_28.png` | 484,314 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_29.png` | 513,816 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_3.png` | 720,185 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_30.png` | 521,341 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_31.png` | 521,983 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_32.png` | 523,907 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_33.png` | 527,533 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_34.png` | 530,433 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_35.png` | 530,644 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_36.png` | 530,752 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_37.png` | 530,451 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_38.png` | 530,201 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_39.png` | 528,876 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_4.png` | 718,688 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_40.png` | 529,577 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_41.png` | 578,311 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_42.png` | 632,326 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_43.png` | 691,664 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_44.png` | 750,070 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_45.png` | 822,409 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_46.png` | 885,935 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_47.png` | 924,643 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_48.png` | 933,337 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_49.png` | 933,337 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_5.png` | 696,182 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_50.png` | 933,337 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_51.png` | 933,337 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_52.png` | 1,018,986 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_53.png` | 1,105,615 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_54.png` | 1,167,019 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_55.png` | 1,202,205 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_56.png` | 1,228,821 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_57.png` | 1,282,679 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_58.png` | 1,328,125 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_59.png` | 1,339,815 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_6.png` | 652,972 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_60.png` | 1,324,725 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_61.png` | 1,268,155 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_62.png` | 1,208,699 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_63.png` | 1,216,217 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_64.png` | 1,224,438 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_65.png` | 1,224,834 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_66.png` | 1,225,298 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_67.png` | 1,223,296 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_68.png` | 1,223,801 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_69.png` | 1,224,725 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_7.png` | 599,667 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_70.png` | 1,227,958 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_71.png` | 1,236,227 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_72.png` | 1,236,625 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_73.png` | 1,235,399 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_74.png` | 1,232,301 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_75.png` | 1,227,325 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_76.png` | 1,223,203 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_77.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_78.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_79.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_8.png` | 537,125 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_80.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_81.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_82.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_83.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_84.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_85.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_86.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_87.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_88.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_89.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_9.png` | 443,417 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_90.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_91.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_92.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_93.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_94.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_95.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_96.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_97.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_98.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/com_img/eng/comp_99.png` | 1,221,411 | 파일 크기/참조 검사 |
| `en/egbim/img/dia_valuebg01.png` | 730,776 | 파일 크기/참조 검사 |
| `en/egbim/img/dia_valuebg02.png` | 3,809,536 | 파일 크기/참조 검사 |
| `en/egbim/img/dia_valuebg03.png` | 195,168 | 파일 크기/참조 검사 |
| `en/egbim/img/dual_img01_01.png` | 75,739 | 파일 크기/참조 검사 |
| `en/egbim/img/dual_img01_02.png` | 60,751 | 파일 크기/참조 검사 |
| `en/egbim/img/dual_img02_01.png` | 108,269 | 파일 크기/참조 검사 |
| `en/egbim/img/dual_img02_02.png` | 33,746 | 파일 크기/참조 검사 |
| `en/egbim/img/eee.svg` | 10,775 | 파일 크기/참조 검사 |
| `en/egbim/img/egbim_k.svg` | 2,690 | 파일 크기/참조 검사 |
| `en/egbim/img/egbim_logo.svg` | 13,099 | 파일 크기/참조 검사 |
| `en/egbim/img/egbim_obj_k.svg` | 715 | 파일 크기/참조 검사 |
| `en/egbim/img/egbim_obj_w.svg` | 698 | 파일 크기/참조 검사 |
| `en/egbim/img/egbim_w.svg` | 4,791 | 파일 크기/참조 검사 |
| `en/egbim/img/faq_intro_bg.png` | 933,519 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_01.png` | 122,202 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_01_01.svg` | 210,524 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_02.png` | 196,677 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_02_01.png` | 138,549 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_03.png` | 994,848 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_03_01.png` | 424,384 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_03_02.png` | 56,224 | 파일 크기/참조 검사 |
| `en/egbim/img/find_img_03_02_bak.png` | 20,071 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/img/find_img_03_03.png` | 31,134 | 파일 크기/참조 검사 |
| `en/egbim/img/floating_bg.png` | 50,554 | 파일 크기/참조 검사 |
| `en/egbim/img/floating_bg2.png` | 40,051 | 파일 크기/참조 검사 |
| `en/egbim/img/floating_bg_4.png` | 30,679 | 파일 크기/참조 검사 |
| `en/egbim/img/floating_bg_r2.png` | 23,992 | 파일 크기/참조 검사 |
| `en/egbim/img/floating_bg_r4.png` | 24,497 | 파일 크기/참조 검사 |
| `en/egbim/img/floating_bg_row4.png` | 24,497 | 파일 크기/참조 검사 |
| `en/egbim/img/floorplan_01.png` | 1,496,234 | 파일 크기/참조 검사 |
| `en/egbim/img/floorplan_02.png` | 379,594 | 파일 크기/참조 검사 |
| `en/egbim/img/floorplan_03.png` | 421,584 | 파일 크기/참조 검사 |
| `en/egbim/img/floorplan_intro_bg.png` | 409,923 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_intro_bg.png` | 3,164,915 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_process_01_1.png` | 142,533 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_process_01_2.png` | 252,994 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_process_01_3.png` | 137,277 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_process_02.png` | 270,863 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_process_bg.png` | 649,084 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_process_bg02.png` | 2,977,942 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_theorys_bg.png` | 1,051,872 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_theorys_bim.svg` | 5,157 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_theorys_plan.svg` | 8,382 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_visual.png` | 2,279,956 | 파일 크기/참조 검사 |
| `en/egbim/img/forbim_visual_bg.png` | 317,387 | 파일 크기/참조 검사 |
| `en/egbim/img/ft.png` | 3,204 | 파일 크기/참조 검사 |
| `en/egbim/img/ft_logo.png` | 3,737 | 파일 크기/참조 검사 |
| `en/egbim/img/gnb_bg.gif` | 1,169 | 파일 크기/참조 검사 |
| `en/egbim/img/gnb_bg00.gif` | 54 | 파일 크기/참조 검사 |
| `en/egbim/img/gnb_bg01.gif` | 54 | 파일 크기/참조 검사 |
| `en/egbim/img/gnb_bg2.gif` | 49 | 파일 크기/참조 검사 |
| `en/egbim/img/ico-default-naverpay.png` | 2,689 | 파일 크기/참조 검사 |
| `en/egbim/img/ico-mobile-applepay.png` | 2,063 | 파일 크기/참조 검사 |
| `en/egbim/img/ico-mobile-kakaopay.png` | 3,251 | 파일 크기/참조 검사 |
| `en/egbim/img/ico-mobile-naverpay.png` | 3,261 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_admin.svg` | 5,691 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_angle.svg` | 243 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_answer.svg` | 296 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_arrow.svg` | 488 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_buy_alarm.svg` | 929 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_buy_ask.svg` | 2,054 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_buy_brochure.svg` | 2,196 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_buy_mail.svg` | 585 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_buy_manual.svg` | 1,638 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_buy_tel.svg` | 1,093 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_cafe.svg` | 1,171 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_check.svg` | 900 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_close.svg` | 196 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_company.svg` | 887 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_complete.svg` | 1,088 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_email.svg` | 1,146 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_facebook.svg` | 952 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_find_01.svg` | 1,317 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_find_02.svg` | 2,042 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_find_03.svg` | 1,168 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_find_tri.svg` | 193 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_book.svg` | 3,903 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_book_on.svg` | 3,905 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_buy.svg` | 651 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_buy_on.svg` | 654 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_download.svg` | 678 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_download_on.svg` | 680 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_faq.svg` | 1,173 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floating_faq_on.svg` | 1,171 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floorplan_dia_01.svg` | 1,969 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floorplan_dia_02.svg` | 2,992 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_floorplan_dia_03.svg` | 2,363 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_footer_close.svg` | 333 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_forbim_check.svg` | 3,003 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_forbim_link.svg` | 3,292 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_ham.svg` | 309 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_id.svg` | 1,018 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_info_01.svg` | 4,159 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_info_02.svg` | 1,767 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_language.svg` | 1,324 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_link.svg` | 791 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_link_b.svg` | 789 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_lock.svg` | 1,609 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_my.svg` | 888 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_pg_left.svg` | 1,056 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_pg_right.svg` | 1,046 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_phone.svg` | 727 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_print_01.svg` | 919 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_print_02.svg` | 1,225 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_pripary_civil.svg` | 1,209 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_pripary_command.svg` | 3,764 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_pripary_my.svg` | 4,678 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_pw.svg` | 1,185 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_send_email.svg` | 634 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_signout.svg` | 933 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_upload.svg` | 323 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_userlist.svg` | 375 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_bim_k.svg` | 4,979 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_bim_w.svg` | 4,972 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_floorplan_k.svg` | 1,763 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_floorplan_w.svg` | 1,763 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_interface_k.svg` | 800 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_interface_w.svg` | 800 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_tool_k.svg` | 1,609 | 파일 크기/참조 검사 |
| `en/egbim/img/ico_value_tool_w.svg` | 1,611 | 파일 크기/참조 검사 |
| `en/egbim/img/info_img_01.png` | 144,566 | 파일 크기/참조 검사 |
| `en/egbim/img/info_img_01_01.svg` | 5,631 | 파일 크기/참조 검사 |
| `en/egbim/img/info_img_02.png` | 285,557 | 파일 크기/참조 검사 |
| `en/egbim/img/info_img_02_01.png` | 41,355 | 파일 크기/참조 검사 |
| `en/egbim/img/inter_svg_01.svg` | 59,439 | 파일 크기/참조 검사 |
| `en/egbim/img/inter_svg_02.svg` | 66,967 | 파일 크기/참조 검사 |
| `en/egbim/img/inter_svg_03.svg` | 55,423 | 파일 크기/참조 검사 |
| `en/egbim/img/inter_svg_04.svg` | 52,359 | 파일 크기/참조 검사 |
| `en/egbim/img/inter_svg_05.svg` | 55,759 | 파일 크기/참조 검사 |
| `en/egbim/img/inter_svg_06.svg` | 54,887 | 파일 크기/참조 검사 |
| `en/egbim/img/interface_dual_bg.png` | 531,948 | 파일 크기/참조 검사 |
| `en/egbim/img/interface_img_01.svg` | 17,429 | 파일 크기/참조 검사 |
| `en/egbim/img/interface_img_02.png` | 370,646 | 파일 크기/참조 검사 |
| `en/egbim/img/interface_img_03.svg` | 425,824 | 파일 크기/참조 검사 |
| `en/egbim/img/interface_intro_bg.png` | 3,812,608 | 파일 크기/참조 검사 |
| `en/egbim/img/interface_route_bg.png` | 317,387 | 파일 크기/참조 검사 |
| `en/egbim/img/interface_route_screen.png` | 252,999 | 파일 크기/참조 검사 |
| `en/egbim/img/intro_mask.svg` | 166 | 파일 크기/참조 검사 |
| `en/egbim/img/kakao.png` | 804 | 파일 크기/참조 검사 |
| `en/egbim/img/kpay.png` | 2,697 | 파일 크기/참조 검사 |
| `en/egbim/img/loginBg1.jpg` | 593,676 | 파일 크기/참조 검사 |
| `en/egbim/img/loginBg2.jpg` | 246,684 | 파일 크기/참조 검사 |
| `en/egbim/img/loginBgTest.jpg` | 692,071 | 파일 크기/참조 검사 |
| `en/egbim/img/loginBgTestB.jpg` | 466,966 | 파일 크기/참조 검사 |
| `en/egbim/img/logo.png` | 3,797 | 파일 크기/참조 검사 |
| `en/egbim/img/lpay_logo.png` | 1,393 | 파일 크기/참조 검사 |
| `en/egbim/img/m_floating_bg_4.png` | 9,192 | 파일 크기/참조 검사 |
| `en/egbim/img/m_logo.png` | 3,100 | 파일 크기/참조 검사 |
| `en/egbim/img/main_1.mp4` | 7,972,277 | 파일 크기/참조 검사 |
| `en/egbim/img/main_1_v.mp4` | 10,867,479 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/main_2.mp4` | 8,962,969 | 파일 크기/참조 검사 |
| `en/egbim/img/main_2_v.mp4` | 10,762,397 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/main_3.mp4` | 12,229,358 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/main_3_v.mp4` | 10,529,771 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/main_4.mp4` | 6,876,992 | 파일 크기/참조 검사 |
| `en/egbim/img/main_4_v.mp4` | 11,079,565 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/main_5.mp4` | 10,866,078 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/main_5_v.mp4` | 10,436,388 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/egbim/img/main_popup/251027_main_popup.png` | 1,017,667 | 파일 크기/참조 검사 |
| `en/egbim/img/main_popup/251027_main_popup_m.png` | 532,029 | 파일 크기/참조 검사 |
| `en/egbim/img/main_popup/251128_main_popup.png` | 251,815 | 파일 크기/참조 검사 |
| `en/egbim/img/main_popup/251128_main_popup_m.png` | 146,133 | 파일 크기/참조 검사 |
| `en/egbim/img/main_popup/251223_main_popup.png` | 370,651 | 파일 크기/참조 검사 |
| `en/egbim/img/main_popup/251223_main_popup_m.png` | 196,368 | 파일 크기/참조 검사 |
| `en/egbim/img/mobile/btn_close.png` | 3,265 | 파일 크기/참조 검사 |
| `en/egbim/img/mobile/gnb_bg.png` | 1,012 | 파일 크기/참조 검사 |
| `en/egbim/img/mobile/gnb_bg2.png` | 976 | 파일 크기/참조 검사 |
| `en/egbim/img/mobile/gnb_sch.png` | 1,795 | 파일 크기/참조 검사 |
| `en/egbim/img/mobile/icon_menu.png` | 1,090 | 파일 크기/참조 검사 |
| `en/egbim/img/mobile/icon_my.png` | 1,634 | 파일 크기/참조 검사 |
| `en/egbim/img/more-btn.gif` | 1,204 | 파일 크기/참조 검사 |
| `en/egbim/img/no_img.png` | 991 | 파일 크기/참조 검사 |
| `en/egbim/img/no_profile.gif` | 1,953 | 파일 크기/참조 검사 |
| `en/egbim/img/og-main-thumb.JPG` | 112,930 | 파일 크기/참조 검사 |
| `en/egbim/img/pay_icon1.png` | 1,676 | 파일 크기/참조 검사 |
| `en/egbim/img/pay_icon2.png` | 1,703 | 파일 크기/참조 검사 |
| `en/egbim/img/pay_icon3.png` | 1,174 | 파일 크기/참조 검사 |
| `en/egbim/img/pay_icon4.png` | 1,185 | 파일 크기/참조 검사 |
| `en/egbim/img/payco.png` | 2,326 | 파일 크기/참조 검사 |
| `en/egbim/img/payco_logo.png` | 711 | 파일 크기/참조 검사 |
| `en/egbim/img/paynow.png` | 2,387 | 파일 크기/참조 검사 |
| `en/egbim/img/paynow_logo.png` | 679 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_block_bg.png` | 906,391 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_intro_bg.png` | 475,109 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_menu_bg.png` | 298,380 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_print_bg.png` | 786,099 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_route_01.png` | 870,613 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_route_02.png` | 120,852 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_route_03.png` | 112,932 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_route_bg.png` | 980,927 | 파일 크기/참조 검사 |
| `en/egbim/img/primary_style_bg.png` | 1,043,595 | 파일 크기/참조 검사 |
| `en/egbim/img/print_img_01.png` | 307,911 | 파일 크기/참조 검사 |
| `en/egbim/img/print_img_02.png` | 1,340,845 | 파일 크기/참조 검사 |
| `en/egbim/img/printarea_img_01.png` | 1,019,373 | 파일 크기/참조 검사 |
| `en/egbim/img/printarea_img_02.png` | 661,226 | 파일 크기/참조 검사 |
| `en/egbim/img/require.png` | 2,922 | 파일 크기/참조 검사 |
| `en/egbim/img/road_proportionality_bg.jpg` | 374,805 | 파일 크기/참조 검사 |
| `en/egbim/img/samsungpay.png` | 2,071 | 파일 크기/참조 검사 |
| `en/egbim/img/sch_btn.png` | 1,234 | 파일 크기/참조 검사 |
| `en/egbim/img/sitemap_menu01.png` | 1,768,415 | 파일 크기/참조 검사 |
| `en/egbim/img/sitemap_menu02.png` | 1,000,846 | 파일 크기/참조 검사 |
| `en/egbim/img/sitemap_menu03.png` | 1,659,994 | 파일 크기/참조 검사 |
| `en/egbim/img/sitemap_menu04.png` | 1,568,391 | 파일 크기/참조 검사 |
| `en/egbim/img/sitemap_menu05.png` | 2,119,415 | 파일 크기/참조 검사 |
| `en/egbim/img/skpay11_icon.png` | 7,920 | 파일 크기/참조 검사 |
| `en/egbim/img/ssgpay_icon.png` | 1,887 | 파일 크기/참조 검사 |
| `en/egbim/img/style_img_01.png` | 98,394 | 파일 크기/참조 검사 |
| `en/egbim/img/style_img_02.png` | 129,694 | 파일 크기/참조 검사 |
| `en/egbim/img/style_img_03.png` | 397,053 | 파일 크기/참조 검사 |
| `en/egbim/img/tnb_shop.jpg` | 881 | 파일 크기/참조 검사 |
| `en/egbim/img/tri_img.svg` | 888 | 파일 크기/참조 검사 |
| `en/egbim/img/ts01.gif` | 138 | 파일 크기/참조 검사 |
| `en/egbim/img/ts01.png` | 1,219 | 파일 크기/참조 검사 |
| `en/egbim/img/ts02.gif` | 148 | 파일 크기/참조 검사 |
| `en/egbim/img/ts02.png` | 1,252 | 파일 크기/참조 검사 |
| `en/egbim/img/ts03.gif` | 154 | 파일 크기/참조 검사 |
| `en/egbim/img/ts03.png` | 1,319 | 파일 크기/참조 검사 |
| `en/egbim/img/value_arc.svg` | 925 | 파일 크기/참조 검사 |
| `en/egbim/img/value_arc_r.svg` | 924 | 파일 크기/참조 검사 |
| `en/egbim/img/value_feature_bg.png` | 815,763 | 파일 크기/참조 검사 |
| `en/egbim/img/value_feature_bim_bg.png` | 842,050 | 파일 크기/참조 검사 |
| `en/egbim/img/value_feature_floorplan_bg.png` | 730,776 | 파일 크기/참조 검사 |
| `en/egbim/img/value_feature_interface_bg.png` | 2,549,341 | 파일 크기/참조 검사 |
| `en/egbim/img/value_feature_tool_bg.png` | 271,209 | 파일 크기/참조 검사 |
| `en/egbim/img/value_introbg.png` | 4,678,800 | 파일 크기/참조 검사 |
| `en/egbim/img/value_system_bg.png` | 555,451 | 파일 크기/참조 검사 |
| `en/egbim/img/wrest.gif` | 51 | 파일 크기/참조 검사 |
| `en/egbim/interface.html` | 11,052 | HTML: 동기 외부 스크립트 13, 이미지 4 (lazy 0), video 0, iframe 0; 외부 URL 12, 로컬 참조 확인 필요 0 |
| `en/egbim/js/StickyOnTable.js` | 5,296 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/autosave.js` | 5,067 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/certify.js` | 4,875 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/ckeditor/adapters/jquery.js` | 3,189 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/build-config.js` | 2,909 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/ckeditor.js` | 760,672 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 7; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/config.js` | 346 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/contents.css` | 3,092 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/lang/en.js` | 18,232 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/lang/ko.js` | 19,743 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/a11yhelp.js` | 2,978 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/af.js` | 4,182 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ar.js` | 4,378 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/az.js` | 4,358 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/bg.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ca.js` | 4,816 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/cs.js` | 4,965 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/cy.js` | 4,415 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/da.js` | 4,273 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/de-ch.js` | 4,740 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/de.js` | 4,684 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/el.js` | 7,659 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/en-au.js` | 4,230 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/en-gb.js` | 4,230 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/en.js` | 4,227 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/eo.js` | 4,825 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/es-mx.js` | 4,921 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/es.js` | 4,827 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/et.js` | 4,444 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/eu.js` | 4,532 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fa.js` | 6,178 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fi.js` | 4,787 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fo.js` | 4,229 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fr-ca.js` | 4,949 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fr.js` | 5,337 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/gl.js` | 4,841 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/gu.js` | 4,437 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/he.js` | 4,981 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/hi.js` | 4,241 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/hr.js` | 4,307 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/hu.js` | 4,793 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/id.js` | 4,065 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/it.js` | 5,265 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ja.js` | 5,224 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/km.js` | 5,245 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ko.js` | 5,624 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ku.js` | 6,059 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/lt.js` | 4,236 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/lv.js` | 4,860 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/mk.js` | 4,618 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/mn.js` | 4,234 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/nb.js` | 4,484 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/nl.js` | 4,559 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/no.js` | 4,470 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/oc.js` | 5,125 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/pl.js` | 5,188 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/pt-br.js` | 4,955 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/pt.js` | 4,595 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ro.js` | 4,586 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ru.js` | 6,672 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/si.js` | 6,170 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sk.js` | 4,795 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sl.js` | 4,575 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sq.js` | 4,960 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sr-latn.js` | 4,924 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sr.js` | 7,542 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sv.js` | 4,395 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/th.js` | 4,605 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/tr.js` | 4,606 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/tt.js` | 4,545 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ug.js` | 6,963 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/uk.js` | 6,953 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/vi.js` | 5,426 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/zh-cn.js` | 4,172 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/zh.js` | 4,381 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/about/dialogs/about.js` | 1,957 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/clipboard/dialogs/paste.js` | 3,835 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/colordialog/dialogs/colordialog.css` | 806 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/colordialog/dialogs/colordialog.js` | 5,356 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/copyformatting/styles/copyformatting.css` | 1,527 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/dialog/dialogDefinition.js` | 186 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/dialog/styles/dialog.css` | 249 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/div/dialogs/div.js` | 4,685 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/plugindefinition.js` | 3 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/_helpers/tools.js` | 677 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/authentication.js` | 3,038 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/exportpdf.js` | 4,835 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/configfilename.html` | 694 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/emptyeditor.html` | 432 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integration.html` | 5,396 | HTML: 동기 외부 스크립트 0, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integrations/easyimage.html` | 814 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/notifications.html` | 396 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/notificationsasync.html` | 1,047 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/paperformat.html` | 1,273 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/readonly.html` | 411 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/stylesheets.html` | 1,200 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokenfetching.html` | 568 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokentwoeditorscorrect.html` | 1,064 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokentwoeditorswrong.html` | 1,088 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokenwithouturl.html` | 475 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/manual/wrongendpoint.html` | 488 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/notification.js` | 1,977 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js` | 4,757 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/statistics.js` | 1,098 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/exportpdf/tests/stylesheets.js` | 9,899 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/find/dialogs/find.js` | 11,465 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/button.js` | 1,886 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/checkbox.js` | 2,601 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/form.js` | 2,150 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/hiddenfield.js` | 1,728 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/radio.js` | 2,411 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/select.js` | 8,562 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/textarea.js` | 2,358 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/forms/dialogs/textfield.js` | 3,463 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/iframe/dialogs/iframe.js` | 3,505 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/image/dialogs/image.js` | 21,588 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/link/dialogs/anchor.js` | 2,231 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/link/dialogs/link.js` | 13,279 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/liststyle/dialogs/liststyle.js` | 2,908 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/pastefromgdocs/filter/default.js` | 2,232 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/pastefromlibreoffice/filter/default.js` | 3,536 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/pastefromword/filter/default.js` | 19,960 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/pastetools/filter/common.js` | 10,419 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/pastetools/filter/image.js` | 3,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/preview/preview.html` | 259 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/preview/styles/screen.css` | 242 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/scayt/dialogs/dialog.css` | 419 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/scayt/dialogs/options.js` | 16,167 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/scayt/dialogs/toolbar.css` | 1,302 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/scayt/skins/moono-lisa/scayt.css` | 381 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/smiley/dialogs/smiley.js` | 3,487 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/af.js` | 4,575 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ar.js` | 4,824 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/az.js` | 3,432 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/bg.js` | 4,848 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ca.js` | 5,057 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/cs.js` | 5,013 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/cy.js` | 4,938 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/da.js` | 3,406 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/de-ch.js` | 4,835 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/de.js` | 4,826 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/el.js` | 7,774 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en-au.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en-ca.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en-gb.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en.js` | 4,589 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/eo.js` | 4,109 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/es-mx.js` | 4,818 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/es.js` | 4,989 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/et.js` | 3,857 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/eu.js` | 4,591 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fa.js` | 5,813 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fi.js` | 4,627 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fr-ca.js` | 3,259 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fr.js` | 3,897 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/gl.js` | 5,046 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/he.js` | 5,027 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/hr.js` | 4,433 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/hu.js` | 4,176 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/id.js` | 4,596 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/it.js` | 5,063 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ja.js` | 4,022 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/km.js` | 4,793 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ko.js` | 4,959 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ku.js` | 7,606 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/lt.js` | 4,634 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/lv.js` | 5,064 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/nb.js` | 3,472 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/nl.js` | 4,768 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/no.js` | 3,472 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/oc.js` | 3,871 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/pl.js` | 4,370 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/pt-br.js` | 3,870 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/pt.js` | 4,837 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ro.js` | 4,720 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ru.js` | 7,589 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/si.js` | 4,930 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sk.js` | 4,806 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sl.js` | 4,390 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sq.js` | 5,033 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sr-latn.js` | 4,756 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sr.js` | 7,558 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sv.js` | 3,524 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/th.js` | 4,718 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/tr.js` | 4,520 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/tt.js` | 6,771 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ug.js` | 5,045 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/uk.js` | 6,411 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/vi.js` | 6,128 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/zh-cn.js` | 4,419 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/zh.js` | 4,199 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/specialchar/dialogs/specialchar.js` | 5,034 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/table/dialogs/table.js` | 9,080 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/tableselection/styles/tableselection.css` | 1,145 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/tabletools/dialogs/tableCell.js` | 7,387 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/templates/dialogs/templates.css` | 1,604 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/templates/dialogs/templates.js` | 3,429 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/templates/templatedefinition.js` | 186 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/plugins/templates/templates/default.js` | 1,983 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/css/samples.css` | 67,340 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/img/github-top.png` | 383 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/img/header-bg.png` | 13,086 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/img/header-separator.png` | 123 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/img/logo.png` | 5,634 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/img/logo.svg` | 10,900 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/img/navigation-tip.png` | 12,029 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/index.html` | 7,234 | HTML: 동기 외부 스크립트 2, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 16, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/js/sample.js` | 1,594 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/js/sf.js` | 6,442 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/ajax.html` | 2,911 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/api.html` | 7,545 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/appendto.html` | 2,523 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/assets/outputxhtml/outputxhtml.css` | 2,161 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/assets/uilanguages/languages.js` | 1,467 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/datafiltering.html` | 47,840 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 15, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/dialog/assets/my_dialog.js` | 911 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/dialog/dialog.html` | 7,606 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/divreplace.html` | 4,893 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/enterkey/enterkey.html` | 5,018 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/htmlwriter/outputhtml.html` | 7,622 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/index.html` | 6,073 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/inlineall.html` | 10,399 | HTML: 동기 외부 스크립트 1, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 7, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/inlinebycode.html` | 6,395 | HTML: 동기 외부 스크립트 1, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 14, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/inlinetextarea.html` | 5,125 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/jquery.html` | 7,754 | HTML: 동기 외부 스크립트 3, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 12, 로컬 참조 확인 필요 3; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/magicline/magicline.html` | 9,249 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/readonly.html` | 3,132 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/replacebyclass.html` | 7,234 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/replacebycode.html` | 7,119 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/sample.css` | 5,112 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/sample.js` | 1,693 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/tabindex.html` | 2,609 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/toolbar/toolbar.html` | 10,291 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/uicolor.html` | 2,810 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/uilanguages.html` | 4,741 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/wysiwygarea/fullpage.html` | 8,531 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/old/xhtmlstyle.html` | 7,233 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/css/fontello.css` | 1,758 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/font/LICENSE.txt` | 188 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/font/config.json` | 584 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.eot` | 4,988 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.svg` | 1,714 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.ttf` | 4,820 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.woff` | 2,904 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/index.html` | 15,808 | HTML: 동기 외부 스크립트 9, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 11, 로컬 참조 확인 필요 6; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/js/abstracttoolbarmodifier.js` | 6,535 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/js/fulltoolbareditor.js` | 3,846 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/js/toolbarmodifier.js` | 16,683 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/samples/toolbarconfigurator/js/toolbartextmodifier.js` | 6,863 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/dialog.css` | 13,650 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/dialog_ie.css` | 14,673 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/dialog_ie8.css` | 15,222 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/dialog_iequirks.css` | 14,702 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/editor.css` | 48,325 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/editor_gecko.css` | 48,406 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/editor_ie.css` | 49,324 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/editor_ie8.css` | 50,130 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/skins/moono-lisa/editor_iequirks.css` | 49,973 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/styles.js` | 5,577 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/ckeditor/vendor/promise.js` | 6,309 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/common.js` | 39,215 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 4 |
| `en/egbim/js/common_240813.js` | 27,419 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `en/egbim/js/common_250204.js` | 30,806 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `en/egbim/js/common_250307.js` | 31,539 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `en/egbim/js/common_OR.js` | 32,362 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `en/egbim/js/common_bak.js` | 27,658 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `en/egbim/js/floorplan.js` | 5,586 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/floorplan_253010.js` | 4,375 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/font-awesome/css/font-awesome.css` | 39,751 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `en/egbim/js/font-awesome/css/font-awesome.min.css` | 31,004 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `en/egbim/js/forbim.js` | 4,613 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/forbim_250204.js` | 2,304 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/forbim_250310.js` | 3,755 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/html5.js` | 2,396 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/include.js` | 620 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/index.js` | 5,748 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/index_240813.js` | 4,036 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/index_250204.js` | 4,513 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/index_250310.js` | 4,593 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/interface.js` | 4,785 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/interface_251226.js` | 4,687 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery-1.12.4.min.js` | 97,168 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `en/egbim/js/jquery-1.8.3.min.js` | 93,637 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `en/egbim/js/jquery-3.6.1.min.js` | 89,664 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery-migrate-1.4.1.min.js` | 10,057 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.anchorScroll.js` | 2,234 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.bxslider.js` | 53,133 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.fancyalert.js` | 988 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.fancylist.js` | 2,105 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.menu.js` | 2,930 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.mousewheel.min.js` | 2,680 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.nicescroll.min.js` | 57,783 | 텍스트 리소스 참조 검사; 외부 URL 1, 로컬 참조 확인 필요 1 |
| `en/egbim/js/jquery.register_form.js` | 2,172 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.shop.menu.js` | 1,838 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/jquery.sms_paging.js` | 3,309 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/kakaolink.js` | 759 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/md5.js` | 8,084 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/modernizr.custom.70111.js` | 2,127 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/owlcarousel/owl.carousel.css` | 4,930 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `en/egbim/js/owlcarousel/owl.carousel.js` | 93,440 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/owlcarousel/owl.carousel.min.css` | 3,356 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `en/egbim/js/owlcarousel/owl.carousel.min.js` | 44,348 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `en/egbim/js/placeholders.min.js` | 5,103 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/popup.js` | 11,039 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/popup_240813.js` | 8,834 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/popup_250204.js` | 11,966 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/primary.js` | 4,150 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/primary_240927.js` | 4,251 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/primary_250307.js` | 3,538 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/public.js` | 3,544 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/public_240813.js` | 6,135 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/remodal/remodal-default-theme.css` | 4,181 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/remodal/remodal.css` | 1,275 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/remodal/remodal.js` | 19,911 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/road.js` | 3,906 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/road_240813.js` | 4,450 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/scroll_oldie.js` | 1,239 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.category.navigation.js` | 2,156 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.couponzone.js` | 1,118 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.js` | 16,514 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.list.action.js` | 10,215 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.list.js` | 3,078 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.mobile.list.js` | 1,385 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.mobile.main.js` | 4,480 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.order.js` | 297 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/shop.override.js` | 7,342 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/sns.js` | 385 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/style.css` | 109,081 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/egbim/js/swipe.js` | 14,924 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/swiper/swiper.min.css` | 19,345 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/swiper/swiper.min.js` | 111,727 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/tooltipster/tooltipster.bundle.css` | 9,909 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/tooltipster/tooltipster.bundle.js` | 124,074 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/tooltipster/tooltipster.bundle.min.css` | 6,495 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/tooltipster/tooltipster.bundle.min.js` | 39,901 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/value.js` | 1,189 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/value_240813.js` | 7,022 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 4 |
| `en/egbim/js/viewimageresize.js` | 2,575 | 텍스트 리소스 참조 검사 |
| `en/egbim/js/wrest.js` | 11,466 | 텍스트 리소스 참조 검사 |
| `en/egbim/primary.html` | 12,955 | HTML: 동기 외부 스크립트 9, 이미지 6 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/egbim/value.html` | 13,365 | HTML: 동기 외부 스크립트 9, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/faq.html` | 2,722 | HTML: 동기 외부 스크립트 6, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/buy.html` | 3,489 | HTML: 동기 외부 스크립트 8, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 9, 로컬 참조 확인 필요 0 |
| `en/gaia/css/font.css` | 1,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `en/gaia/css/reset.css` | 2,193 | 텍스트 리소스 참조 검사 |
| `en/gaia/css/style.css` | 271,356 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `en/gaia/download/GAIA_leaflet.pdf` | 7,402,090 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Black/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Black/notokr-black-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/gaia/font/NotoKR-Black/notokr-black.eot` | 149,951 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Black/notokr-black.svg` | 703,668 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Black/notokr-black.ttf` | 358,600 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Black/notokr-black.woff` | 180,348 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Black/notokr-black.woff2` | 128,720 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Black/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Black/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Black/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Black/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Bold/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Bold/notokr-bold-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/gaia/font/NotoKR-Bold/notokr-bold.eot` | 156,008 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Bold/notokr-bold.svg` | 705,999 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Bold/notokr-bold.ttf` | 359,412 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Bold/notokr-bold.woff` | 185,412 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Bold/notokr-bold.woff2` | 134,968 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Bold/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Bold/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Bold/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Bold/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-DemiLight/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 173,863 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/gaia/font/NotoKR-DemiLight/notokr-demilight.eot` | 155,464 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/notokr-demilight.svg` | 733,933 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/notokr-demilight.ttf` | 369,728 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/notokr-demilight.woff` | 187,464 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/notokr-demilight.woff2` | 133,772 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-DemiLight/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-DemiLight/stylesheet.css` | 547 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Light/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Light/notokr-light-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/gaia/font/NotoKR-Light/notokr-light.eot` | 153,179 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Light/notokr-light.svg` | 748,368 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Light/notokr-light.ttf` | 373,820 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Light/notokr-light.woff` | 185,532 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Light/notokr-light.woff2` | 131,096 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Light/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Light/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Light/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Light/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Medium/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Medium/notokr-medium-demo.html` | 173,842 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/gaia/font/NotoKR-Medium/notokr-medium.eot` | 155,800 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Medium/notokr-medium.svg` | 717,209 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Medium/notokr-medium.ttf` | 364,276 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Medium/notokr-medium.woff` | 185,440 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Medium/notokr-medium.woff2` | 133,836 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Medium/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Medium/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Medium/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Medium/stylesheet.css` | 523 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Regular/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Regular/notokr-regular-demo.html` | 173,868 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/gaia/font/NotoKR-Regular/notokr-regular.eot` | 156,734 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Regular/notokr-regular.svg` | 727,332 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Regular/notokr-regular.ttf` | 367,940 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Regular/notokr-regular.woff` | 187,364 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Regular/notokr-regular.woff2` | 134,960 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Regular/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Regular/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Regular/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Regular/stylesheet.css` | 531 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Thin/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Thin/notokr-thin-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `en/gaia/font/NotoKR-Thin/notokr-thin.eot` | 143,518 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Thin/notokr-thin.svg` | 761,397 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Thin/notokr-thin.ttf` | 377,440 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Thin/notokr-thin.woff` | 175,184 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Thin/notokr-thin.woff2` | 120,720 | 파일 크기/참조 검사 |
| `en/gaia/font/NotoKR-Thin/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Thin/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `en/gaia/font/NotoKR-Thin/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/font/NotoKR-Thin/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/gaia/further.html` | 13,489 | HTML: 동기 외부 스크립트 9, 이미지 20 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/gaia/img/Thumbs.db` | 1,845,248 | 파일 크기/참조 검사 |
| `en/gaia/img/arrow_r.svg` | 167 | 파일 크기/참조 검사 |
| `en/gaia/img/atom_line.svg` | 1,633 | 파일 크기/참조 검사 |
| `en/gaia/img/atom_obj.svg` | 1,936 | 파일 크기/참조 검사 |
| `en/gaia/img/baron_logo.svg` | 6,233 | 파일 크기/참조 검사 |
| `en/gaia/img/baron_logo_eng.svg` | 9,591 | 파일 크기/참조 검사 |
| `en/gaia/img/bg_close.png` | 906 | 파일 크기/참조 검사 |
| `en/gaia/img/bg_pop.png` | 2,213,561 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_end.gif` | 1,176 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_first.gif` | 1,885 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_idx_left.png` | 3,141 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_idx_right.png` | 442 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_next.gif` | 1,169 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_prev.gif` | 1,873 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_search.jpg` | 782 | 파일 크기/참조 검사 |
| `en/gaia/img/btn_top.gif` | 1,178 | 파일 크기/참조 검사 |
| `en/gaia/img/bullet.gif` | 1,165 | 파일 크기/참조 검사 |
| `en/gaia/img/buy_intro_bg.jpg` | 727,741 | 파일 크기/참조 검사 |
| `en/gaia/img/buy_video.mp4` | 60,429,670 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/captcha.png` | 4,886 | 파일 크기/참조 검사 |
| `en/gaia/img/captcha2.png` | 4,886 | 파일 크기/참조 검사 |
| `en/gaia/img/chk.png` | 1,070 | 파일 크기/참조 검사 |
| `en/gaia/img/close_btn.gif` | 1,209 | 파일 크기/참조 검사 |
| `en/gaia/img/close_btn.png` | 1,147 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/Thumbs.db` | 522,752 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_1.png` | 729,470 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_10.png` | 361,340 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_11.png` | 145,644 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_12.png` | 14,091 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_13.png` | 17,110 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_14.png` | 92,527 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_15.png` | 144,244 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_16.png` | 188,767 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_17.png` | 221,944 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_18.png` | 254,233 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_19.png` | 317,194 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_2.png` | 727,547 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_20.png` | 397,369 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_21.png` | 468,221 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_22.png` | 502,992 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_23.png` | 503,362 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_24.png` | 500,551 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_25.png` | 500,422 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_26.png` | 503,390 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_27.png` | 502,812 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_28.png` | 503,077 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_29.png` | 541,028 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_3.png` | 729,358 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_30.png` | 549,525 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_31.png` | 549,041 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_32.png` | 550,112 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_33.png` | 554,641 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_34.png` | 559,102 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_35.png` | 558,365 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_36.png` | 559,487 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_37.png` | 560,431 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_38.png` | 558,668 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_39.png` | 558,298 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_4.png` | 728,233 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_40.png` | 559,030 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_41.png` | 607,476 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_42.png` | 662,486 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_43.png` | 720,297 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_44.png` | 780,145 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_45.png` | 851,441 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_46.png` | 914,471 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_47.png` | 953,623 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_48.png` | 962,638 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_49.png` | 962,638 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_5.png` | 705,944 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_50.png` | 962,638 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_51.png` | 962,638 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_52.png` | 1,049,340 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_53.png` | 1,138,471 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_54.png` | 1,197,889 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_55.png` | 1,233,019 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_56.png` | 1,259,825 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_57.png` | 1,311,789 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_58.png` | 1,357,885 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_59.png` | 1,366,900 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_6.png` | 662,210 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_60.png` | 1,350,101 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_61.png` | 1,288,616 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_62.png` | 1,223,769 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_63.png` | 1,232,384 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_64.png` | 1,240,668 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_65.png` | 1,241,184 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_66.png` | 1,240,533 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_67.png` | 1,239,298 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_68.png` | 1,240,688 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_69.png` | 1,241,242 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_7.png` | 607,289 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_70.png` | 1,243,732 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_71.png` | 1,252,218 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_72.png` | 1,252,668 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_73.png` | 1,251,460 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_74.png` | 1,248,539 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_75.png` | 1,243,890 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_76.png` | 1,239,844 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_77.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_78.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_79.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_8.png` | 543,705 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_80.png` | 1,238,030 | 파일 크기/참조 검사 |
| `en/gaia/img/com_img/comp_9.png` | 451,356 | 파일 크기/참조 검사 |
| `en/gaia/img/faq_intro_bg.png` | 933,519 | 파일 크기/참조 검사 |
| `en/gaia/img/floating_buy_bg.svg` | 1,318 | 파일 크기/참조 검사 |
| `en/gaia/img/floating_buy_bg_m.svg` | 1,907 | 파일 크기/참조 검사 |
| `en/gaia/img/floating_faq_bg.svg` | 1,352 | 파일 크기/참조 검사 |
| `en/gaia/img/floating_faq_bg_m.svg` | 3,299 | 파일 크기/참조 검사 |
| `en/gaia/img/ft.png` | 3,204 | 파일 크기/참조 검사 |
| `en/gaia/img/ft_logo.png` | 3,737 | 파일 크기/참조 검사 |
| `en/gaia/img/further_app_fig1.jpg` | 352,068 | 파일 크기/참조 검사 |
| `en/gaia/img/further_app_fig2.jpg` | 439,908 | 파일 크기/참조 검사 |
| `en/gaia/img/further_app_fig3.jpg` | 781,742 | 파일 크기/참조 검사 |
| `en/gaia/img/further_app_fig4.jpg` | 898,768 | 파일 크기/참조 검사 |
| `en/gaia/img/further_gather_arrow_l.svg` | 546 | 파일 크기/참조 검사 |
| `en/gaia/img/further_gather_step1_line.svg` | 1,258 | 파일 크기/참조 검사 |
| `en/gaia/img/further_gather_step2_line1.svg` | 10,139 | 파일 크기/참조 검사 |
| `en/gaia/img/further_gather_step2_line2.svg` | 1,398 | 파일 크기/참조 검사 |
| `en/gaia/img/further_intro_bg.jpg` | 583,279 | 파일 크기/참조 검사 |
| `en/gaia/img/further_link_fig1.jpg` | 243,891 | 파일 크기/참조 검사 |
| `en/gaia/img/further_link_fig2.jpg` | 389,080 | 파일 크기/참조 검사 |
| `en/gaia/img/further_link_fig3.jpg` | 338,322 | 파일 크기/참조 검사 |
| `en/gaia/img/further_link_fig4.jpg` | 393,229 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_bg1.jpg` | 381,978 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_bg2.jpg` | 366,130 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_bg3.jpg` | 318,558 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_gather01.jpg` | 217,150 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_gather02-1.jpg` | 11,898 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_gather02-2.jpg` | 24,152 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_gather02-3.jpg` | 37,404 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_gather02.jpg` | 186,226 | 파일 크기/참조 검사 |
| `en/gaia/img/further_process_gather03.jpg` | 310,012 | 파일 크기/참조 검사 |
| `en/gaia/img/gaia_k.svg` | 870 | 파일 크기/참조 검사 |
| `en/gaia/img/gaia_obj_k.svg` | 343 | 파일 크기/참조 검사 |
| `en/gaia/img/gaia_obj_w.svg` | 341 | 파일 크기/참조 검사 |
| `en/gaia/img/gaia_w.svg` | 888 | 파일 크기/참조 검사 |
| `en/gaia/img/gnb_bg.gif` | 1,169 | 파일 크기/참조 검사 |
| `en/gaia/img/gnb_bg00.gif` | 54 | 파일 크기/참조 검사 |
| `en/gaia/img/gnb_bg01.gif` | 54 | 파일 크기/참조 검사 |
| `en/gaia/img/gnb_bg2.gif` | 49 | 파일 크기/참조 검사 |
| `en/gaia/img/ico-default-naverpay.png` | 2,689 | 파일 크기/참조 검사 |
| `en/gaia/img/ico-mobile-applepay.png` | 2,063 | 파일 크기/참조 검사 |
| `en/gaia/img/ico-mobile-kakaopay.png` | 3,251 | 파일 크기/참조 검사 |
| `en/gaia/img/ico-mobile-naverpay.png` | 3,261 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_admin.svg` | 5,691 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_angle.svg` | 243 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_answer.svg` | 294 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_arrow.svg` | 488 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_arrow_s.svg` | 490 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_bulit_check.svg` | 247 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_buy_alarm.svg` | 929 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_buy_ask.svg` | 2,054 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_buy_brochure.svg` | 2,196 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_buy_mail.svg` | 585 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_buy_manual.svg` | 1,638 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_buy_tel.svg` | 1,093 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_cafe.svg` | 1,171 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_close.svg` | 201 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_company.svg` | 887 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_complete.svg` | 1,088 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_countdown.svg` | 4,119 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_infomodel.svg` | 1,985 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_modify.svg` | 3,495 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_network.svg` | 3,849 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_results_01.svg` | 2,409 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_results_02.svg` | 2,480 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_results_03.svg` | 2,086 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_results_04.svg` | 2,024 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_results_05.svg` | 858 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dia_site.svg` | 983 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_dublecheck.svg` | 1,680 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_email.svg` | 1,146 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_facebook.svg` | 952 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_floating_buy.svg` | 651 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_floating_buy_on.svg` | 651 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_floating_faq.svg` | 1,173 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_floating_faq_on.svg` | 1,174 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_footer_close.svg` | 333 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_further_dia1.svg` | 6,202 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_further_dia1_w.svg` | 6,194 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_further_dia2.svg` | 1,008 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_further_dia2_w.svg` | 1,000 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_further_dia3.svg` | 994 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_further_dia3_w.svg` | 990 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_further_send.svg` | 1,486 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_ham.svg` | 309 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_id.svg` | 1,018 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_language.svg` | 1,324 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_location_01.svg` | 1,732 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_location_02.svg` | 1,432 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_location_03.svg` | 898 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_location_04.svg` | 4,247 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_lock.svg` | 1,607 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_model_01.svg` | 622 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_model_02.svg` | 734 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_model_03.svg` | 664 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_model_04.svg` | 1,427 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_model_05.svg` | 1,045 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_model_06.svg` | 3,675 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_modify_01.svg` | 711 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_modify_02.svg` | 13,436 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_modify_03.svg` | 589 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_modify_04.svg` | 988 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_modify_05.svg` | 555 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_modify_06.svg` | 839 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_my.svg` | 888 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_network.svg` | 1,574 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_pg_left.svg` | 1,056 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_pg_right.svg` | 1,046 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_phone.svg` | 727 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_primary_pub04.svg` | 359 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_pw.svg` | 1,185 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_send_email.svg` | 634 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_signout.svg` | 933 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs01.svg` | 2,420 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs01_mo.svg` | 2,465 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs01_mo_w.svg` | 2,458 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs01_w.svg` | 2,383 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs02.svg` | 739 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs02_mo.svg` | 889 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs02_mo_w.svg` | 885 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs02_w.svg` | 710 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs03.svg` | 2,030 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs03_mo.svg` | 2,067 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs03_mo_w.svg` | 2,072 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs03_w.svg` | 1,999 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs04.svg` | 2,074 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs04_mo.svg` | 2,078 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs04_mo_w.svg` | 2,066 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs04_w.svg` | 2,043 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs05.svg` | 2,401 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs05_mo.svg` | 2,390 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs05_mo_w.svg` | 2,382 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_slide_tabs05_w.svg` | 2,374 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_cursor.svg` | 1,810 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_data_k.svg` | 1,774 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_data_w.svg` | 1,774 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_design_k.svg` | 1,415 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_design_w.svg` | 1,415 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_devices_k.svg` | 988 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_devices_w.svg` | 988 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_interface_k.svg` | 800 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_interface_w.svg` | 800 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_screen.svg` | 1,742 | 파일 크기/참조 검사 |
| `en/gaia/img/ico_value_scroll.svg` | 996 | 파일 크기/참조 검사 |
| `en/gaia/img/info_img_01_01.svg` | 5,631 | 파일 크기/참조 검사 |
| `en/gaia/img/interface_img_01.svg` | 92,104 | 파일 크기/참조 검사 |
| `en/gaia/img/interface_img_03.svg` | 709,308 | 파일 크기/참조 검사 |
| `en/gaia/img/interface_route_screen.png` | 301,366 | 파일 크기/참조 검사 |
| `en/gaia/img/kakao.png` | 804 | 파일 크기/참조 검사 |
| `en/gaia/img/kpay.png` | 2,697 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_01.png` | 562,212 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_01.svg` | 1,224,284 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_01_01.png` | 1,343,215 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_01_02.png` | 1,900,900 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_01_03.png` | 1,821,380 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_01_04.png` | 1,817,622 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_01.png` | 1,456,305 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_01_click_off.png` | 1,537,297 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_01_click_on.png` | 1,538,120 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_02.png` | 1,405,222 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_02_click_off.png` | 1,249,678 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_02_click_on.png` | 1,249,941 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_03.png` | 227,925 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_02_04.png` | 1,459,148 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_01.png` | 1,704,772 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_02.png` | 948,803 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_03.png` | 115,766 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_03_01.png` | 798,498 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_03_02.png` | 806,540 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_03_03.png` | 806,957 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_03_04.png` | 806,003 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_04.png` | 114,308 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_05.png` | 114,833 | 파일 크기/참조 검사 |
| `en/gaia/img/location_img_03_06.png` | 113,024 | 파일 크기/참조 검사 |
| `en/gaia/img/logo.png` | 3,797 | 파일 크기/참조 검사 |
| `en/gaia/img/logo_gaia.jpg` | 18,188 | 파일 크기/참조 검사 |
| `en/gaia/img/lpay_logo.png` | 1,393 | 파일 크기/참조 검사 |
| `en/gaia/img/m_logo.png` | 3,100 | 파일 크기/참조 검사 |
| `en/gaia/img/main_1.mp4` | 9,516,000 | 파일 크기/참조 검사 |
| `en/gaia/img/main_1_ko.mp4` | 20,469,695 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_1_v.mp4` | 10,485,194 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_1_v_ko.mp4` | 11,291,274 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_2.mp4` | 10,515,067 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_2_ko.mp4` | 58,516,537 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_2_v.mp4` | 10,531,343 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_2_v_ko.mp4` | 14,360,051 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_3.mp4` | 11,124,442 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_3_ko.mp4` | 30,498,805 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_3_v.mp4` | 11,033,733 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_3_v_ko.mp4` | 13,165,355 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_4.mp4` | 10,874,713 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_4_ko.mp4` | 68,228,680 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_4_v.mp4` | 10,665,223 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/main_4_v_ko.mp4` | 10,319,879 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/gaia/img/mobile/btn_close.png` | 3,265 | 파일 크기/참조 검사 |
| `en/gaia/img/mobile/gnb_bg.png` | 1,012 | 파일 크기/참조 검사 |
| `en/gaia/img/mobile/gnb_bg2.png` | 976 | 파일 크기/참조 검사 |
| `en/gaia/img/mobile/gnb_sch.png` | 1,795 | 파일 크기/참조 검사 |
| `en/gaia/img/mobile/icon_menu.png` | 1,090 | 파일 크기/참조 검사 |
| `en/gaia/img/mobile/icon_my.png` | 1,634 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_01_01.png` | 548,555 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_01_02.png` | 717,462 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_01_02_01.png` | 483,292 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_01_02_02.png` | 464,687 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_01_03.png` | 576,995 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_02.png` | 1,361,676 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_02_01.png` | 1,318,258 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_02_02.png` | 54,650 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_02_03.png` | 56,953 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_02_04.png` | 60,257 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_03_01.png` | 1,477,584 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_03_02.png` | 289,861 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_03_03.png` | 230,838 | 파일 크기/참조 검사 |
| `en/gaia/img/model_img_03_04.png` | 812,589 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_01_01.png` | 376,953 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_01_02.png` | 326,247 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_01_03.png` | 56,866 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_01_04.png` | 459,715 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_02_01.png` | 777,808 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_02_02.png` | 913,580 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_02_03.png` | 794,299 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_02_04.png` | 668,213 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_01.png` | 1,281,753 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_02.png` | 1,021,853 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_03.png` | 950,246 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_04.png` | 253,390 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_05.png` | 179,530 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_06.png` | 776,210 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_07.png` | 802,556 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_08.png` | 1,011,609 | 파일 크기/참조 검사 |
| `en/gaia/img/modify_img_03_09.png` | 1,014,051 | 파일 크기/참조 검사 |
| `en/gaia/img/more-btn.gif` | 1,204 | 파일 크기/참조 검사 |
| `en/gaia/img/no_img.png` | 991 | 파일 크기/참조 검사 |
| `en/gaia/img/no_profile.gif` | 1,953 | 파일 크기/참조 검사 |
| `en/gaia/img/og-main-thumb.JPG` | 182,485 | 파일 크기/참조 검사 |
| `en/gaia/img/pay_icon1.png` | 1,676 | 파일 크기/참조 검사 |
| `en/gaia/img/pay_icon2.png` | 1,703 | 파일 크기/참조 검사 |
| `en/gaia/img/pay_icon3.png` | 1,174 | 파일 크기/참조 검사 |
| `en/gaia/img/pay_icon4.png` | 1,185 | 파일 크기/참조 검사 |
| `en/gaia/img/payco.png` | 2,326 | 파일 크기/참조 검사 |
| `en/gaia/img/payco_logo.png` | 711 | 파일 크기/참조 검사 |
| `en/gaia/img/paynow.png` | 2,387 | 파일 크기/참조 검사 |
| `en/gaia/img/paynow_logo.png` | 679 | 파일 크기/참조 검사 |
| `en/gaia/img/primary_01.png` | 959,337 | 파일 크기/참조 검사 |
| `en/gaia/img/primary_02.png` | 1,347,298 | 파일 크기/참조 검사 |
| `en/gaia/img/primary_03.png` | 1,333,641 | 파일 크기/참조 검사 |
| `en/gaia/img/primary_block_bg.png` | 906,391 | 파일 크기/참조 검사 |
| `en/gaia/img/primary_intro_bg.jpg` | 1,012,187 | 파일 크기/참조 검사 |
| `en/gaia/img/require.png` | 2,922 | 파일 크기/참조 검사 |
| `en/gaia/img/results_intro_bg.png` | 1,067,582 | 파일 크기/참조 검사 |
| `en/gaia/img/road_conclusion_bg.jpg` | 8,826,947 | 파일 크기/참조 검사 |
| `en/gaia/img/sample_video.jpg` | 255,486 | 파일 크기/참조 검사 |
| `en/gaia/img/samsungpay.png` | 2,071 | 파일 크기/참조 검사 |
| `en/gaia/img/sch_btn.png` | 1,234 | 파일 크기/참조 검사 |
| `en/gaia/img/sitemap_menu01.jpg` | 1,002,893 | 파일 크기/참조 검사 |
| `en/gaia/img/sitemap_menu02.jpg` | 618,118 | 파일 크기/참조 검사 |
| `en/gaia/img/sitemap_menu03.jpg` | 335,497 | 파일 크기/참조 검사 |
| `en/gaia/img/sitemap_menu04.jpg` | 315,822 | 파일 크기/참조 검사 |
| `en/gaia/img/skpay11_icon.png` | 7,920 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_04_02.png` | 629,139 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_04_03.png` | 819,680 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_fix_bg.png` | 317,387 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_01.png` | 4,235,308 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_01_01.png` | 12,263 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_01_01_m.png` | 6,051 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_01_03.png` | 314,848 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_01_03_m.png` | 136,473 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_01_03_m_.png` | 128,357 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_01_m.png` | 1,940,084 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_02.png` | 668,937 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_02_01.png` | 9,730 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_02_01_m.png` | 4,591 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_02_02.png` | 11,180 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_02_03.png` | 418,812 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_02_03_m.png` | 176,383 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_02_m.png` | 368,083 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03.png` | 849,446 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_01.png` | 12,025 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_01_m.png` | 5,871 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_02.png` | 11,192 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_03.png` | 425,914 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_03_m.png` | 289,819 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_04.png` | 489,456 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_04_m.png` | 265,226 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_03_m.png` | 444,778 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_04.png` | 632,083 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_04_01.png` | 10,619 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_04_01_m.png` | 4,961 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_04_02.png` | 11,192 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_04_03.png` | 674,263 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_04_03_m.png` | 355,018 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_04_m.png` | 370,907 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_05.png` | 432,448 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_05_01.png` | 10,333 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_05_01_m.png` | 5,464 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_05_02.png` | 11,202 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_05_03.png` | 683,588 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_05_03_m.png` | 368,861 | 파일 크기/참조 검사 |
| `en/gaia/img/slide_img_05_m.png` | 268,701 | 파일 크기/참조 검사 |
| `en/gaia/img/ssgpay_icon.png` | 1,887 | 파일 크기/참조 검사 |
| `en/gaia/img/tnb_shop.jpg` | 881 | 파일 크기/참조 검사 |
| `en/gaia/img/tri_img.svg` | 888 | 파일 크기/참조 검사 |
| `en/gaia/img/ts01.gif` | 138 | 파일 크기/참조 검사 |
| `en/gaia/img/ts01.png` | 1,219 | 파일 크기/참조 검사 |
| `en/gaia/img/ts02.gif` | 148 | 파일 크기/참조 검사 |
| `en/gaia/img/ts02.png` | 1,252 | 파일 크기/참조 검사 |
| `en/gaia/img/ts03.gif` | 154 | 파일 크기/참조 검사 |
| `en/gaia/img/ts03.png` | 1,319 | 파일 크기/참조 검사 |
| `en/gaia/img/value_arrow_down.svg` | 10,635 | 파일 크기/참조 검사 |
| `en/gaia/img/value_arrow_down_m.svg` | 3,338 | 파일 크기/참조 검사 |
| `en/gaia/img/value_arrow_left.svg` | 1,983 | 파일 크기/참조 검사 |
| `en/gaia/img/value_arrow_left_m.svg` | 927 | 파일 크기/참조 검사 |
| `en/gaia/img/value_feature_bg.jpg` | 415,702 | 파일 크기/참조 검사 |
| `en/gaia/img/value_feature_bg_m.jpg` | 207,352 | 파일 크기/참조 검사 |
| `en/gaia/img/value_feature_data_bg.jpg` | 748,770 | 파일 크기/참조 검사 |
| `en/gaia/img/value_feature_design_bg.jpg` | 349,982 | 파일 크기/참조 검사 |
| `en/gaia/img/value_feature_devices_bg.jpg` | 418,143 | 파일 크기/참조 검사 |
| `en/gaia/img/value_intro_bg_bottom.png` | 1,256,598 | 파일 크기/참조 검사 |
| `en/gaia/img/value_intro_bg_top.png` | 4,500,150 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen1.jpg` | 605,917 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen1.png` | 1,249,763 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen2.jpg` | 565,249 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen3.jpg` | 932,185 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen4.jpg` | 651,106 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screenM_01.png` | 95,326 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screenM_02.png` | 1,081,755 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screenM_03.png` | 309,369 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screenM_04.png` | 613,779 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screenM_05.png` | 125,698 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen_bg.png` | 1,713,477 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen_bg_m.png` | 1,744,016 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen_tab1.svg` | 744 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen_tab2.svg` | 802 | 파일 크기/참조 검사 |
| `en/gaia/img/value_screen_tab3.svg` | 787 | 파일 크기/참조 검사 |
| `en/gaia/img/wrest.gif` | 51 | 파일 크기/참조 검사 |
| `en/gaia/index.html` | 4,125 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/gaia/js/further.js` | 5,222 | 텍스트 리소스 참조 검사 |
| `en/gaia/js/index.js` | 5,725 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `en/gaia/js/jquery-3.6.1.min.js` | 89,664 | 텍스트 리소스 참조 검사 |
| `en/gaia/js/jquery.mousewheel.min.js` | 2,680 | 텍스트 리소스 참조 검사 |
| `en/gaia/js/primary.js` | 6,137 | 텍스트 리소스 참조 검사 |
| `en/gaia/js/results.js` | 5,333 | 텍스트 리소스 참조 검사 |
| `en/gaia/js/value.js` | 6,002 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `en/gaia/primary.html` | 20,422 | HTML: 동기 외부 스크립트 9, 이미지 32 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/gaia/results.html` | 18,260 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/gaia/value.html` | 19,736 | HTML: 동기 외부 스크립트 9, 이미지 6 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/hosting_index1.html` | 2,143 | HTML: 동기 외부 스크립트 0, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 2 |
| `en/index.html` | 1,744 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/pr_brochure.html` | 6,013 | HTML: 동기 외부 스크립트 7, 이미지 11 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/pr_ci.html` | 7,203 | HTML: 동기 외부 스크립트 8, 이미지 5 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `en/pr_news.html` | 10,133 | HTML: 동기 외부 스크립트 8, 이미지 4 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/pr_news_view_251127.html` | 6,641 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/pr_news_view_260121.html` | 6,017 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/pr_news_view_260519.html` | 5,406 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/pr_news_view_260527.html` | 6,830 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/sv_bigroom.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/sv_solution.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/sv_solution_construction.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/sv_solution_operation.html` | 1,216 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/sv_sw.html` | 5,434 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `en/sv_sw_egbim.html` | 3,698 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `en/sv_sw_gaia.html` | 3,704 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `en/sv_sw_ipipes.html` | 3,455 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `en/sv_sw_kngil.html` | 3,513 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `en/sv_sw_pq_program.html` | 3,513 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `en/tova/.htaccess` | 327 | 파일 크기/참조 검사 |
| `en/tova/buy.html` | 40,542 | HTML: 동기 외부 스크립트 9, 이미지 1 (lazy 0), video 1, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/tova/css/font.css` | 1,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `en/tova/css/reset.css` | 2,221 | 텍스트 리소스 참조 검사 |
| `en/tova/css/style.css` | 200,207 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `en/tova/download/TOVA.zip` | 157,598,645 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/tova/download/TOVA_leaflet.pdf` | 1,996,565 | 파일 크기/참조 검사 |
| `en/tova/download/TOVA_manual.pdf` | 12,226,439 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/tova/font/NotoKR-Black/notokr-black.woff` | 180,348 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Black/notokr-black.woff2` | 128,720 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Bold/notokr-bold.woff` | 185,412 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Bold/notokr-bold.woff2` | 134,968 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Light/notokr-light.woff` | 185,532 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Light/notokr-light.woff2` | 131,096 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Medium/notokr-medium.woff` | 185,440 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Medium/notokr-medium.woff2` | 133,836 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Regular/notokr-regular.woff` | 187,364 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Regular/notokr-regular.woff2` | 134,960 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Thin/notokr-thin.woff` | 175,184 | 파일 크기/참조 검사 |
| `en/tova/font/NotoKR-Thin/notokr-thin.woff2` | 120,720 | 파일 크기/참조 검사 |
| `en/tova/img/arrow_r.svg` | 167 | 파일 크기/참조 검사 |
| `en/tova/img/asset_search.svg` | 1,721 | 파일 크기/참조 검사 |
| `en/tova/img/atom_line.svg` | 1,633 | 파일 크기/참조 검사 |
| `en/tova/img/atom_obj.svg` | 1,939 | 파일 크기/참조 검사 |
| `en/tova/img/baron_logo_eng.svg` | 9,591 | 파일 크기/참조 검사 |
| `en/tova/img/bg_close.png` | 1,280 | 파일 크기/참조 검사 |
| `en/tova/img/bg_pop.png` | 3,480,588 | 파일 크기/참조 검사 |
| `en/tova/img/buy_intro_bg.jpg` | 727,741 | 파일 크기/참조 검사 |
| `en/tova/img/buy_vdieo.mp4` | 31,954,132 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/tova/img/faq_intro_bg.png` | 933,519 | 파일 크기/참조 검사 |
| `en/tova/img/ico_angle.svg` | 243 | 파일 크기/참조 검사 |
| `en/tova/img/ico_answer.svg` | 294 | 파일 크기/참조 검사 |
| `en/tova/img/ico_buy_alarm.svg` | 929 | 파일 크기/참조 검사 |
| `en/tova/img/ico_buy_brochure.svg` | 2,196 | 파일 크기/참조 검사 |
| `en/tova/img/ico_buy_manual.svg` | 1,638 | 파일 크기/참조 검사 |
| `en/tova/img/ico_cafe.svg` | 1,171 | 파일 크기/참조 검사 |
| `en/tova/img/ico_change.svg` | 958 | 파일 크기/참조 검사 |
| `en/tova/img/ico_close.svg` | 196 | 파일 크기/참조 검사 |
| `en/tova/img/ico_company.svg` | 887 | 파일 크기/참조 검사 |
| `en/tova/img/ico_complete.svg` | 1,088 | 파일 크기/참조 검사 |
| `en/tova/img/ico_countdown.svg` | 4,119 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_bus.svg` | 1,500 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_data.svg` | 428 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_modal.svg` | 600 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_network.svg` | 3,849 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_proportionality.svg` | 1,078 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_public.svg` | 1,657 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_subway.svg` | 2,152 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dia_trans.svg` | 1,271 | 파일 크기/참조 검사 |
| `en/tova/img/ico_dublecheck.svg` | 1,680 | 파일 크기/참조 검사 |
| `en/tova/img/ico_email.svg` | 1,146 | 파일 크기/참조 검사 |
| `en/tova/img/ico_facebook.svg` | 952 | 파일 크기/참조 검사 |
| `en/tova/img/ico_floating_buy.svg` | 651 | 파일 크기/참조 검사 |
| `en/tova/img/ico_floating_faq_k.svg` | 1,115 | 파일 크기/참조 검사 |
| `en/tova/img/ico_floating_faq_w.svg` | 1,173 | 파일 크기/참조 검사 |
| `en/tova/img/ico_footer_close.svg` | 333 | 파일 크기/참조 검사 |
| `en/tova/img/ico_id.svg` | 1,018 | 파일 크기/참조 검사 |
| `en/tova/img/ico_language.svg` | 1,324 | 파일 크기/참조 검사 |
| `en/tova/img/ico_link.svg` | 791 | 파일 크기/참조 검사 |
| `en/tova/img/ico_link_b.svg` | 789 | 파일 크기/참조 검사 |
| `en/tova/img/ico_lock.svg` | 1,607 | 파일 크기/참조 검사 |
| `en/tova/img/ico_network.svg` | 1,574 | 파일 크기/참조 검사 |
| `en/tova/img/ico_network_bulit.svg` | 219 | 파일 크기/참조 검사 |
| `en/tova/img/ico_pg_left.svg` | 1,056 | 파일 크기/참조 검사 |
| `en/tova/img/ico_pg_right.svg` | 1,046 | 파일 크기/참조 검사 |
| `en/tova/img/ico_phone.svg` | 727 | 파일 크기/참조 검사 |
| `en/tova/img/ico_primary_pub01.svg` | 1,344 | 파일 크기/참조 검사 |
| `en/tova/img/ico_primary_pub02.svg` | 4,311 | 파일 크기/참조 검사 |
| `en/tova/img/ico_primary_pub03.svg` | 990 | 파일 크기/참조 검사 |
| `en/tova/img/ico_primary_pub04.svg` | 359 | 파일 크기/참조 검사 |
| `en/tova/img/ico_pub_slide_01.svg` | 425 | 파일 크기/참조 검사 |
| `en/tova/img/ico_pub_slide_02.svg` | 403 | 파일 크기/참조 검사 |
| `en/tova/img/ico_pub_slide_03.svg` | 450 | 파일 크기/참조 검사 |
| `en/tova/img/ico_public_od.svg` | 983 | 파일 크기/참조 검사 |
| `en/tova/img/ico_public_pay.svg` | 797 | 파일 크기/참조 검사 |
| `en/tova/img/ico_public_station.svg` | 917 | 파일 크기/참조 검사 |
| `en/tova/img/ico_pw.svg` | 1,185 | 파일 크기/참조 검사 |
| `en/tova/img/ico_refresh.svg` | 566 | 파일 크기/참조 검사 |
| `en/tova/img/ico_send_email.svg` | 634 | 파일 크기/참조 검사 |
| `en/tova/img/ico_signout.svg` | 933 | 파일 크기/참조 검사 |
| `en/tova/img/ico_slide_bus.svg` | 2,080 | 파일 크기/참조 검사 |
| `en/tova/img/ico_slide_subway.svg` | 2,403 | 파일 크기/참조 검사 |
| `en/tova/img/ico_slide_trans.svg` | 1,056 | 파일 크기/참조 검사 |
| `en/tova/img/ico_social.svg` | 2,381 | 파일 크기/참조 검사 |
| `en/tova/img/ico_sync.svg` | 847 | 파일 크기/참조 검사 |
| `en/tova/img/ico_value_cursor.svg` | 1,810 | 파일 크기/참조 검사 |
| `en/tova/img/ico_value_frog_w.svg` | 2,968 | 파일 크기/참조 검사 |
| `en/tova/img/ico_value_ktdb_w.svg` | 1,550 | 파일 크기/참조 검사 |
| `en/tova/img/ico_value_public_w.svg` | 1,467 | 파일 크기/참조 검사 |
| `en/tova/img/ico_value_screen.svg` | 1,742 | 파일 크기/참조 검사 |
| `en/tova/img/ico_value_user_w.svg` | 2,059 | 파일 크기/참조 검사 |
| `en/tova/img/ico_way.svg` | 974 | 파일 크기/참조 검사 |
| `en/tova/img/ico_won.svg` | 1,573 | 파일 크기/참조 검사 |
| `en/tova/img/main_01.mp4` | 20,764,328 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `en/tova/img/primary_01.png` | 1,818,762 | 파일 크기/참조 검사 |
| `en/tova/img/primary_01_01.png` | 463,130 | 파일 크기/참조 검사 |
| `en/tova/img/primary_01_02.png` | 499,996 | 파일 크기/참조 검사 |
| `en/tova/img/primary_01_03.png` | 432,100 | 파일 크기/참조 검사 |
| `en/tova/img/primary_02.png` | 1,113,839 | 파일 크기/참조 검사 |
| `en/tova/img/primary_02_04.png` | 210,783 | 파일 크기/참조 검사 |
| `en/tova/img/primary_02_04.svg` | 2,350,528 | 파일 크기/참조 검사 |
| `en/tova/img/primary_03.png` | 1,493,077 | 파일 크기/참조 검사 |
| `en/tova/img/primary_03_01.png` | 675,653 | 파일 크기/참조 검사 |
| `en/tova/img/primary_intro_bg.jpg` | 1,374,244 | 파일 크기/참조 검사 |
| `en/tova/img/pub_01_01.svg` | 1,061,104 | 파일 크기/참조 검사 |
| `en/tova/img/pub_02_01.png` | 885,214 | 파일 크기/참조 검사 |
| `en/tova/img/pub_03_01.svg` | 1,186,945 | 파일 크기/참조 검사 |
| `en/tova/img/pub_04_01.png` | 215,850 | 파일 크기/참조 검사 |
| `en/tova/img/pub_slide_01.svg` | 14,324 | 파일 크기/참조 검사 |
| `en/tova/img/pub_slide_02.svg` | 14,296 | 파일 크기/참조 검사 |
| `en/tova/img/pub_slide_03.svg` | 14,107 | 파일 크기/참조 검사 |
| `en/tova/img/public_intro_bg.jpg` | 1,227,248 | 파일 크기/참조 검사 |
| `en/tova/img/public_od_bg.png` | 5,752,538 | 파일 크기/참조 검사 |
| `en/tova/img/public_pay_bg.png` | 5,512,213 | 파일 크기/참조 검사 |
| `en/tova/img/public_process_01.svg` | 2,558,063 | 파일 크기/참조 검사 |
| `en/tova/img/public_process_02.svg` | 1,512,874 | 파일 크기/참조 검사 |
| `en/tova/img/public_process_03.svg` | 1,988,424 | 파일 크기/참조 검사 |
| `en/tova/img/public_station_bg.png` | 5,171,780 | 파일 크기/참조 검사 |
| `en/tova/img/road_conclusion_bg.jpg` | 2,501,320 | 파일 크기/참조 검사 |
| `en/tova/img/road_frog1.jpg` | 537,110 | 파일 크기/참조 검사 |
| `en/tova/img/road_frog2.jpg` | 375,279 | 파일 크기/참조 검사 |
| `en/tova/img/road_frog_markup.svg` | 54,539 | 파일 크기/참조 검사 |
| `en/tova/img/road_intro_bg.jpg` | 1,402,015 | 파일 크기/참조 검사 |
| `en/tova/img/road_process_bg1.jpg` | 356,883 | 파일 크기/참조 검사 |
| `en/tova/img/road_process_bg2.jpg` | 366,423 | 파일 크기/참조 검사 |
| `en/tova/img/road_process_soba.svg` | 34,825 | 파일 크기/참조 검사 |
| `en/tova/img/road_process_warm_bg.svg` | 4,240 | 파일 크기/참조 검사 |
| `en/tova/img/road_process_warm_fig1.svg` | 6,894 | 파일 크기/참조 검사 |
| `en/tova/img/road_process_warm_fig2.svg` | 3,687 | 파일 크기/참조 검사 |
| `en/tova/img/road_proportionality_bg.jpg` | 374,805 | 파일 크기/참조 검사 |
| `en/tova/img/road_proportionality_fig1.svg` | 836,352 | 파일 크기/참조 검사 |
| `en/tova/img/road_proportionality_fig2.svg` | 156,873 | 파일 크기/참조 검사 |
| `en/tova/img/road_theorys_algo.svg` | 7,752 | 파일 크기/참조 검사 |
| `en/tova/img/road_theorys_bg.jpg` | 2,254,517 | 파일 크기/참조 검사 |
| `en/tova/img/road_theorys_modal.svg` | 5,589 | 파일 크기/참조 검사 |
| `en/tova/img/road_tova.svg` | 1,096 | 파일 크기/참조 검사 |
| `en/tova/img/sitemap_menu01.jpg` | 2,526,307 | 파일 크기/참조 검사 |
| `en/tova/img/sitemap_menu02.jpg` | 2,193,661 | 파일 크기/참조 검사 |
| `en/tova/img/sitemap_menu03.jpg` | 1,557,231 | 파일 크기/참조 검사 |
| `en/tova/img/sitemap_menu04.jpg` | 1,455,733 | 파일 크기/참조 검사 |
| `en/tova/img/slide_img_bus.png` | 1,592,555 | 파일 크기/참조 검사 |
| `en/tova/img/slide_img_subway.png` | 1,996,522 | 파일 크기/참조 검사 |
| `en/tova/img/slide_img_trans.png` | 1,634,816 | 파일 크기/참조 검사 |
| `en/tova/img/tova_k.svg` | 1,099 | 파일 크기/참조 검사 |
| `en/tova/img/tova_obj_k.svg` | 448 | 파일 크기/참조 검사 |
| `en/tova/img/tova_obj_w.svg` | 318 | 파일 크기/참조 검사 |
| `en/tova/img/tova_w.svg` | 1,066 | 파일 크기/참조 검사 |
| `en/tova/img/tri_img.svg` | 888 | 파일 크기/참조 검사 |
| `en/tova/img/value_feature_bg.jpg` | 799,271 | 파일 크기/참조 검사 |
| `en/tova/img/value_feature_frog_bg.jpg` | 747,969 | 파일 크기/참조 검사 |
| `en/tova/img/value_feature_ktdb_bg.jpg` | 434,092 | 파일 크기/참조 검사 |
| `en/tova/img/value_feature_public_bg.jpg` | 512,907 | 파일 크기/참조 검사 |
| `en/tova/img/value_feature_user_bg.jpg` | 277,532 | 파일 크기/참조 검사 |
| `en/tova/img/value_intro_bg.jpg` | 1,954,590 | 파일 크기/참조 검사 |
| `en/tova/img/value_intro_summary1.png` | 769,611 | 파일 크기/참조 검사 |
| `en/tova/img/value_intro_summary2.jpg` | 1,375,068 | 파일 크기/참조 검사 |
| `en/tova/img/value_screen1.png` | 587,131 | 파일 크기/참조 검사 |
| `en/tova/img/value_screen2.png` | 565,370 | 파일 크기/참조 검사 |
| `en/tova/img/value_screenM_01.png` | 144,980 | 파일 크기/참조 검사 |
| `en/tova/img/value_screenM_02.png` | 286,803 | 파일 크기/참조 검사 |
| `en/tova/img/value_screenM_03.png` | 216,104 | 파일 크기/참조 검사 |
| `en/tova/img/value_screen_bg.svg` | 9,792 | 파일 크기/참조 검사 |
| `en/tova/img/value_system_bg.jpg` | 1,254,858 | 파일 크기/참조 검사 |
| `en/tova/img/zone_01_01.png` | 352,261 | 파일 크기/참조 검사 |
| `en/tova/img/zone_01_02.png` | 211,111 | 파일 크기/참조 검사 |
| `en/tova/img/zone_01_03.svg` | 19,213 | 파일 크기/참조 검사 |
| `en/tova/img/zone_01_04.svg` | 14,026 | 파일 크기/참조 검사 |
| `en/tova/img/zone_02_01.png` | 599,609 | 파일 크기/참조 검사 |
| `en/tova/img/zone_03_01.png` | 369,812 | 파일 크기/참조 검사 |
| `en/tova/index.html` | 41,025 | HTML: 동기 외부 스크립트 10, 이미지 1 (lazy 0), video 1, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 1 |
| `en/tova/js/common.js` | 86,855 | 텍스트 리소스 참조 검사; 외부 URL 12, 로컬 참조 확인 필요 1 |
| `en/tova/js/index.js` | 6,730 | 텍스트 리소스 참조 검사 |
| `en/tova/js/jquery-3.6.1.min.js` | 89,664 | 텍스트 리소스 참조 검사 |
| `en/tova/js/jquery.mousewheel.min.js` | 2,680 | 텍스트 리소스 참조 검사 |
| `en/tova/js/popup.js` | 8,548 | 텍스트 리소스 참조 검사 |
| `en/tova/js/primary.js` | 7,155 | 텍스트 리소스 참조 검사 |
| `en/tova/js/public.js` | 4,461 | 텍스트 리소스 참조 검사 |
| `en/tova/js/road.js` | 3,957 | 텍스트 리소스 참조 검사 |
| `en/tova/js/value.js` | 8,182 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 4 |
| `en/tova/primary.html` | 57,219 | HTML: 동기 외부 스크립트 10, 이미지 28 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/tova/public.html` | 47,675 | HTML: 동기 외부 스크립트 10, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/tova/road.html` | 51,749 | HTML: 동기 외부 스크립트 10, 이미지 6 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/tova/value.html` | 53,940 | HTML: 동기 외부 스크립트 10, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `en/video_ex.html` | 2,013 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `index.html` | 520 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/Vector 3196.svg` | 1,074 | 파일 크기/참조 검사 |
| `ko/br_future.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/br_future_bak_250610.html` | 9,673 | HTML: 동기 외부 스크립트 7, 이미지 10 (lazy 0), video 1, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/br_future_bak_251103.html` | 13,849 | HTML: 동기 외부 스크립트 7, 이미지 10 (lazy 0), video 1, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/br_tech.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/br_tech_bak_251103.html` | 14,135 | HTML: 동기 외부 스크립트 8, 이미지 28 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/br_value.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/dt_explain.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/dt_sw.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/dt_use.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/dx.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/dx_250612.html` | 4,186 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0 |
| `ko/egbim/buy.html` | 3,499 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 3 |
| `ko/egbim/css/default.css` | 0 | 텍스트 리소스 참조 검사 |
| `ko/egbim/css/default_shop.css` | 88,628 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `ko/egbim/css/font.css` | 1,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `ko/egbim/css/mobile.css` | 22,838 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `ko/egbim/css/mobile_shop.css` | 74,767 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/reset.css` | 2,193 | 텍스트 리소스 참조 검사 |
| `ko/egbim/css/slickslider/slick-theme.css` | 3,349 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `ko/egbim/css/slickslider/slick.css` | 1,895 | 텍스트 리소스 참조 검사 |
| `ko/egbim/css/stickyOnTable.css` | 497 | 텍스트 리소스 참조 검사 |
| `ko/egbim/css/style copy.css` | 69,809 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 37 |
| `ko/egbim/css/style.css` | 226,473 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/style_240911.css` | 105,228 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/style_240927.css` | 109,645 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/style_250203.css` | 110,556 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `ko/egbim/css/style_250307.css` | 163,943 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/style_250310.css` | 163,960 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/style_250312.css` | 164,116 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/style_260526.css` | 226,017 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/css/style_sales.css` | 4,109 | 텍스트 리소스 참조 검사 |
| `ko/egbim/floorplan.html` | 14,986 | HTML: 동기 외부 스크립트 9, 이미지 27 (lazy 0), video 0, iframe 0; 외부 URL 7, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Black/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Black/notokr-black-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/egbim/font/NotoKR-Black/notokr-black.eot` | 149,951 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Black/notokr-black.svg` | 703,668 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Black/notokr-black.ttf` | 358,600 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Black/notokr-black.woff` | 180,348 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Black/notokr-black.woff2` | 128,720 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Black/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Black/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Black/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Black/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Bold/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Bold/notokr-bold-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/egbim/font/NotoKR-Bold/notokr-bold.eot` | 156,008 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Bold/notokr-bold.svg` | 705,999 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Bold/notokr-bold.ttf` | 359,412 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Bold/notokr-bold.woff` | 185,412 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Bold/notokr-bold.woff2` | 134,968 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Bold/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Bold/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Bold/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Bold/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-DemiLight/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 173,863 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/egbim/font/NotoKR-DemiLight/notokr-demilight.eot` | 155,464 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/notokr-demilight.svg` | 733,933 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/notokr-demilight.ttf` | 369,728 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/notokr-demilight.woff` | 187,464 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/notokr-demilight.woff2` | 133,772 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-DemiLight/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-DemiLight/stylesheet.css` | 547 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Light/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Light/notokr-light-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/egbim/font/NotoKR-Light/notokr-light.eot` | 153,179 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Light/notokr-light.svg` | 748,368 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Light/notokr-light.ttf` | 373,820 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Light/notokr-light.woff` | 185,532 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Light/notokr-light.woff2` | 131,096 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Light/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Light/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Light/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Light/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Medium/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Medium/notokr-medium-demo.html` | 173,842 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/egbim/font/NotoKR-Medium/notokr-medium.eot` | 155,800 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Medium/notokr-medium.svg` | 717,209 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Medium/notokr-medium.ttf` | 364,276 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Medium/notokr-medium.woff` | 185,440 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Medium/notokr-medium.woff2` | 133,836 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Medium/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Medium/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Medium/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Medium/stylesheet.css` | 523 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Regular/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Regular/notokr-regular-demo.html` | 173,868 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/egbim/font/NotoKR-Regular/notokr-regular.eot` | 156,734 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Regular/notokr-regular.svg` | 727,332 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Regular/notokr-regular.ttf` | 367,940 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Regular/notokr-regular.woff` | 187,364 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Regular/notokr-regular.woff2` | 134,960 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Regular/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Regular/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Regular/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Regular/stylesheet.css` | 531 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Thin/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Thin/notokr-thin-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/egbim/font/NotoKR-Thin/notokr-thin.eot` | 143,518 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Thin/notokr-thin.svg` | 761,397 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Thin/notokr-thin.ttf` | 377,440 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Thin/notokr-thin.woff` | 175,184 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Thin/notokr-thin.woff2` | 120,720 | 파일 크기/참조 검사 |
| `ko/egbim/font/NotoKR-Thin/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Thin/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/egbim/font/NotoKR-Thin/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/font/NotoKR-Thin/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/forbim.html` | 6,963 | HTML: 동기 외부 스크립트 9, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 7, 로컬 참조 확인 필요 0 |
| `ko/egbim/img/EGBIM_buy.mp4` | 42,045,445 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/egbim/img/Subtract2.svg` | 1,693 | 파일 크기/참조 검사 |
| `ko/egbim/img/Thumbs.db` | 338,944 | 파일 크기/참조 검사 |
| `ko/egbim/img/arrow_r.svg` | 167 | 파일 크기/참조 검사 |
| `ko/egbim/img/asset_search.svg` | 1,658 | 파일 크기/참조 검사 |
| `ko/egbim/img/atom_line.svg` | 1,525 | 파일 크기/참조 검사 |
| `ko/egbim/img/atom_obj.svg` | 1,936 | 파일 크기/참조 검사 |
| `ko/egbim/img/baron_logo.svg` | 6,233 | 파일 크기/참조 검사 |
| `ko/egbim/img/bg_close.png` | 898 | 파일 크기/참조 검사 |
| `ko/egbim/img/bg_pop.png` | 1,795,801 | 파일 크기/참조 검사 |
| `ko/egbim/img/block_img_01.png` | 51,252 | 파일 크기/참조 검사 |
| `ko/egbim/img/block_img_02.png` | 90,967 | 파일 크기/참조 검사 |
| `ko/egbim/img/block_img_ico.svg` | 4,910 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_end.gif` | 1,176 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_first.gif` | 1,885 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_idx_left.png` | 3,141 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_idx_right.png` | 442 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_next.gif` | 1,169 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_prev.gif` | 1,873 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_search.jpg` | 782 | 파일 크기/참조 검사 |
| `ko/egbim/img/btn_top.gif` | 1,178 | 파일 크기/참조 검사 |
| `ko/egbim/img/bullet.gif` | 1,165 | 파일 크기/참조 검사 |
| `ko/egbim/img/buy_intro_bg.png` | 1,186,792 | 파일 크기/참조 검사 |
| `ko/egbim/img/captcha.png` | 4,886 | 파일 크기/참조 검사 |
| `ko/egbim/img/captcha2.png` | 4,886 | 파일 크기/참조 검사 |
| `ko/egbim/img/chk.png` | 1,070 | 파일 크기/참조 검사 |
| `ko/egbim/img/close_btn.gif` | 1,209 | 파일 크기/참조 검사 |
| `ko/egbim/img/close_btn.png` | 1,147 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/Thumbs.db` | 522,752 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_1.png` | 729,470 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_10.png` | 361,340 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_100.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_101.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_102.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_103.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_104.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_11.png` | 145,644 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_12.png` | 14,091 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_13.png` | 17,110 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_14.png` | 92,527 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_15.png` | 144,244 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_16.png` | 188,767 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_17.png` | 221,944 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_18.png` | 254,233 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_19.png` | 317,194 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_2.png` | 727,547 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_20.png` | 397,369 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_21.png` | 468,221 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_22.png` | 502,992 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_23.png` | 503,362 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_24.png` | 500,551 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_25.png` | 500,422 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_26.png` | 503,390 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_27.png` | 502,812 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_28.png` | 503,077 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_29.png` | 541,028 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_3.png` | 729,358 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_30.png` | 549,525 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_31.png` | 549,041 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_32.png` | 550,112 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_33.png` | 554,641 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_34.png` | 559,102 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_35.png` | 558,365 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_36.png` | 559,487 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_37.png` | 560,431 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_38.png` | 558,668 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_39.png` | 558,298 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_4.png` | 728,233 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_40.png` | 559,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_41.png` | 607,476 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_42.png` | 662,486 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_43.png` | 720,297 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_44.png` | 780,145 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_45.png` | 851,441 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_46.png` | 914,471 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_47.png` | 953,623 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_48.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_49.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_5.png` | 705,944 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_50.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_51.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_52.png` | 1,049,340 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_53.png` | 1,138,471 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_54.png` | 1,197,889 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_55.png` | 1,233,019 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_56.png` | 1,259,825 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_57.png` | 1,311,789 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_58.png` | 1,357,885 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_59.png` | 1,366,900 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_6.png` | 662,210 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_60.png` | 1,350,101 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_61.png` | 1,288,616 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_62.png` | 1,223,769 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_63.png` | 1,232,384 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_64.png` | 1,240,668 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_65.png` | 1,241,184 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_66.png` | 1,240,533 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_67.png` | 1,239,298 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_68.png` | 1,240,688 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_69.png` | 1,241,242 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_7.png` | 607,289 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_70.png` | 1,243,732 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_71.png` | 1,252,218 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_72.png` | 1,252,668 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_73.png` | 1,251,460 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_74.png` | 1,248,539 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_75.png` | 1,243,890 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_76.png` | 1,239,844 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_77.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_78.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_79.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_8.png` | 543,705 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_80.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_81.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_82.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_83.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_84.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_85.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_86.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_87.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_88.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_89.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_9.png` | 451,356 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_90.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_91.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_92.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_93.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_94.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_95.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_96.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_97.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_98.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/comp_99.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_1.png` | 719,887 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_10.png` | 353,905 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_11.png` | 138,751 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_12.png` | 14,091 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_13.png` | 17,110 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_14.png` | 94,354 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_15.png` | 136,539 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_16.png` | 172,152 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_17.png` | 196,026 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_18.png` | 226,995 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_19.png` | 291,966 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_2.png` | 718,214 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_20.png` | 377,017 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_21.png` | 450,658 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_22.png` | 486,573 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_23.png` | 485,564 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_24.png` | 483,575 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_25.png` | 483,091 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_26.png` | 485,020 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_27.png` | 484,627 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_28.png` | 484,314 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_29.png` | 513,816 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_3.png` | 720,185 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_30.png` | 521,341 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_31.png` | 521,983 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_32.png` | 523,907 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_33.png` | 527,533 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_34.png` | 530,433 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_35.png` | 530,644 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_36.png` | 530,752 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_37.png` | 530,451 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_38.png` | 530,201 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_39.png` | 528,876 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_4.png` | 718,688 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_40.png` | 529,577 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_41.png` | 578,311 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_42.png` | 632,326 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_43.png` | 691,664 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_44.png` | 750,070 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_45.png` | 822,409 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_46.png` | 885,935 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_47.png` | 924,643 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_48.png` | 933,337 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_49.png` | 933,337 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_5.png` | 696,182 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_50.png` | 933,337 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_51.png` | 933,337 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_52.png` | 1,018,986 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_53.png` | 1,105,615 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_54.png` | 1,167,019 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_55.png` | 1,202,205 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_56.png` | 1,228,821 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_57.png` | 1,282,679 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_58.png` | 1,328,125 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_59.png` | 1,339,815 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_6.png` | 652,972 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_60.png` | 1,324,725 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_61.png` | 1,268,155 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_62.png` | 1,208,699 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_63.png` | 1,216,217 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_64.png` | 1,224,438 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_65.png` | 1,224,834 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_66.png` | 1,225,298 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_67.png` | 1,223,296 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_68.png` | 1,223,801 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_69.png` | 1,224,725 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_7.png` | 599,667 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_70.png` | 1,227,958 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_71.png` | 1,236,227 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_72.png` | 1,236,625 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_73.png` | 1,235,399 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_74.png` | 1,232,301 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_75.png` | 1,227,325 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_76.png` | 1,223,203 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_77.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_78.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_79.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_8.png` | 537,125 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_80.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_81.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_82.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_83.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_84.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_85.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_86.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_87.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_88.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_89.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_9.png` | 443,417 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_90.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_91.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_92.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_93.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_94.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_95.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_96.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_97.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_98.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/com_img/eng/comp_99.png` | 1,221,411 | 파일 크기/참조 검사 |
| `ko/egbim/img/dia_valuebg01.png` | 730,776 | 파일 크기/참조 검사 |
| `ko/egbim/img/dia_valuebg02.png` | 3,809,536 | 파일 크기/참조 검사 |
| `ko/egbim/img/dia_valuebg03.png` | 195,168 | 파일 크기/참조 검사 |
| `ko/egbim/img/dual_img01_01.png` | 75,739 | 파일 크기/참조 검사 |
| `ko/egbim/img/dual_img01_02.png` | 60,751 | 파일 크기/참조 검사 |
| `ko/egbim/img/dual_img02_01.png` | 108,269 | 파일 크기/참조 검사 |
| `ko/egbim/img/dual_img02_02.png` | 33,746 | 파일 크기/참조 검사 |
| `ko/egbim/img/eee.svg` | 10,775 | 파일 크기/참조 검사 |
| `ko/egbim/img/egbim_k.svg` | 2,690 | 파일 크기/참조 검사 |
| `ko/egbim/img/egbim_logo.svg` | 13,099 | 파일 크기/참조 검사 |
| `ko/egbim/img/egbim_obj_k.svg` | 715 | 파일 크기/참조 검사 |
| `ko/egbim/img/egbim_obj_w.svg` | 698 | 파일 크기/참조 검사 |
| `ko/egbim/img/egbim_w.svg` | 4,791 | 파일 크기/참조 검사 |
| `ko/egbim/img/faq_intro_bg.png` | 933,519 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_01.png` | 122,202 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_01_01.svg` | 210,524 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_02.png` | 196,677 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_02_01.png` | 138,549 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_03.png` | 994,848 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_03_01.png` | 424,384 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_03_02.png` | 131,421 | 파일 크기/참조 검사 |
| `ko/egbim/img/find_img_03_03.png` | 31,134 | 파일 크기/참조 검사 |
| `ko/egbim/img/floating_bg.png` | 50,554 | 파일 크기/참조 검사 |
| `ko/egbim/img/floating_bg2.png` | 40,051 | 파일 크기/참조 검사 |
| `ko/egbim/img/floating_bg_4.png` | 30,679 | 파일 크기/참조 검사 |
| `ko/egbim/img/floating_bg_r4.png` | 24,497 | 파일 크기/참조 검사 |
| `ko/egbim/img/floating_bg_row4.png` | 24,497 | 파일 크기/참조 검사 |
| `ko/egbim/img/floorplan_01.png` | 1,496,234 | 파일 크기/참조 검사 |
| `ko/egbim/img/floorplan_02.png` | 379,594 | 파일 크기/참조 검사 |
| `ko/egbim/img/floorplan_03.png` | 421,584 | 파일 크기/참조 검사 |
| `ko/egbim/img/floorplan_intro_bg.png` | 409,923 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_intro_bg.png` | 3,164,915 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_process_01_1.png` | 142,533 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_process_01_2.png` | 252,994 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_process_01_3.png` | 137,277 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_process_02.png` | 270,863 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_process_bg.png` | 649,084 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_process_bg02.png` | 2,977,942 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_theorys_bg.png` | 1,051,872 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_theorys_bim.svg` | 5,157 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_theorys_plan.svg` | 8,382 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_visaul.png` | 1,245,965 | 파일 크기/참조 검사 |
| `ko/egbim/img/forbim_visual_bg.png` | 317,387 | 파일 크기/참조 검사 |
| `ko/egbim/img/ft.png` | 3,204 | 파일 크기/참조 검사 |
| `ko/egbim/img/ft_logo.png` | 3,737 | 파일 크기/참조 검사 |
| `ko/egbim/img/gnb_bg.gif` | 1,169 | 파일 크기/참조 검사 |
| `ko/egbim/img/gnb_bg00.gif` | 54 | 파일 크기/참조 검사 |
| `ko/egbim/img/gnb_bg01.gif` | 54 | 파일 크기/참조 검사 |
| `ko/egbim/img/gnb_bg2.gif` | 49 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico-default-naverpay.png` | 2,689 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico-mobile-applepay.png` | 2,063 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico-mobile-kakaopay.png` | 3,251 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico-mobile-naverpay.png` | 3,261 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_admin.svg` | 5,691 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_angle.svg` | 243 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_answer.svg` | 296 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_arrow.svg` | 488 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_buy_alarm.svg` | 929 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_buy_ask.svg` | 2,054 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_buy_brochure.svg` | 2,196 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_buy_mail.svg` | 585 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_buy_manual.svg` | 1,638 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_buy_tel.svg` | 1,093 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_cafe.svg` | 1,171 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_check.svg` | 900 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_close.svg` | 196 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_company.svg` | 887 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_complete.svg` | 1,088 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_email.svg` | 1,146 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_facebook.svg` | 952 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_find_01.svg` | 1,317 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_find_02.svg` | 2,042 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_find_03.svg` | 1,168 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_find_tri.svg` | 193 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_book.svg` | 3,903 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_book_on.svg` | 3,905 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_buy.svg` | 651 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_buy_on.svg` | 654 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_download.svg` | 678 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_download_on.svg` | 680 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_faq.svg` | 1,173 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floating_faq_on.svg` | 1,171 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floorplan_dia_01.svg` | 1,969 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floorplan_dia_02.svg` | 2,992 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_floorplan_dia_03.svg` | 2,363 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_footer_close.svg` | 333 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_forbim_check.svg` | 3,003 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_forbim_link.svg` | 3,292 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_ham.svg` | 309 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_id.svg` | 1,018 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_info_01.svg` | 4,159 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_info_02.svg` | 1,767 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_language.svg` | 1,324 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_link.svg` | 791 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_link_b.svg` | 789 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_lock.svg` | 1,609 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_my.svg` | 888 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_pg_left.svg` | 1,056 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_pg_right.svg` | 1,046 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_phone.svg` | 727 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_print_01.svg` | 919 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_print_02.svg` | 1,225 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_pripary_civil.svg` | 1,209 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_pripary_command.svg` | 3,764 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_pripary_my.svg` | 4,678 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_pw.svg` | 1,185 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_send_email.svg` | 634 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_signout.svg` | 933 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_upload.svg` | 323 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_userlist.svg` | 375 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_bim_k.svg` | 4,979 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_bim_w.svg` | 4,972 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_floorplan_k.svg` | 1,763 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_floorplan_w.svg` | 1,763 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_interface_k.svg` | 800 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_interface_w.svg` | 800 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_tool_k.svg` | 1,609 | 파일 크기/참조 검사 |
| `ko/egbim/img/ico_value_tool_w.svg` | 1,611 | 파일 크기/참조 검사 |
| `ko/egbim/img/info_img_01.png` | 144,566 | 파일 크기/참조 검사 |
| `ko/egbim/img/info_img_01_01.svg` | 5,631 | 파일 크기/참조 검사 |
| `ko/egbim/img/info_img_02.png` | 285,557 | 파일 크기/참조 검사 |
| `ko/egbim/img/info_img_02_01.png` | 69,289 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_dual_bg.png` | 531,948 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_img_01.svg` | 17,429 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_img_02.png` | 569,952 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_img_02.svg` | 705,699 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_img_03.svg` | 708,104 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_intro_bg.png` | 3,812,608 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_route_bg.png` | 317,387 | 파일 크기/참조 검사 |
| `ko/egbim/img/interface_route_screen.png` | 301,366 | 파일 크기/참조 검사 |
| `ko/egbim/img/intro_mask.svg` | 166 | 파일 크기/참조 검사 |
| `ko/egbim/img/kakao.png` | 804 | 파일 크기/참조 검사 |
| `ko/egbim/img/kpay.png` | 2,697 | 파일 크기/참조 검사 |
| `ko/egbim/img/loginBg1.jpg` | 593,676 | 파일 크기/참조 검사 |
| `ko/egbim/img/loginBg2.jpg` | 246,684 | 파일 크기/참조 검사 |
| `ko/egbim/img/loginBgTest.jpg` | 692,071 | 파일 크기/참조 검사 |
| `ko/egbim/img/loginBgTestB.jpg` | 466,966 | 파일 크기/참조 검사 |
| `ko/egbim/img/logo.png` | 3,797 | 파일 크기/참조 검사 |
| `ko/egbim/img/lpay_logo.png` | 1,393 | 파일 크기/참조 검사 |
| `ko/egbim/img/m_floating_bg_4.png` | 9,192 | 파일 크기/참조 검사 |
| `ko/egbim/img/m_logo.png` | 3,100 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_1.mp4` | 10,921,358 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/egbim/img/main_1_bak.mp4` | 16,643,306 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/img/main_1_v.mp4` | 8,328,105 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_2.mp4` | 10,616,836 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/egbim/img/main_2_bak.mp4` | 10,621,600 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/img/main_2_v.mp4` | 3,276,165 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_3.mp4` | 11,458,153 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/egbim/img/main_3_bak.mp4` | 11,688,592 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/img/main_3_v.mp4` | 7,615,012 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_4.mp4` | 10,609,637 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/egbim/img/main_4_bak.mp4` | 10,620,801 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/img/main_4_v.mp4` | 6,865,277 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_5.mp4` | 10,517,598 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/egbim/img/main_5_bak.mp4` | 7,055,091 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/img/main_5_v.mp4` | 4,401,682 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_popup/251027_main_popup.png` | 1,017,667 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_popup/251027_main_popup_m.png` | 532,029 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_popup/251128_main_popup.png` | 246,204 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_popup/251128_main_popup_m.png` | 148,568 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_popup/251223_main_popup.png` | 368,467 | 파일 크기/참조 검사 |
| `ko/egbim/img/main_popup/251223_main_popup_m.png` | 188,562 | 파일 크기/참조 검사 |
| `ko/egbim/img/mobile/btn_close.png` | 3,265 | 파일 크기/참조 검사 |
| `ko/egbim/img/mobile/gnb_bg.png` | 1,012 | 파일 크기/참조 검사 |
| `ko/egbim/img/mobile/gnb_bg2.png` | 976 | 파일 크기/참조 검사 |
| `ko/egbim/img/mobile/gnb_sch.png` | 1,795 | 파일 크기/참조 검사 |
| `ko/egbim/img/mobile/icon_menu.png` | 1,090 | 파일 크기/참조 검사 |
| `ko/egbim/img/mobile/icon_my.png` | 1,634 | 파일 크기/참조 검사 |
| `ko/egbim/img/more-btn.gif` | 1,204 | 파일 크기/참조 검사 |
| `ko/egbim/img/no_img.png` | 991 | 파일 크기/참조 검사 |
| `ko/egbim/img/no_profile.gif` | 1,953 | 파일 크기/참조 검사 |
| `ko/egbim/img/og-main-thumb.JPG` | 112,930 | 파일 크기/참조 검사 |
| `ko/egbim/img/pay_icon1.png` | 1,676 | 파일 크기/참조 검사 |
| `ko/egbim/img/pay_icon2.png` | 1,703 | 파일 크기/참조 검사 |
| `ko/egbim/img/pay_icon3.png` | 1,174 | 파일 크기/참조 검사 |
| `ko/egbim/img/pay_icon4.png` | 1,185 | 파일 크기/참조 검사 |
| `ko/egbim/img/payco.png` | 2,326 | 파일 크기/참조 검사 |
| `ko/egbim/img/payco_logo.png` | 711 | 파일 크기/참조 검사 |
| `ko/egbim/img/paynow.png` | 2,387 | 파일 크기/참조 검사 |
| `ko/egbim/img/paynow_logo.png` | 679 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_block_bg.png` | 906,391 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_intro_bg.png` | 475,109 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_menu_bg.png` | 298,380 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_print_bg.png` | 786,099 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_route_01.png` | 394,592 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_route_02.png` | 232,221 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_route_03.png` | 254,405 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_route_bg.png` | 980,927 | 파일 크기/참조 검사 |
| `ko/egbim/img/primary_style_bg.png` | 1,043,595 | 파일 크기/참조 검사 |
| `ko/egbim/img/print_img_01.png` | 307,911 | 파일 크기/참조 검사 |
| `ko/egbim/img/print_img_02.png` | 1,340,845 | 파일 크기/참조 검사 |
| `ko/egbim/img/printarea_img_01.png` | 1,019,373 | 파일 크기/참조 검사 |
| `ko/egbim/img/printarea_img_02.png` | 661,226 | 파일 크기/참조 검사 |
| `ko/egbim/img/require.png` | 2,922 | 파일 크기/참조 검사 |
| `ko/egbim/img/road_proportionality_bg.jpg` | 374,805 | 파일 크기/참조 검사 |
| `ko/egbim/img/samsungpay.png` | 2,071 | 파일 크기/참조 검사 |
| `ko/egbim/img/sch_btn.png` | 1,234 | 파일 크기/참조 검사 |
| `ko/egbim/img/sitemap_menu01.png` | 1,768,415 | 파일 크기/참조 검사 |
| `ko/egbim/img/sitemap_menu02.png` | 1,000,846 | 파일 크기/참조 검사 |
| `ko/egbim/img/sitemap_menu03.png` | 1,659,994 | 파일 크기/참조 검사 |
| `ko/egbim/img/sitemap_menu04.png` | 1,568,391 | 파일 크기/참조 검사 |
| `ko/egbim/img/sitemap_menu05.png` | 2,119,415 | 파일 크기/참조 검사 |
| `ko/egbim/img/skpay11_icon.png` | 7,920 | 파일 크기/참조 검사 |
| `ko/egbim/img/ssgpay_icon.png` | 1,887 | 파일 크기/참조 검사 |
| `ko/egbim/img/style_img_01.png` | 269,512 | 파일 크기/참조 검사 |
| `ko/egbim/img/style_img_02.png` | 272,754 | 파일 크기/참조 검사 |
| `ko/egbim/img/style_img_03.png` | 340,582 | 파일 크기/참조 검사 |
| `ko/egbim/img/tnb_shop.jpg` | 881 | 파일 크기/참조 검사 |
| `ko/egbim/img/tri_img.svg` | 888 | 파일 크기/참조 검사 |
| `ko/egbim/img/ts01.gif` | 138 | 파일 크기/참조 검사 |
| `ko/egbim/img/ts01.png` | 1,219 | 파일 크기/참조 검사 |
| `ko/egbim/img/ts02.gif` | 148 | 파일 크기/참조 검사 |
| `ko/egbim/img/ts02.png` | 1,252 | 파일 크기/참조 검사 |
| `ko/egbim/img/ts03.gif` | 154 | 파일 크기/참조 검사 |
| `ko/egbim/img/ts03.png` | 1,319 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_arc.svg` | 925 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_arc_r.svg` | 924 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_feature_bg.png` | 815,763 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_feature_bim_bg.png` | 842,050 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_feature_floorplan_bg.png` | 730,776 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_feature_interface_bg.png` | 2,549,341 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_feature_tool_bg.png` | 271,209 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_introbg.png` | 4,678,800 | 파일 크기/참조 검사 |
| `ko/egbim/img/value_system_bg.png` | 555,451 | 파일 크기/참조 검사 |
| `ko/egbim/img/wrest.gif` | 51 | 파일 크기/참조 검사 |
| `ko/egbim/interface.html` | 10,415 | HTML: 동기 외부 스크립트 13, 이미지 5 (lazy 0), video 0, iframe 0; 외부 URL 11, 로컬 참조 확인 필요 0 |
| `ko/egbim/js/StickyOnTable.js` | 5,296 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/autosave.js` | 5,067 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/certify.js` | 4,875 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/ckeditor/adapters/jquery.js` | 3,189 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/build-config.js` | 2,909 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/ckeditor.js` | 760,672 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 7; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/config.js` | 346 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/contents.css` | 3,092 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/lang/en.js` | 18,232 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/lang/ko.js` | 19,743 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/a11yhelp.js` | 2,978 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/af.js` | 4,182 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ar.js` | 4,378 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/az.js` | 4,358 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/bg.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ca.js` | 4,816 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/cs.js` | 4,965 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/cy.js` | 4,415 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/da.js` | 4,273 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/de-ch.js` | 4,740 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/de.js` | 4,684 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/el.js` | 7,659 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/en-au.js` | 4,230 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/en-gb.js` | 4,230 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/en.js` | 4,227 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/eo.js` | 4,825 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/es-mx.js` | 4,921 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/es.js` | 4,827 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/et.js` | 4,444 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/eu.js` | 4,532 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fa.js` | 6,178 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fi.js` | 4,787 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fo.js` | 4,229 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fr-ca.js` | 4,949 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/fr.js` | 5,337 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/gl.js` | 4,841 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/gu.js` | 4,437 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/he.js` | 4,981 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/hi.js` | 4,241 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/hr.js` | 4,307 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/hu.js` | 4,793 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/id.js` | 4,065 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/it.js` | 5,265 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ja.js` | 5,224 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/km.js` | 5,245 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ko.js` | 5,624 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ku.js` | 6,059 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/lt.js` | 4,236 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/lv.js` | 4,860 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/mk.js` | 4,618 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/mn.js` | 4,234 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/nb.js` | 4,484 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/nl.js` | 4,559 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/no.js` | 4,470 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/oc.js` | 5,125 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/pl.js` | 5,188 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/pt-br.js` | 4,955 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/pt.js` | 4,595 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ro.js` | 4,586 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ru.js` | 6,672 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/si.js` | 6,170 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sk.js` | 4,795 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sl.js` | 4,575 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sq.js` | 4,960 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sr-latn.js` | 4,924 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sr.js` | 7,542 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/sv.js` | 4,395 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/th.js` | 4,605 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/tr.js` | 4,606 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/tt.js` | 4,545 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/ug.js` | 6,963 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/uk.js` | 6,953 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/vi.js` | 5,426 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/zh-cn.js` | 4,172 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/a11yhelp/dialogs/lang/zh.js` | 4,381 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/about/dialogs/about.js` | 1,957 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/clipboard/dialogs/paste.js` | 3,835 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/colordialog/dialogs/colordialog.css` | 806 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/colordialog/dialogs/colordialog.js` | 5,356 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/copyformatting/styles/copyformatting.css` | 1,527 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/dialog/dialogDefinition.js` | 186 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/dialog/styles/dialog.css` | 249 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/div/dialogs/div.js` | 4,685 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/plugindefinition.js` | 3 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/_helpers/tools.js` | 677 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/authentication.js` | 3,038 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/exportpdf.js` | 4,835 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/configfilename.html` | 694 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/emptyeditor.html` | 432 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integration.html` | 5,396 | HTML: 동기 외부 스크립트 0, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/integrations/easyimage.html` | 814 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/notifications.html` | 396 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/notificationsasync.html` | 1,047 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/paperformat.html` | 1,273 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/readonly.html` | 411 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/stylesheets.html` | 1,200 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokenfetching.html` | 568 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokentwoeditorscorrect.html` | 1,064 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokentwoeditorswrong.html` | 1,088 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/tokenwithouturl.html` | 475 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/manual/wrongendpoint.html` | 488 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/notification.js` | 1,977 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/resourcespaths.js` | 4,757 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/statistics.js` | 1,098 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/exportpdf/tests/stylesheets.js` | 9,899 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/find/dialogs/find.js` | 11,465 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/button.js` | 1,886 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/checkbox.js` | 2,601 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/form.js` | 2,150 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/hiddenfield.js` | 1,728 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/radio.js` | 2,411 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/select.js` | 8,562 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/textarea.js` | 2,358 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/forms/dialogs/textfield.js` | 3,463 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/iframe/dialogs/iframe.js` | 3,505 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/image/dialogs/image.js` | 21,588 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/link/dialogs/anchor.js` | 2,231 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/link/dialogs/link.js` | 13,279 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/liststyle/dialogs/liststyle.js` | 2,908 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/pastefromgdocs/filter/default.js` | 2,232 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/pastefromlibreoffice/filter/default.js` | 3,536 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/pastefromword/filter/default.js` | 19,960 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/pastetools/filter/common.js` | 10,419 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/pastetools/filter/image.js` | 3,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/preview/preview.html` | 259 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/preview/styles/screen.css` | 242 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/scayt/dialogs/dialog.css` | 419 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/scayt/dialogs/options.js` | 16,167 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/scayt/dialogs/toolbar.css` | 1,302 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/scayt/skins/moono-lisa/scayt.css` | 381 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/smiley/dialogs/smiley.js` | 3,487 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/af.js` | 4,575 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ar.js` | 4,824 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/az.js` | 3,432 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/bg.js` | 4,848 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ca.js` | 5,057 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/cs.js` | 5,013 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/cy.js` | 4,938 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/da.js` | 3,406 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/de-ch.js` | 4,835 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/de.js` | 4,826 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/el.js` | 7,774 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en-au.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en-ca.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en-gb.js` | 4,592 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/en.js` | 4,589 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/eo.js` | 4,109 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/es-mx.js` | 4,818 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/es.js` | 4,989 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/et.js` | 3,857 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/eu.js` | 4,591 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fa.js` | 5,813 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fi.js` | 4,627 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fr-ca.js` | 3,259 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/fr.js` | 3,897 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/gl.js` | 5,046 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/he.js` | 5,027 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/hr.js` | 4,433 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/hu.js` | 4,176 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/id.js` | 4,596 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/it.js` | 5,063 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ja.js` | 4,022 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/km.js` | 4,793 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ko.js` | 4,959 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ku.js` | 7,606 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/lt.js` | 4,634 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/lv.js` | 5,064 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/nb.js` | 3,472 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/nl.js` | 4,768 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/no.js` | 3,472 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/oc.js` | 3,871 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/pl.js` | 4,370 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/pt-br.js` | 3,870 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/pt.js` | 4,837 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ro.js` | 4,720 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ru.js` | 7,589 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/si.js` | 4,930 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sk.js` | 4,806 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sl.js` | 4,390 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sq.js` | 5,033 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sr-latn.js` | 4,756 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sr.js` | 7,558 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/sv.js` | 3,524 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/th.js` | 4,718 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/tr.js` | 4,520 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/tt.js` | 6,771 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/ug.js` | 5,045 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/uk.js` | 6,411 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/vi.js` | 6,128 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/zh-cn.js` | 4,419 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/lang/zh.js` | 4,199 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/specialchar/dialogs/specialchar.js` | 5,034 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/table/dialogs/table.js` | 9,080 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/tableselection/styles/tableselection.css` | 1,145 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/tabletools/dialogs/tableCell.js` | 7,387 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/templates/dialogs/templates.css` | 1,604 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/templates/dialogs/templates.js` | 3,429 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/templates/templatedefinition.js` | 186 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/plugins/templates/templates/default.js` | 1,983 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/css/samples.css` | 67,340 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/img/github-top.png` | 383 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/img/header-bg.png` | 13,086 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/img/header-separator.png` | 123 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/img/logo.png` | 5,634 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/img/logo.svg` | 10,900 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/img/navigation-tip.png` | 12,029 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/index.html` | 7,234 | HTML: 동기 외부 스크립트 2, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 16, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/js/sample.js` | 1,594 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/js/sf.js` | 6,442 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/ajax.html` | 2,911 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/api.html` | 7,545 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/appendto.html` | 2,523 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/assets/outputxhtml/outputxhtml.css` | 2,161 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/assets/uilanguages/languages.js` | 1,467 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/datafiltering.html` | 47,840 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 15, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/dialog/assets/my_dialog.js` | 911 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/dialog/dialog.html` | 7,606 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/divreplace.html` | 4,893 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/enterkey/enterkey.html` | 5,018 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/htmlwriter/outputhtml.html` | 7,622 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/index.html` | 6,073 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/inlineall.html` | 10,399 | HTML: 동기 외부 스크립트 1, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 7, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/inlinebycode.html` | 6,395 | HTML: 동기 외부 스크립트 1, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 14, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/inlinetextarea.html` | 5,125 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/jquery.html` | 7,754 | HTML: 동기 외부 스크립트 3, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 12, 로컬 참조 확인 필요 3; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/magicline/magicline.html` | 9,249 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/readonly.html` | 3,132 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/replacebyclass.html` | 7,234 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/replacebycode.html` | 7,119 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/sample.css` | 5,112 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/sample.js` | 1,693 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/tabindex.html` | 2,609 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/toolbar/toolbar.html` | 10,291 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/uicolor.html` | 2,810 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/uilanguages.html` | 4,741 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 6, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/wysiwygarea/fullpage.html` | 8,531 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 4, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/old/xhtmlstyle.html` | 7,233 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 5, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/css/fontello.css` | 1,758 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/font/LICENSE.txt` | 188 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/font/config.json` | 584 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.eot` | 4,988 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.svg` | 1,714 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.ttf` | 4,820 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/font/fontello.woff` | 2,904 | 파일 크기/참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/index.html` | 15,808 | HTML: 동기 외부 스크립트 9, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 11, 로컬 참조 확인 필요 6; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/js/abstracttoolbarmodifier.js` | 6,535 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/js/fulltoolbareditor.js` | 3,846 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/js/toolbarmodifier.js` | 16,683 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/samples/toolbarconfigurator/js/toolbartextmodifier.js` | 6,863 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/dialog.css` | 13,650 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/dialog_ie.css` | 14,673 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/dialog_ie8.css` | 15,222 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/dialog_iequirks.css` | 14,702 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 9; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/editor.css` | 48,325 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/editor_gecko.css` | 48,406 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/editor_ie.css` | 49,324 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/editor_ie8.css` | 50,130 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/skins/moono-lisa/editor_iequirks.css` | 49,973 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 172; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/styles.js` | 5,577 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/ckeditor/vendor/promise.js` | 6,309 | 텍스트 리소스 참조 검사; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/common.js` | 39,011 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 4 |
| `ko/egbim/js/common_240813.js` | 27,419 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/common_250204.js` | 30,806 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/common_250307.js` | 31,539 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/common_OR.js` | 32,362 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/common_bak.js` | 27,658 | 텍스트 리소스 참조 검사; 외부 URL 2, 로컬 참조 확인 필요 1; 샘플/백업 포함, 초기 로드 여부 별도 확인 |
| `ko/egbim/js/floorplan.js` | 5,586 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/floorplan_253010.js` | 4,375 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/font-awesome/css/font-awesome.css` | 39,751 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `ko/egbim/js/font-awesome/css/font-awesome.min.css` | 31,004 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `ko/egbim/js/forbim.js` | 4,613 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/forbim_250204.js` | 2,304 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/forbim_250310.js` | 3,755 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/html5.js` | 2,396 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/include.js` | 620 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/index.js` | 5,748 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/index_240813.js` | 4,036 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/index_250204.js` | 4,513 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/index_250310.js` | 4,593 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/interface.js` | 4,687 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery-1.12.4.min.js` | 97,168 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `ko/egbim/js/jquery-1.8.3.min.js` | 93,637 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/jquery-3.6.1.min.js` | 89,664 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery-migrate-1.4.1.min.js` | 10,057 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.anchorScroll.js` | 2,234 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.bxslider.js` | 53,133 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.fancyalert.js` | 988 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.fancylist.js` | 2,105 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.menu.js` | 2,930 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.mousewheel.min.js` | 2,680 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.nicescroll.min.js` | 57,783 | 텍스트 리소스 참조 검사; 외부 URL 1, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/jquery.register_form.js` | 2,172 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.shop.menu.js` | 1,838 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/jquery.sms_paging.js` | 3,309 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/kakaolink.js` | 759 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/md5.js` | 8,084 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/modernizr.custom.70111.js` | 2,127 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/owlcarousel/owl.carousel.css` | 4,930 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/owlcarousel/owl.carousel.js` | 93,440 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/owlcarousel/owl.carousel.min.css` | 3,356 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/owlcarousel/owl.carousel.min.js` | 44,348 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `ko/egbim/js/placeholders.min.js` | 5,103 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/popup.js` | 11,039 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/popup_240813.js` | 8,834 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/popup_250204.js` | 11,966 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/primary.js` | 4,150 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/primary_240927.js` | 4,251 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/primary_250307.js` | 3,538 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/public.js` | 3,544 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/public_240813.js` | 6,135 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/remodal/remodal-default-theme.css` | 4,181 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/remodal/remodal.css` | 1,275 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/remodal/remodal.js` | 19,911 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/road.js` | 3,906 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/road_240813.js` | 4,450 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/scroll_oldie.js` | 1,239 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.category.navigation.js` | 2,156 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.couponzone.js` | 1,118 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.js` | 16,514 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.list.action.js` | 10,215 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.list.js` | 3,078 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.mobile.list.js` | 1,385 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.mobile.main.js` | 4,480 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.order.js` | 297 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/shop.override.js` | 7,342 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/sns.js` | 385 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/style.css` | 109,081 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/egbim/js/swipe.js` | 14,924 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/swiper/swiper.min.css` | 19,345 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/swiper/swiper.min.js` | 111,727 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/tooltipster/tooltipster.bundle.css` | 9,909 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/tooltipster/tooltipster.bundle.js` | 124,074 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/tooltipster/tooltipster.bundle.min.css` | 6,495 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/tooltipster/tooltipster.bundle.min.js` | 39,901 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/value.js` | 1,189 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/value_240813.js` | 7,022 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 4 |
| `ko/egbim/js/viewimageresize.js` | 2,575 | 텍스트 리소스 참조 검사 |
| `ko/egbim/js/wrest.js` | 11,466 | 텍스트 리소스 참조 검사 |
| `ko/egbim/primary.html` | 12,678 | HTML: 동기 외부 스크립트 9, 이미지 6 (lazy 0), video 0, iframe 0; 외부 URL 7, 로컬 참조 확인 필요 0 |
| `ko/egbim/value.html` | 12,972 | HTML: 동기 외부 스크립트 9, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 7, 로컬 참조 확인 필요 0 |
| `ko/faq.html` | 2,754 | HTML: 동기 외부 스크립트 6, 이미지 1 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/buy.html` | 3,558 | HTML: 동기 외부 스크립트 8, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 9, 로컬 참조 확인 필요 0 |
| `ko/gaia/css/font.css` | 1,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `ko/gaia/css/reset.css` | 2,193 | 텍스트 리소스 참조 검사 |
| `ko/gaia/css/style.css` | 257,549 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 2 |
| `ko/gaia/download/GAIA_leaflet.pdf` | 7,402,090 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Black/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Black/notokr-black-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/gaia/font/NotoKR-Black/notokr-black.eot` | 149,951 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Black/notokr-black.svg` | 703,668 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Black/notokr-black.ttf` | 358,600 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Black/notokr-black.woff` | 180,348 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Black/notokr-black.woff2` | 128,720 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Black/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Black/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Black/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Black/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Bold/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Bold/notokr-bold-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/gaia/font/NotoKR-Bold/notokr-bold.eot` | 156,008 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Bold/notokr-bold.svg` | 705,999 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Bold/notokr-bold.ttf` | 359,412 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Bold/notokr-bold.woff` | 185,412 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Bold/notokr-bold.woff2` | 134,968 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Bold/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Bold/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Bold/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Bold/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-DemiLight/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/notokr-demilight-demo.html` | 173,863 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/gaia/font/NotoKR-DemiLight/notokr-demilight.eot` | 155,464 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/notokr-demilight.svg` | 733,933 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/notokr-demilight.ttf` | 369,728 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/notokr-demilight.woff` | 187,464 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/notokr-demilight.woff2` | 133,772 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-DemiLight/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-DemiLight/stylesheet.css` | 547 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Light/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Light/notokr-light-demo.html` | 173,835 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/gaia/font/NotoKR-Light/notokr-light.eot` | 153,179 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Light/notokr-light.svg` | 748,368 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Light/notokr-light.ttf` | 373,820 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Light/notokr-light.woff` | 185,532 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Light/notokr-light.woff2` | 131,096 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Light/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Light/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Light/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Light/stylesheet.css` | 515 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Medium/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Medium/notokr-medium-demo.html` | 173,842 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/gaia/font/NotoKR-Medium/notokr-medium.eot` | 155,800 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Medium/notokr-medium.svg` | 717,209 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Medium/notokr-medium.ttf` | 364,276 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Medium/notokr-medium.woff` | 185,440 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Medium/notokr-medium.woff2` | 133,836 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Medium/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Medium/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Medium/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Medium/stylesheet.css` | 523 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Regular/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Regular/notokr-regular-demo.html` | 173,868 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/gaia/font/NotoKR-Regular/notokr-regular.eot` | 156,734 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Regular/notokr-regular.svg` | 727,332 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Regular/notokr-regular.ttf` | 367,940 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Regular/notokr-regular.woff` | 187,364 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Regular/notokr-regular.woff2` | 134,960 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Regular/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Regular/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Regular/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Regular/stylesheet.css` | 531 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Thin/generator_config.txt` | 561 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Thin/notokr-thin-demo.html` | 173,828 | HTML: 동기 외부 스크립트 2, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 2, 로컬 참조 확인 필요 5 |
| `ko/gaia/font/NotoKR-Thin/notokr-thin.eot` | 143,518 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Thin/notokr-thin.svg` | 761,397 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Thin/notokr-thin.ttf` | 377,440 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Thin/notokr-thin.woff` | 175,184 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Thin/notokr-thin.woff2` | 120,720 | 파일 크기/참조 검사 |
| `ko/gaia/font/NotoKR-Thin/specimen_files/easytabs.js` | 1,088 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Thin/specimen_files/grid_12-825-55-15.css` | 4,725 | 텍스트 리소스 참조 검사 |
| `ko/gaia/font/NotoKR-Thin/specimen_files/specimen_stylesheet.css` | 7,706 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/font/NotoKR-Thin/stylesheet.css` | 507 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/further.html` | 13,558 | HTML: 동기 외부 스크립트 9, 이미지 20 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/gaia/img/Thumbs.db` | 1,845,248 | 파일 크기/참조 검사 |
| `ko/gaia/img/arrow_r.svg` | 167 | 파일 크기/참조 검사 |
| `ko/gaia/img/atom_line.svg` | 1,633 | 파일 크기/참조 검사 |
| `ko/gaia/img/atom_obj.svg` | 1,936 | 파일 크기/참조 검사 |
| `ko/gaia/img/baron_logo.svg` | 6,233 | 파일 크기/참조 검사 |
| `ko/gaia/img/bg_close.png` | 906 | 파일 크기/참조 검사 |
| `ko/gaia/img/bg_pop.png` | 2,213,561 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_end.gif` | 1,176 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_first.gif` | 1,885 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_idx_left.png` | 3,141 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_idx_right.png` | 442 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_next.gif` | 1,169 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_prev.gif` | 1,873 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_search.jpg` | 782 | 파일 크기/참조 검사 |
| `ko/gaia/img/btn_top.gif` | 1,178 | 파일 크기/참조 검사 |
| `ko/gaia/img/bullet.gif` | 1,165 | 파일 크기/참조 검사 |
| `ko/gaia/img/buy_intro_bg.jpg` | 727,741 | 파일 크기/참조 검사 |
| `ko/gaia/img/buy_video.mp4` | 60,429,670 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/captcha.png` | 4,886 | 파일 크기/참조 검사 |
| `ko/gaia/img/captcha2.png` | 4,886 | 파일 크기/참조 검사 |
| `ko/gaia/img/chk.png` | 1,070 | 파일 크기/참조 검사 |
| `ko/gaia/img/close_btn.gif` | 1,209 | 파일 크기/참조 검사 |
| `ko/gaia/img/close_btn.png` | 1,147 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/Thumbs.db` | 522,752 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_1.png` | 729,470 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_10.png` | 361,340 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_11.png` | 145,644 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_12.png` | 14,091 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_13.png` | 17,110 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_14.png` | 92,527 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_15.png` | 144,244 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_16.png` | 188,767 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_17.png` | 221,944 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_18.png` | 254,233 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_19.png` | 317,194 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_2.png` | 727,547 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_20.png` | 397,369 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_21.png` | 468,221 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_22.png` | 502,992 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_23.png` | 503,362 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_24.png` | 500,551 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_25.png` | 500,422 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_26.png` | 503,390 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_27.png` | 502,812 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_28.png` | 503,077 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_29.png` | 541,028 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_3.png` | 729,358 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_30.png` | 549,525 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_31.png` | 549,041 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_32.png` | 550,112 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_33.png` | 554,641 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_34.png` | 559,102 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_35.png` | 558,365 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_36.png` | 559,487 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_37.png` | 560,431 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_38.png` | 558,668 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_39.png` | 558,298 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_4.png` | 728,233 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_40.png` | 559,030 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_41.png` | 607,476 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_42.png` | 662,486 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_43.png` | 720,297 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_44.png` | 780,145 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_45.png` | 851,441 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_46.png` | 914,471 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_47.png` | 953,623 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_48.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_49.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_5.png` | 705,944 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_50.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_51.png` | 962,638 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_52.png` | 1,049,340 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_53.png` | 1,138,471 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_54.png` | 1,197,889 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_55.png` | 1,233,019 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_56.png` | 1,259,825 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_57.png` | 1,311,789 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_58.png` | 1,357,885 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_59.png` | 1,366,900 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_6.png` | 662,210 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_60.png` | 1,350,101 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_61.png` | 1,288,616 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_62.png` | 1,223,769 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_63.png` | 1,232,384 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_64.png` | 1,240,668 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_65.png` | 1,241,184 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_66.png` | 1,240,533 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_67.png` | 1,239,298 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_68.png` | 1,240,688 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_69.png` | 1,241,242 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_7.png` | 607,289 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_70.png` | 1,243,732 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_71.png` | 1,252,218 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_72.png` | 1,252,668 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_73.png` | 1,251,460 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_74.png` | 1,248,539 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_75.png` | 1,243,890 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_76.png` | 1,239,844 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_77.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_78.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_79.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_8.png` | 543,705 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_80.png` | 1,238,030 | 파일 크기/참조 검사 |
| `ko/gaia/img/com_img/comp_9.png` | 451,356 | 파일 크기/참조 검사 |
| `ko/gaia/img/faq_intro_bg.png` | 933,519 | 파일 크기/참조 검사 |
| `ko/gaia/img/floating_buy_bg.svg` | 1,318 | 파일 크기/참조 검사 |
| `ko/gaia/img/floating_buy_bg_m.svg` | 1,907 | 파일 크기/참조 검사 |
| `ko/gaia/img/floating_faq_bg.svg` | 1,352 | 파일 크기/참조 검사 |
| `ko/gaia/img/floating_faq_bg_m.svg` | 3,299 | 파일 크기/참조 검사 |
| `ko/gaia/img/ft.png` | 3,204 | 파일 크기/참조 검사 |
| `ko/gaia/img/ft_logo.png` | 3,737 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_app_fig1.jpg` | 352,068 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_app_fig2.jpg` | 439,908 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_app_fig3.jpg` | 781,742 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_app_fig4.jpg` | 898,768 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_gather_arrow_l.svg` | 546 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_gather_step1_line.svg` | 1,258 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_gather_step2_line1.svg` | 10,139 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_gather_step2_line2.svg` | 1,398 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_intro_bg.jpg` | 583,279 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_link_fig1.jpg` | 243,891 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_link_fig2.jpg` | 389,080 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_link_fig3.jpg` | 338,322 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_link_fig4.jpg` | 393,229 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_bg1.jpg` | 381,978 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_bg2.jpg` | 366,130 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_bg3.jpg` | 318,558 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_gather01.jpg` | 217,150 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_gather02-1.jpg` | 11,898 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_gather02-2.jpg` | 24,152 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_gather02-3.jpg` | 37,404 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_gather02.jpg` | 186,226 | 파일 크기/참조 검사 |
| `ko/gaia/img/further_process_gather03.jpg` | 310,012 | 파일 크기/참조 검사 |
| `ko/gaia/img/gaia_k.svg` | 870 | 파일 크기/참조 검사 |
| `ko/gaia/img/gaia_obj_k.svg` | 343 | 파일 크기/참조 검사 |
| `ko/gaia/img/gaia_obj_w.svg` | 341 | 파일 크기/참조 검사 |
| `ko/gaia/img/gaia_w.svg` | 888 | 파일 크기/참조 검사 |
| `ko/gaia/img/gnb_bg.gif` | 1,169 | 파일 크기/참조 검사 |
| `ko/gaia/img/gnb_bg00.gif` | 54 | 파일 크기/참조 검사 |
| `ko/gaia/img/gnb_bg01.gif` | 54 | 파일 크기/참조 검사 |
| `ko/gaia/img/gnb_bg2.gif` | 49 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico-default-naverpay.png` | 2,689 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico-mobile-applepay.png` | 2,063 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico-mobile-kakaopay.png` | 3,251 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico-mobile-naverpay.png` | 3,261 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_admin.svg` | 5,691 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_angle.svg` | 243 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_answer.svg` | 294 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_arrow.svg` | 488 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_arrow_s.svg` | 490 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_bulit_check.svg` | 247 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_buy_alarm.svg` | 929 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_buy_ask.svg` | 2,054 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_buy_brochure.svg` | 2,196 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_buy_mail.svg` | 585 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_buy_manual.svg` | 1,638 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_buy_tel.svg` | 1,093 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_cafe.svg` | 1,171 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_close.svg` | 201 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_company.svg` | 887 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_complete.svg` | 1,088 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_countdown.svg` | 4,119 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_infomodel.svg` | 1,985 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_modify.svg` | 3,495 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_network.svg` | 3,849 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_results_01.svg` | 2,409 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_results_02.svg` | 2,480 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_results_03.svg` | 2,086 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_results_04.svg` | 2,024 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_results_05.svg` | 858 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dia_site.svg` | 983 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_dublecheck.svg` | 1,680 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_email.svg` | 1,146 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_facebook.svg` | 952 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_floating_buy.svg` | 651 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_floating_buy_on.svg` | 651 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_floating_faq.svg` | 1,173 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_floating_faq_on.svg` | 1,174 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_footer_close.svg` | 333 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_further_dia1.svg` | 6,202 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_further_dia1_w.svg` | 6,194 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_further_dia2.svg` | 1,008 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_further_dia2_w.svg` | 1,000 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_further_dia3.svg` | 994 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_further_dia3_w.svg` | 990 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_further_send.svg` | 1,486 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_ham.svg` | 309 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_id.svg` | 1,018 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_language.svg` | 1,324 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_location_01.svg` | 1,732 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_location_02.svg` | 1,432 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_location_03.svg` | 898 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_location_04.svg` | 4,247 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_lock.svg` | 1,607 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_model_01.svg` | 622 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_model_02.svg` | 734 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_model_03.svg` | 664 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_model_04.svg` | 1,427 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_model_05.svg` | 1,045 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_model_06.svg` | 3,675 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_modify_01.svg` | 711 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_modify_02.svg` | 13,436 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_modify_03.svg` | 589 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_modify_04.svg` | 988 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_modify_05.svg` | 555 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_modify_06.svg` | 839 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_my.svg` | 888 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_network.svg` | 1,574 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_pg_left.svg` | 1,056 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_pg_right.svg` | 1,046 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_phone.svg` | 727 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_primary_pub04.svg` | 359 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_pw.svg` | 1,185 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_send_email.svg` | 634 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_signout.svg` | 933 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs01.svg` | 2,420 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs01_mo.svg` | 2,465 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs01_mo_w.svg` | 2,458 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs01_w.svg` | 2,383 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs02.svg` | 739 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs02_mo.svg` | 889 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs02_mo_w.svg` | 885 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs02_w.svg` | 710 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs03.svg` | 2,030 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs03_mo.svg` | 2,067 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs03_mo_w.svg` | 2,072 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs03_w.svg` | 1,999 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs04.svg` | 2,074 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs04_mo.svg` | 2,078 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs04_mo_w.svg` | 2,066 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs04_w.svg` | 2,043 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs05.svg` | 2,401 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs05_mo.svg` | 2,390 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs05_mo_w.svg` | 2,382 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_slide_tabs05_w.svg` | 2,374 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_cursor.svg` | 1,810 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_data_k.svg` | 1,774 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_data_w.svg` | 1,774 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_design_k.svg` | 1,415 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_design_w.svg` | 1,415 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_devices_k.svg` | 988 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_devices_w.svg` | 988 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_interface_k.svg` | 800 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_interface_w.svg` | 800 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_screen.svg` | 1,742 | 파일 크기/참조 검사 |
| `ko/gaia/img/ico_value_scroll.svg` | 996 | 파일 크기/참조 검사 |
| `ko/gaia/img/info_img_01_01.svg` | 5,631 | 파일 크기/참조 검사 |
| `ko/gaia/img/interface_img_01.svg` | 92,104 | 파일 크기/참조 검사 |
| `ko/gaia/img/interface_img_03.svg` | 709,308 | 파일 크기/참조 검사 |
| `ko/gaia/img/interface_route_screen.png` | 301,366 | 파일 크기/참조 검사 |
| `ko/gaia/img/kakao.png` | 804 | 파일 크기/참조 검사 |
| `ko/gaia/img/kpay.png` | 2,697 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_01.png` | 562,212 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_01.svg` | 1,224,284 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_01_01.png` | 1,343,215 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_01_02.png` | 2,187,993 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_01_03.png` | 2,092,764 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_01_04.png` | 2,087,985 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_01.png` | 1,456,305 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_01_click_off.png` | 1,537,297 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_01_click_on.png` | 1,538,120 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_02.png` | 1,405,222 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_02_click_off.png` | 1,249,678 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_02_click_on.png` | 1,249,941 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_03.png` | 227,925 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_02_04.png` | 1,459,148 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_01.png` | 1,704,772 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_02.png` | 948,803 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_03.png` | 115,766 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_03_01.png` | 798,498 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_03_02.png` | 806,540 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_03_03.png` | 806,957 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_03_04.png` | 806,003 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_04.png` | 114,308 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_05.png` | 114,833 | 파일 크기/참조 검사 |
| `ko/gaia/img/location_img_03_06.png` | 113,024 | 파일 크기/참조 검사 |
| `ko/gaia/img/logo.png` | 3,797 | 파일 크기/참조 검사 |
| `ko/gaia/img/logo_gaia.jpg` | 18,188 | 파일 크기/참조 검사 |
| `ko/gaia/img/lpay_logo.png` | 1,393 | 파일 크기/참조 검사 |
| `ko/gaia/img/m_logo.png` | 3,100 | 파일 크기/참조 검사 |
| `ko/gaia/img/main_1.mp4` | 20,469,695 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/main_1_v.mp4` | 11,291,274 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/main_2.mp4` | 58,516,537 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/main_2_v.mp4` | 14,360,051 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/main_3.mp4` | 30,498,805 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/main_3_v.mp4` | 13,165,355 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/main_4.mp4` | 68,228,680 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/main_4_v.mp4` | 10,319,879 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/gaia/img/mobile/btn_close.png` | 3,265 | 파일 크기/참조 검사 |
| `ko/gaia/img/mobile/gnb_bg.png` | 1,012 | 파일 크기/참조 검사 |
| `ko/gaia/img/mobile/gnb_bg2.png` | 976 | 파일 크기/참조 검사 |
| `ko/gaia/img/mobile/gnb_sch.png` | 1,795 | 파일 크기/참조 검사 |
| `ko/gaia/img/mobile/icon_menu.png` | 1,090 | 파일 크기/참조 검사 |
| `ko/gaia/img/mobile/icon_my.png` | 1,634 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_01_01.png` | 548,555 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_01_02.png` | 810,507 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_01_02_01.png` | 483,292 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_01_02_02.png` | 464,687 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_01_03.png` | 666,967 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_02.png` | 1,361,676 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_02_01.png` | 1,319,846 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_02_02.png` | 54,650 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_02_03.png` | 56,953 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_02_04.png` | 60,257 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_03_01.png` | 1,490,067 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_03_02.png` | 287,111 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_03_03.png` | 230,267 | 파일 크기/참조 검사 |
| `ko/gaia/img/model_img_03_04.png` | 812,589 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_01_01.png` | 376,953 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_01_02.png` | 326,247 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_01_03.png` | 56,866 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_01_04.png` | 459,715 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_02_01.png` | 777,808 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_02_02.png` | 913,580 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_02_03.png` | 794,299 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_02_04.png` | 668,213 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_01.png` | 1,281,753 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_02.png` | 1,021,853 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_03.png` | 950,246 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_04.png` | 253,390 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_05.png` | 179,530 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_06.png` | 776,210 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_07.png` | 802,556 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_08.png` | 1,011,609 | 파일 크기/참조 검사 |
| `ko/gaia/img/modify_img_03_09.png` | 1,014,051 | 파일 크기/참조 검사 |
| `ko/gaia/img/more-btn.gif` | 1,204 | 파일 크기/참조 검사 |
| `ko/gaia/img/no_img.png` | 991 | 파일 크기/참조 검사 |
| `ko/gaia/img/no_profile.gif` | 1,953 | 파일 크기/참조 검사 |
| `ko/gaia/img/og-main-thumb.JPG` | 182,485 | 파일 크기/참조 검사 |
| `ko/gaia/img/pay_icon1.png` | 1,676 | 파일 크기/참조 검사 |
| `ko/gaia/img/pay_icon2.png` | 1,703 | 파일 크기/참조 검사 |
| `ko/gaia/img/pay_icon3.png` | 1,174 | 파일 크기/참조 검사 |
| `ko/gaia/img/pay_icon4.png` | 1,185 | 파일 크기/참조 검사 |
| `ko/gaia/img/payco.png` | 2,326 | 파일 크기/참조 검사 |
| `ko/gaia/img/payco_logo.png` | 711 | 파일 크기/참조 검사 |
| `ko/gaia/img/paynow.png` | 2,387 | 파일 크기/참조 검사 |
| `ko/gaia/img/paynow_logo.png` | 679 | 파일 크기/참조 검사 |
| `ko/gaia/img/primary_01.png` | 959,337 | 파일 크기/참조 검사 |
| `ko/gaia/img/primary_02.png` | 1,347,298 | 파일 크기/참조 검사 |
| `ko/gaia/img/primary_03.png` | 1,333,641 | 파일 크기/참조 검사 |
| `ko/gaia/img/primary_block_bg.png` | 906,391 | 파일 크기/참조 검사 |
| `ko/gaia/img/primary_intro_bg.jpg` | 1,012,187 | 파일 크기/참조 검사 |
| `ko/gaia/img/require.png` | 2,922 | 파일 크기/참조 검사 |
| `ko/gaia/img/results_intro_bg.png` | 1,067,582 | 파일 크기/참조 검사 |
| `ko/gaia/img/road_conclusion_bg.jpg` | 8,826,947 | 파일 크기/참조 검사 |
| `ko/gaia/img/sample_video.jpg` | 255,486 | 파일 크기/참조 검사 |
| `ko/gaia/img/samsungpay.png` | 2,071 | 파일 크기/참조 검사 |
| `ko/gaia/img/sch_btn.png` | 1,234 | 파일 크기/참조 검사 |
| `ko/gaia/img/sitemap_menu01.jpg` | 1,002,893 | 파일 크기/참조 검사 |
| `ko/gaia/img/sitemap_menu02.jpg` | 618,118 | 파일 크기/참조 검사 |
| `ko/gaia/img/sitemap_menu03.jpg` | 335,497 | 파일 크기/참조 검사 |
| `ko/gaia/img/sitemap_menu04.jpg` | 315,822 | 파일 크기/참조 검사 |
| `ko/gaia/img/skpay11_icon.png` | 7,920 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_04_02.png` | 629,139 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_04_03.png` | 819,680 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_fix_bg.png` | 317,387 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_01.png` | 4,235,308 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_01_01.png` | 12,263 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_01_01_m.png` | 6,051 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_01_03.png` | 314,848 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_01_03_m.png` | 136,473 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_01_03_m_.png` | 128,357 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_01_m.png` | 1,940,084 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_02.png` | 668,937 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_02_01.png` | 9,730 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_02_01_m.png` | 4,591 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_02_02.png` | 11,180 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_02_03.png` | 418,812 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_02_03_m.png` | 176,383 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_02_m.png` | 368,083 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03.png` | 849,446 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_01.png` | 12,025 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_01_m.png` | 5,871 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_02.png` | 11,192 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_03.png` | 425,914 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_03_m.png` | 289,819 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_04.png` | 489,456 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_04_m.png` | 265,226 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_03_m.png` | 444,778 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_04.png` | 632,083 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_04_01.png` | 10,619 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_04_01_m.png` | 4,961 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_04_02.png` | 11,192 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_04_03.png` | 674,263 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_04_03_m.png` | 355,018 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_04_m.png` | 370,907 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_05.png` | 432,448 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_05_01.png` | 10,333 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_05_01_m.png` | 5,464 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_05_02.png` | 11,202 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_05_03.png` | 683,588 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_05_03_m.png` | 368,861 | 파일 크기/참조 검사 |
| `ko/gaia/img/slide_img_05_m.png` | 268,701 | 파일 크기/참조 검사 |
| `ko/gaia/img/ssgpay_icon.png` | 1,887 | 파일 크기/참조 검사 |
| `ko/gaia/img/tnb_shop.jpg` | 881 | 파일 크기/참조 검사 |
| `ko/gaia/img/tri_img.svg` | 888 | 파일 크기/참조 검사 |
| `ko/gaia/img/ts01.gif` | 138 | 파일 크기/참조 검사 |
| `ko/gaia/img/ts01.png` | 1,219 | 파일 크기/참조 검사 |
| `ko/gaia/img/ts02.gif` | 148 | 파일 크기/참조 검사 |
| `ko/gaia/img/ts02.png` | 1,252 | 파일 크기/참조 검사 |
| `ko/gaia/img/ts03.gif` | 154 | 파일 크기/참조 검사 |
| `ko/gaia/img/ts03.png` | 1,319 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_arrow_down.svg` | 10,635 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_arrow_down_m.svg` | 3,338 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_arrow_left.svg` | 1,983 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_arrow_left_m.svg` | 927 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_feature_bg.jpg` | 415,702 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_feature_bg_m.jpg` | 207,352 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_feature_data_bg.jpg` | 748,770 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_feature_design_bg.jpg` | 349,982 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_feature_devices_bg.jpg` | 418,143 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_intro_bg_bottom.png` | 1,256,598 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_intro_bg_top.png` | 4,500,150 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen1.jpg` | 605,917 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen1.png` | 1,249,763 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen2.jpg` | 565,249 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen3.jpg` | 932,185 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen4.jpg` | 651,106 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screenM_01.png` | 95,326 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screenM_02.png` | 1,081,755 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screenM_03.png` | 309,369 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screenM_04.png` | 613,779 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screenM_05.png` | 125,698 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen_bg.png` | 1,713,477 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen_bg_m.png` | 1,744,016 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen_tab1.svg` | 744 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen_tab2.svg` | 802 | 파일 크기/참조 검사 |
| `ko/gaia/img/value_screen_tab3.svg` | 787 | 파일 크기/참조 검사 |
| `ko/gaia/img/wrest.gif` | 51 | 파일 크기/참조 검사 |
| `ko/gaia/index.html` | 4,737 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/gaia/js/further.js` | 5,222 | 텍스트 리소스 참조 검사 |
| `ko/gaia/js/index.js` | 5,725 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 1 |
| `ko/gaia/js/jquery-3.6.1.min.js` | 89,664 | 텍스트 리소스 참조 검사 |
| `ko/gaia/js/jquery.mousewheel.min.js` | 2,680 | 텍스트 리소스 참조 검사 |
| `ko/gaia/js/primary.js` | 6,137 | 텍스트 리소스 참조 검사 |
| `ko/gaia/js/results.js` | 5,333 | 텍스트 리소스 참조 검사 |
| `ko/gaia/js/value.js` | 6,068 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/gaia/primary.html` | 20,787 | HTML: 동기 외부 스크립트 9, 이미지 32 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/gaia/results.html` | 19,242 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/gaia/value.html` | 20,300 | HTML: 동기 외부 스크립트 9, 이미지 6 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/hosting_index1.html` | 2,143 | HTML: 동기 외부 스크립트 0, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 2 |
| `ko/index.html` | 2,967 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `ko/pr_brochure.html` | 5,887 | HTML: 동기 외부 스크립트 7, 이미지 11 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/pr_ci.html` | 7,001 | HTML: 동기 외부 스크립트 8, 이미지 5 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `ko/pr_news.html` | 9,849 | HTML: 동기 외부 스크립트 7, 이미지 4 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/pr_news_view_251127.html` | 6,333 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/pr_news_view_260121.html` | 5,915 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/pr_news_view_260519.html` | 4,995 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/pr_news_view_260527.html` | 6,182 | HTML: 동기 외부 스크립트 7, 이미지 3 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/sv_bigroom.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/sv_solution copy.html` | 4 | HTML: 동기 외부 스크립트 0, 이미지 0 (lazy 0), video 0, iframe 0 |
| `ko/sv_solution.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/sv_solution_construction.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/sv_solution_operation.html` | 1,208 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/sv_sw.html` | 5,389 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `ko/sv_sw_egbim.html` | 3,636 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `ko/sv_sw_gaia.html` | 3,680 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `ko/sv_sw_ipipes.html` | 3,417 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `ko/sv_sw_kngil.html` | 3,513 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `ko/sv_sw_pq_program.html` | 3,462 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 3, 로컬 참조 확인 필요 0 |
| `ko/tova/.htaccess` | 327 | 파일 크기/참조 검사 |
| `ko/tova/buy.html` | 4,281 | HTML: 동기 외부 스크립트 9, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/tova/css/font.css` | 1,959 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 6 |
| `ko/tova/css/reset.css` | 2,221 | 텍스트 리소스 참조 검사 |
| `ko/tova/css/style.css` | 196,542 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `ko/tova/download/TOVA_leaflet.pdf` | 1,996,565 | 파일 크기/참조 검사 |
| `ko/tova/download/TOVA_manual.pdf` | 12,226,439 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/tova/font/NotoKR-Black/notokr-black.woff` | 180,348 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Black/notokr-black.woff2` | 128,720 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Bold/notokr-bold.woff` | 185,412 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Bold/notokr-bold.woff2` | 134,968 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Light/notokr-light.woff` | 185,532 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Light/notokr-light.woff2` | 131,096 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Medium/notokr-medium.woff` | 185,440 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Medium/notokr-medium.woff2` | 133,836 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Regular/notokr-regular.woff` | 187,364 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Regular/notokr-regular.woff2` | 134,960 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Thin/notokr-thin.woff` | 175,184 | 파일 크기/참조 검사 |
| `ko/tova/font/NotoKR-Thin/notokr-thin.woff2` | 120,720 | 파일 크기/참조 검사 |
| `ko/tova/img/arrow_r.svg` | 167 | 파일 크기/참조 검사 |
| `ko/tova/img/asset_search.svg` | 1,721 | 파일 크기/참조 검사 |
| `ko/tova/img/atom_line.svg` | 1,633 | 파일 크기/참조 검사 |
| `ko/tova/img/atom_obj.svg` | 1,939 | 파일 크기/참조 검사 |
| `ko/tova/img/baron_logo.svg` | 6,233 | 파일 크기/참조 검사 |
| `ko/tova/img/bg_close.png` | 1,280 | 파일 크기/참조 검사 |
| `ko/tova/img/bg_pop.png` | 3,480,588 | 파일 크기/참조 검사 |
| `ko/tova/img/buy_intro_bg.jpg` | 727,741 | 파일 크기/참조 검사 |
| `ko/tova/img/buy_vdieo.mp4` | 31,954,132 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/tova/img/faq_intro_bg.png` | 933,519 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_angle.svg` | 243 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_answer.svg` | 294 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_buy_alarm.svg` | 929 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_buy_brochure.svg` | 2,196 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_buy_manual.svg` | 1,638 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_cafe.svg` | 1,171 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_change.svg` | 958 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_company.svg` | 887 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_complete.svg` | 1,088 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_countdown.svg` | 4,119 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_bus.svg` | 1,500 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_data.svg` | 428 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_modal.svg` | 600 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_network.svg` | 3,849 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_proportionality.svg` | 1,078 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_public.svg` | 1,657 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_subway.svg` | 2,152 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dia_trans.svg` | 1,271 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_dublecheck.svg` | 1,680 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_email.svg` | 1,146 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_facebook.svg` | 952 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_floating_buy.svg` | 651 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_floating_faq_k.svg` | 1,115 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_floating_faq_w.svg` | 1,173 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_footer_close.svg` | 333 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_id.svg` | 1,018 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_language.svg` | 1,324 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_link.svg` | 791 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_link_b.svg` | 789 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_lock.svg` | 1,607 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_network.svg` | 1,574 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_network_bulit.svg` | 219 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_pg_left.svg` | 1,056 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_pg_right.svg` | 1,046 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_phone.svg` | 727 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_primary_pub01.svg` | 1,344 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_primary_pub02.svg` | 4,311 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_primary_pub03.svg` | 990 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_primary_pub04.svg` | 359 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_pub_slide_01.svg` | 425 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_pub_slide_02.svg` | 403 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_pub_slide_03.svg` | 450 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_public_od.svg` | 983 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_public_pay.svg` | 797 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_public_station.svg` | 917 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_pw.svg` | 1,185 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_refresh.svg` | 566 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_send_email.svg` | 634 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_signout.svg` | 933 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_slide_bus.svg` | 2,080 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_slide_subway.svg` | 2,403 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_slide_trans.svg` | 1,056 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_social.svg` | 2,381 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_sync.svg` | 847 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_value_cursor.svg` | 1,810 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_value_frog_w.svg` | 2,968 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_value_ktdb_w.svg` | 1,550 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_value_public_w.svg` | 1,467 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_value_screen.svg` | 1,742 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_value_user_w.svg` | 2,059 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_way.svg` | 974 | 파일 크기/참조 검사 |
| `ko/tova/img/ico_won.svg` | 1,573 | 파일 크기/참조 검사 |
| `ko/tova/img/main_01.mp4` | 20,764,328 | 파일 크기/참조 검사; 10 MB 초과: 실제 요청될 때 전송 부담 |
| `ko/tova/img/primary_01.png` | 1,818,762 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_01_01.png` | 463,130 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_01_02.png` | 459,641 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_01_03.png` | 432,100 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_02.png` | 1,113,839 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_02_04.svg` | 2,350,587 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_03.png` | 1,493,077 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_03_01.png` | 675,653 | 파일 크기/참조 검사 |
| `ko/tova/img/primary_intro_bg.jpg` | 1,374,244 | 파일 크기/참조 검사 |
| `ko/tova/img/pub_01_01.svg` | 1,061,104 | 파일 크기/참조 검사 |
| `ko/tova/img/pub_02_01.png` | 885,214 | 파일 크기/참조 검사 |
| `ko/tova/img/pub_03_01.svg` | 1,171,979 | 파일 크기/참조 검사 |
| `ko/tova/img/pub_04_01.png` | 215,850 | 파일 크기/참조 검사 |
| `ko/tova/img/pub_slide_01.svg` | 14,324 | 파일 크기/참조 검사 |
| `ko/tova/img/pub_slide_02.svg` | 14,296 | 파일 크기/참조 검사 |
| `ko/tova/img/pub_slide_03.svg` | 14,107 | 파일 크기/참조 검사 |
| `ko/tova/img/public_intro_bg.jpg` | 1,227,248 | 파일 크기/참조 검사 |
| `ko/tova/img/public_od_bg.png` | 5,752,538 | 파일 크기/참조 검사 |
| `ko/tova/img/public_pay_bg.png` | 5,512,213 | 파일 크기/참조 검사 |
| `ko/tova/img/public_process_01.svg` | 2,558,063 | 파일 크기/참조 검사 |
| `ko/tova/img/public_process_02.svg` | 1,512,874 | 파일 크기/참조 검사 |
| `ko/tova/img/public_process_03.svg` | 1,988,424 | 파일 크기/참조 검사 |
| `ko/tova/img/public_station_bg.png` | 5,171,780 | 파일 크기/참조 검사 |
| `ko/tova/img/road_conclusion_bg.jpg` | 2,501,320 | 파일 크기/참조 검사 |
| `ko/tova/img/road_frog1.jpg` | 537,110 | 파일 크기/참조 검사 |
| `ko/tova/img/road_frog2.jpg` | 375,279 | 파일 크기/참조 검사 |
| `ko/tova/img/road_frog_markup.svg` | 42,284 | 파일 크기/참조 검사 |
| `ko/tova/img/road_intro_bg.jpg` | 1,402,015 | 파일 크기/참조 검사 |
| `ko/tova/img/road_process_bg1.jpg` | 356,883 | 파일 크기/참조 검사 |
| `ko/tova/img/road_process_bg2.jpg` | 366,423 | 파일 크기/참조 검사 |
| `ko/tova/img/road_process_soba.svg` | 34,825 | 파일 크기/참조 검사 |
| `ko/tova/img/road_process_warm_bg.svg` | 4,240 | 파일 크기/참조 검사 |
| `ko/tova/img/road_process_warm_fig1.svg` | 6,894 | 파일 크기/참조 검사 |
| `ko/tova/img/road_process_warm_fig2.svg` | 3,687 | 파일 크기/참조 검사 |
| `ko/tova/img/road_proportionality_bg.jpg` | 374,805 | 파일 크기/참조 검사 |
| `ko/tova/img/road_proportionality_fig1.svg` | 812,984 | 파일 크기/참조 검사 |
| `ko/tova/img/road_proportionality_fig2.svg` | 156,873 | 파일 크기/참조 검사 |
| `ko/tova/img/road_theorys_algo.svg` | 7,752 | 파일 크기/참조 검사 |
| `ko/tova/img/road_theorys_bg.jpg` | 2,254,517 | 파일 크기/참조 검사 |
| `ko/tova/img/road_theorys_modal.svg` | 5,589 | 파일 크기/참조 검사 |
| `ko/tova/img/road_tova.svg` | 1,096 | 파일 크기/참조 검사 |
| `ko/tova/img/sitemap_menu01.jpg` | 2,526,307 | 파일 크기/참조 검사 |
| `ko/tova/img/sitemap_menu02.jpg` | 2,193,661 | 파일 크기/참조 검사 |
| `ko/tova/img/sitemap_menu03.jpg` | 1,557,231 | 파일 크기/참조 검사 |
| `ko/tova/img/sitemap_menu04.jpg` | 1,455,733 | 파일 크기/참조 검사 |
| `ko/tova/img/slide_img_bus.png` | 1,592,555 | 파일 크기/참조 검사 |
| `ko/tova/img/slide_img_subway.png` | 1,996,522 | 파일 크기/참조 검사 |
| `ko/tova/img/slide_img_trans.png` | 1,634,816 | 파일 크기/참조 검사 |
| `ko/tova/img/tova_k.svg` | 1,099 | 파일 크기/참조 검사 |
| `ko/tova/img/tova_obj_k.svg` | 448 | 파일 크기/참조 검사 |
| `ko/tova/img/tova_obj_w.svg` | 318 | 파일 크기/참조 검사 |
| `ko/tova/img/tova_w.svg` | 1,066 | 파일 크기/참조 검사 |
| `ko/tova/img/tri_img.svg` | 888 | 파일 크기/참조 검사 |
| `ko/tova/img/value_feature_bg.jpg` | 799,271 | 파일 크기/참조 검사 |
| `ko/tova/img/value_feature_frog_bg.jpg` | 747,969 | 파일 크기/참조 검사 |
| `ko/tova/img/value_feature_ktdb_bg.jpg` | 434,092 | 파일 크기/참조 검사 |
| `ko/tova/img/value_feature_public_bg.jpg` | 512,907 | 파일 크기/참조 검사 |
| `ko/tova/img/value_feature_user_bg.jpg` | 277,532 | 파일 크기/참조 검사 |
| `ko/tova/img/value_intro_bg.jpg` | 1,954,590 | 파일 크기/참조 검사 |
| `ko/tova/img/value_intro_summary1.png` | 769,611 | 파일 크기/참조 검사 |
| `ko/tova/img/value_intro_summary2.jpg` | 1,375,068 | 파일 크기/참조 검사 |
| `ko/tova/img/value_screen1.png` | 587,131 | 파일 크기/참조 검사 |
| `ko/tova/img/value_screen2.png` | 565,370 | 파일 크기/참조 검사 |
| `ko/tova/img/value_screenM_01.png` | 144,980 | 파일 크기/참조 검사 |
| `ko/tova/img/value_screenM_02.png` | 286,803 | 파일 크기/참조 검사 |
| `ko/tova/img/value_screenM_03.png` | 216,104 | 파일 크기/참조 검사 |
| `ko/tova/img/value_screen_bg.svg` | 9,792 | 파일 크기/참조 검사 |
| `ko/tova/img/value_system_bg.jpg` | 1,254,858 | 파일 크기/참조 검사 |
| `ko/tova/img/zone_01_01.svg` | 692,223 | 파일 크기/참조 검사 |
| `ko/tova/img/zone_01_02.svg` | 701,151 | 파일 크기/참조 검사 |
| `ko/tova/img/zone_01_03.svg` | 9,404 | 파일 크기/참조 검사 |
| `ko/tova/img/zone_01_04.svg` | 4,372 | 파일 크기/참조 검사 |
| `ko/tova/img/zone_02_01.png` | 599,609 | 파일 크기/참조 검사 |
| `ko/tova/img/zone_03_01.png` | 369,812 | 파일 크기/참조 검사 |
| `ko/tova/index.html` | 5,140 | HTML: 동기 외부 스크립트 10, 이미지 0 (lazy 0), video 1, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/tova/js/common.js` | 87,328 | 텍스트 리소스 참조 검사; 외부 URL 12, 로컬 참조 확인 필요 1 |
| `ko/tova/js/index.js` | 5,646 | 텍스트 리소스 참조 검사 |
| `ko/tova/js/jquery-3.6.1.min.js` | 89,664 | 텍스트 리소스 참조 검사 |
| `ko/tova/js/jquery.mousewheel.min.js` | 2,680 | 텍스트 리소스 참조 검사 |
| `ko/tova/js/popup.js` | 8,396 | 텍스트 리소스 참조 검사 |
| `ko/tova/js/primary.js` | 7,155 | 텍스트 리소스 참조 검사 |
| `ko/tova/js/public.js` | 4,461 | 텍스트 리소스 참조 검사 |
| `ko/tova/js/road.js` | 3,957 | 텍스트 리소스 참조 검사 |
| `ko/tova/js/value.js` | 8,182 | 텍스트 리소스 참조 검사; 외부 URL 0, 로컬 참조 확인 필요 4 |
| `ko/tova/primary.html` | 20,735 | HTML: 동기 외부 스크립트 10, 이미지 26 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/tova/public.html` | 9,319 | HTML: 동기 외부 스크립트 10, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/tova/road.html` | 15,797 | HTML: 동기 외부 스크립트 10, 이미지 5 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/tova/value.html` | 17,788 | HTML: 동기 외부 스크립트 10, 이미지 2 (lazy 0), video 0, iframe 0; 외부 URL 8, 로컬 참조 확인 필요 0 |
| `ko/video_ex.html` | 2,009 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `portfolio/compilation.html` | 9,271 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `portfolio/ux.html` | 8,552 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `portfolio/video.html` | 8,558 | HTML: 동기 외부 스크립트 1, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 1, 로컬 참조 확인 필요 0 |
| `recruit/br_recruit.html` | 37,261 | HTML: 동기 외부 스크립트 7, 이미지 38 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `recruit/job_banner.json` | 1,840 | 파일 크기/참조 검사 |
| `recruit/job_list.json` | 14,341 | 파일 크기/참조 검사 |
| `recruit/job_part.json` | 1,244 | 파일 크기/참조 검사 |
| `recruit/recruit_apply.html` | 5,186 | HTML: 동기 외부 스크립트 8, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `recruit/recruit_faq.html` | 12,839 | HTML: 동기 외부 스크립트 6, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `recruit/recruit_view.html` | 8,461 | HTML: 동기 외부 스크립트 7, 이미지 0 (lazy 0), video 0, iframe 0; 외부 URL 0, 로컬 참조 확인 필요 0 |
| `scripts/performance_audit.py` | 10,208 | 파일 크기/참조 검사 |
| `software-header-footer-integration.md` | 5,271 | 파일 크기/참조 검사 |
| `문의하기 페이지 수정(2026-06-26).md` | 2,108 | 파일 크기/참조 검사 |
