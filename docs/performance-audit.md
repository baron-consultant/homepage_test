# 정적 사이트 로딩 성능 감사 및 개선 전·후 비교

> 측정 기준: `90c1cc9` 코드와 당시 성능 개선 작업. 이후 `homepage_test/main`의 `cebb14b`를 pull하고 개선 작업을 다시 적용했습니다. 아래 수치와 오류 목록은 pull 이전의 기록이며, 최신 코드 전체를 재측정한 결과가 아닙니다. pull 후에는 국문·영문 메인의 응답, 헤더 표시, 영상 재생 및 JavaScript 오류 없음을 확인했습니다.

측정일: 2026-09-15. 대상: 이 저장소의 로컬 정적 파일. 운영 서버에는 배포하지 않았습니다.

## 핵심 원인

1. 메인 배경 영상 `assets/img/index.mp4`: 118,043,547 bytes, 20.73초, 1920×1080 / 30fps, 약 45.55Mbps. 10Mbps 접속에서는 영상 비트레이트가 회선 속도보다 높습니다. 원본은 이미 moov 메타데이터가 앞에 있으므로 faststart 누락이 원인은 아닙니다. 음소거 배경에 AAC 오디오도 들어 있습니다.
2. 공통 메뉴: 같은 nav HTML을 헤더·사이트맵·푸터에서 각각 요청하며 캐시 방지 쿼리를 붙입니다. 메인에서 include 요청 5회가 발생했습니다.
3. 메인 head의 동기 스크립트 6개가 HTML 파싱을 막습니다. font-face에 font-display가 없어 글꼴을 기다리는 동안 글자가 늦게 표시될 수 있습니다.
4. 제품 페이지는 외부 CDN의 AOS·Lenis·GSAP를 동기 로드합니다. 외부 서버 지연·실패에 영향을 받는 구조이며, 이번 실측에서 관측한 요청 시간은 아래 리소스 표에 따로 기록했습니다.
5. TOVA는 초기 HTML의 main_01.mp4를 JS에서 main_1.mp4로 바꾸지만 후자가 로컬에 없어 404 및 재생 오류가 발생합니다. 일부 페이지는 빈 main 컨테이너만 있어 낮은 로딩 값이 콘텐츠 정상 표시를 뜻하지 않습니다.

## 적용한 개선

- 원본 영상은 보존하고 `assets/media/index-web.mp4`를 생성했습니다. H.264, 1080p/30fps 유지, CRF 24, 최대 비트레이트 4Mbps, 오디오 제거, faststart 적용입니다.
- 국문·영문 메인에 포스터 이미지를 추가하고, 새 영상을 연결했습니다. 초기 라이브러리 6개에 defer를 적용해 실행 순서를 유지하면서 HTML 파싱을 진행하게 했습니다.
- 공통 include 로더는 페이지 내 같은 URL의 진행 중/완료 요청을 공유합니다. 실패한 요청은 제거해 다음 호출에서 다시 시도할 수 있게 했습니다. 헤더·사이트맵·푸터 삽입 및 각 콜백은 그대로 실행합니다.
- 메인과 제품 사이트의 font.css에 font-display: swap을 적용했습니다. 웹폰트 다운로드 전에도 대체 글꼴로 표시됩니다.
- 국문 메인의 favicon은 같은 사이트의 상대 경로를 사용합니다.
- 채용 인트로 사진 4장은 3840×2100 JPEG에서 가로 1600px WebP(품질 82)로 변환했습니다. 합계 13,260,816 → 154,086 bytes (98.84% 감소), 원본 보존.
- 채용 모듈의 common.js import URL을 HTML과 일치시켜 공통 모듈 이중 실행을 제거했습니다. 원래는 쿼리 문자열 유무로 서로 다른 모듈로 인식됐습니다.
- R2 배포에서 scripts/docs/artifacts/.perf-tools를 제외해 감사 도구와 결과가 사이트 자산으로 배포되지 않도록 했습니다.

## 측정 조건과 해석

- Playwright 1.62.0, 실제 Edge/Chromium 153.0.4234.32, headless, Windows.
- 화면 1365×768, ko-KR, 매 실행 새 브라우저 컨텍스트, HTTP 캐시 비활성화, 서비스 워커 차단.
- CDP 네트워크 제한: 다운로드 10Mbps(1,250,000 bytes/s), 업로드 5Mbps, 지연 40ms. CPU 4배 감속.
- 주요 8개 경로를 개선 전·후 각각 3회, 탐색 시작부터 15초 관측했습니다. 표는 중앙값이며 실제 개별 실행값도 아래에 남겼습니다.
- 로컬 서버는 Range/206을 지원하며 압축 없는 정적 파일을 제공합니다. 외부 CDN과 분석 스크립트는 실제 요청하므로 외부 상황에 따른 변동이 남습니다.
- 로컬 실험은 운영 Cloudflare/R2의 DNS·TLS·캐시 적중·압축·회선 상태를 재현하지 않습니다. 운영 속도 개선 수치로 단정할 수 없습니다.
- load는 브라우저 load 이벤트이지 영상 전체 다운로드 완료가 아닙니다. 첫 프레임도 검은 프레임일 수 있으므로 15초 시점 재생 위치와 스크린샷을 함께 봐야 합니다.
- LCP는 15초 관측 구간 내 최대 콘텐츠 표시 후보입니다. 메인 LCP는 이번 실험에서 메뉴의 DIV/A로 기록됐고 배경 영상 표시 시간을 대표하지 못했습니다. 영상 첫 프레임과 재생 위치를 별도로 확인했습니다.
- 전송량은 관측된 CDP encodedDataLength 합계입니다. 진행 중인 영상도 포함하지만 헤더·모든 네트워크 비용을 포함하는 총선로 사용량은 아닙니다.
- 성능 타임라인은 15초 시점에 읽습니다. 각 페이지 1회차의 수신량/요청 목록에는 직후 스크린샷 캡처 동안의 이벤트가 조금 더 포함될 수 있습니다. 전후에 동일한 수집 순서를 사용했습니다.
- 장기 작업 초과시간은 15초 구간에서 각 50ms 초과 작업의 초과분 합계이며 Lighthouse TBT 점수가 아닙니다. CLS는 관측 구간 합계입니다.

- 3회 중앙값은 이 실험의 관측치이며 통계적 유의성을 검증한 결과는 아닙니다. 모바일은 기능 확인만 수행하며 모바일 성능 수치는 별도로 측정하지 않았습니다.

- 전후 수치는 여러 변경을 함께 적용한 결과입니다. 영상·defer·폰트·메뉴 변경 각각의 독립적인 기여율을 분리 측정하지 않았습니다.

## 페이지별 중앙값 비교

단위: ms. 개선율은 `(전−후)/전`이며 양수는 단축, 음수는 증가입니다. 미관측은 0초로 처리하지 않았습니다.

| 페이지 | DCL 전 → 후 | load 전 → 후 | load 단축률 | FCP 전 → 후 | LCP 전 → 후 |
|---|---:|---:|---:|---:|---:|
| `/ko/index.html` | 656.2 → 724.1 | 3,037.8 → 730.3 | +76.0% | 656.0 → 328.0 | 1,240.0 → 944.0 |
| `/en/index.html` | 665.3 → 704.0 | 3,054.4 → 708.8 | +76.8% | 676.0 → 340.0 | 1,264.0 → 940.0 |
| `/ko/br_value.html` | 631.3 → 629.9 | 632.5 → 631.5 | +0.2% | 1,032.0 → 996.0 | 1,360.0 → 996.0 |
| `/ko/dt_explain.html` | 648.6 → 606.2 | 649.4 → 609.7 | +6.1% | 1,004.0 → 976.0 | 1,360.0 → 976.0 |
| `/ko/tova/index.html` | 1,265.9 → 1,176.1 | 1,905.1 → 1,744.7 | +8.4% | 1,216.0 → 1,152.0 | 1,364.0 → 1,412.0 |
| `/ko/gaia/index.html` | 1,069.0 → 1,613.4 | 2,056.4 → 2,189.6 | -6.5% | 1,036.0 → 1,576.0 | 1,348.0 → 1,576.0 |
| `/ko/egbim/primary.html` | 1,904.0 → 2,027.9 | 7,702.1 → 7,714.8 | -0.2% | 1,876.0 → 1,796.0 | 3,376.0 → 3,380.0 |
| `/recruit/br_recruit.html` | 3,949.8 → 2,082.1 | 12,979.2 → 2,490.8 | +80.8% | 1,892.0 → 2,056.0 | 2,080.0 → 2,464.0 |

DCL: HTML 파싱 및 지연 실행 스크립트 완료. FCP: 첫 콘텐츠 표시. LCP: 가장 큰 콘텐츠 표시 후보.

### 메인 영상과 메뉴

| 페이지 | 지표 | 개선 전 | 개선 후 | 감소율 |
|---|---|---:|---:|---:|
| `/ko/index.html` | 첫 영상 프레임 (ms) | 3,023.4 | 525.2 | +82.6% |
| `/ko/index.html` | 15초 시점 영상 재생 위치 (s) | 0.0 | 14.2 | — |
| `/ko/index.html` | 메뉴 링크 DOM 준비 (ms) | 888.3 | 981.1 | -10.4% |
| `/ko/index.html` | 요청 수 | 24.0 | 23.0 | +4.2% |
| `/ko/index.html` | include 요청 수 | 5.0 | 3.0 | +40.0% |
| `/ko/index.html` | 약 15초 관측 수신량 (MB) | 18.1 | 9.1 | +49.9% |
| `/en/index.html` | 첫 영상 프레임 (ms) | 3,041.2 | 521.1 | +82.9% |
| `/en/index.html` | 15초 시점 영상 재생 위치 (s) | 0.0 | 14.2 | — |
| `/en/index.html` | 메뉴 링크 DOM 준비 (ms) | 936.3 | 965.0 | -3.1% |
| `/en/index.html` | 요청 수 | 24.0 | 23.0 | +4.2% |
| `/en/index.html` | include 요청 수 | 5.0 | 3.0 | +40.0% |
| `/en/index.html` | 약 15초 관측 수신량 (MB) | 18.0 | 8.9 | +50.4% |

### 레이아웃 이동 및 긴 작업

| 페이지 | CLS 전 → 후 | 50ms 초과 작업의 초과시간 합계 전 → 후 (ms) |
|---|---:|---:|
| `/ko/index.html` | 0.00000 → 0.00001 | 59.0 → 131.0 |
| `/en/index.html` | 0.00000 → 0.00000 | 110.0 → 188.0 |
| `/ko/br_value.html` | 0.00013 → 0.00020 | 254.0 → 207.0 |
| `/ko/dt_explain.html` | 0.00013 → 0.00013 | 240.0 → 231.0 |
| `/ko/tova/index.html` | 0.04333 → 0.04557 | 757.0 → 620.0 |
| `/ko/gaia/index.html` | 0.12720 → 0.12675 | 634.0 → 682.0 |
| `/ko/egbim/primary.html` | 0.07100 → 0.07057 | 832.0 → 871.0 |
| `/recruit/br_recruit.html` | 0.00308 → 0.00000 | 880.0 → 771.0 |

메인에서는 긴 작업 합계가 증가한 실행도 있습니다. 개선 후에는 영상이 실제 재생되는 상태이므로 정지 상태였던 개선 전과 실행 작업량도 다릅니다. 모든 지표가 개선됐다는 의미는 아닙니다.


영상 파일: **118.04 MB → 8.27 MB (92.99% 감소)**. 포스터 63.2 KB 추가.

## 전체 개별 측정값

| 단계 | 경로 | 회차 | TTFB | DCL | load | FCP | LCP | 첫 영상 프레임 | 수신 MB | JS 오류 수 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 전 | `/ko/index.html` | 1 | 134.3 | 788.7 | 3,291.6 | 792.0 | 1,308.0 | 3,273.4 | 18.1 | 0 |
| 전 | `/ko/index.html` | 2 | 3.8 | 656.2 | 3,037.8 | 656.0 | 1,240.0 | 3,023.4 | 18.1 | 0 |
| 전 | `/ko/index.html` | 3 | 4.4 | 616.1 | 2,996.8 | 620.0 | 1,204.0 | 2,976.1 | 18.0 | 0 |
| 전 | `/en/index.html` | 1 | 3.6 | 651.5 | 3,041.9 | 648.0 | 1,280.0 | 3,002.7 | 18.2 | 0 |
| 전 | `/en/index.html` | 2 | 5.2 | 701.3 | 3,094.1 | 712.0 | 1,256.0 | 3,080.4 | 17.9 | 0 |
| 전 | `/en/index.html` | 3 | 3.3 | 665.3 | 3,054.4 | 676.0 | 1,264.0 | 3,041.2 | 18.0 | 0 |
| 전 | `/ko/br_value.html` | 1 | 3.4 | 588.6 | 590.2 | 980.0 | 1,316.0 | 미관측 | 0.9 | 0 |
| 전 | `/ko/br_value.html` | 2 | 3.6 | 675.9 | 676.9 | 1,032.0 | 1,364.0 | 미관측 | 0.9 | 0 |
| 전 | `/ko/br_value.html` | 3 | 3.7 | 631.3 | 632.5 | 1,060.0 | 1,360.0 | 미관측 | 0.9 | 0 |
| 전 | `/ko/dt_explain.html` | 1 | 4.1 | 648.6 | 649.4 | 992.0 | 1,340.0 | 미관측 | 0.9 | 0 |
| 전 | `/ko/dt_explain.html` | 2 | 6.4 | 672.5 | 673.5 | 1,004.0 | 1,420.0 | 미관측 | 0.9 | 0 |
| 전 | `/ko/dt_explain.html` | 3 | 3.5 | 633.0 | 634.1 | 1,044.0 | 1,360.0 | 미관측 | 0.9 | 0 |
| 전 | `/ko/tova/index.html` | 1 | 3.6 | 1,265.9 | 2,137.5 | 1,216.0 | 1,364.0 | 미관측 | 1.2 | 2 |
| 전 | `/ko/tova/index.html` | 2 | 6.6 | 1,266.3 | 1,905.1 | 1,236.0 | 1,436.0 | 미관측 | 1.2 | 2 |
| 전 | `/ko/tova/index.html` | 3 | 3.6 | 1,075.2 | 1,901.2 | 1,028.0 | 1,260.0 | 미관측 | 1.2 | 2 |
| 전 | `/ko/gaia/index.html` | 1 | 5.2 | 1,181.0 | 2,089.9 | 1,128.0 | 1,552.0 | 2,084.1 | 18.4 | 1 |
| 전 | `/ko/gaia/index.html` | 2 | 4.4 | 1,010.8 | 2,056.4 | 980.0 | 1,336.0 | 2,066.2 | 18.1 | 1 |
| 전 | `/ko/gaia/index.html` | 3 | 3.9 | 1,069.0 | 2,024.7 | 1,036.0 | 1,348.0 | 2,033.4 | 18.0 | 1 |
| 전 | `/ko/egbim/primary.html` | 1 | 3.6 | 1,904.0 | 7,697.0 | 1,876.0 | 3,376.0 | 미관측 | 9.2 | 0 |
| 전 | `/ko/egbim/primary.html` | 2 | 5.3 | 1,839.9 | 7,702.1 | 1,804.0 | 3,352.0 | 미관측 | 9.2 | 0 |
| 전 | `/ko/egbim/primary.html` | 3 | 5.2 | 2,067.2 | 7,703.8 | 2,020.0 | 3,404.0 | 미관측 | 9.2 | 0 |
| 전 | `/recruit/br_recruit.html` | 1 | 4.4 | 4,306.0 | 12,971.9 | 1,884.0 | 2,084.0 | 미관측 | 15.7 | 1 |
| 전 | `/recruit/br_recruit.html` | 2 | 3.7 | 3,932.8 | 12,993.3 | 1,960.0 | 2,080.0 | 미관측 | 15.7 | 1 |
| 전 | `/recruit/br_recruit.html` | 3 | 4.0 | 3,949.8 | 12,979.2 | 1,892.0 | 2,076.0 | 미관측 | 15.7 | 1 |
| 후 | `/ko/index.html` | 1 | 126.0 | 741.2 | 745.1 | 428.0 | 944.0 | 577.4 | 9.1 | 0 |
| 후 | `/ko/index.html` | 2 | 4.3 | 674.4 | 678.0 | 328.0 | 928.0 | 481.4 | 9.1 | 0 |
| 후 | `/ko/index.html` | 3 | 4.0 | 724.1 | 730.3 | 328.0 | 992.0 | 525.2 | 9.1 | 0 |
| 후 | `/en/index.html` | 1 | 3.9 | 704.0 | 708.8 | 360.0 | 940.0 | 542.9 | 8.9 | 0 |
| 후 | `/en/index.html` | 2 | 3.9 | 703.7 | 704.4 | 340.0 | 940.0 | 493.6 | 8.9 | 0 |
| 후 | `/en/index.html` | 3 | 4.7 | 718.9 | 726.2 | 340.0 | 988.0 | 521.1 | 8.9 | 0 |
| 후 | `/ko/br_value.html` | 1 | 3.7 | 629.9 | 631.5 | 996.0 | 996.0 | 미관측 | 0.9 | 0 |
| 후 | `/ko/br_value.html` | 2 | 4.8 | 613.1 | 615.2 | 972.0 | 972.0 | 미관측 | 0.9 | 0 |
| 후 | `/ko/br_value.html` | 3 | 4.4 | 649.4 | 650.5 | 1,108.0 | 1,108.0 | 미관측 | 0.9 | 0 |
| 후 | `/ko/dt_explain.html` | 1 | 4.7 | 654.9 | 656.0 | 1,020.0 | 1,020.0 | 미관측 | 0.9 | 0 |
| 후 | `/ko/dt_explain.html` | 2 | 16.0 | 589.0 | 590.6 | 972.0 | 972.0 | 미관측 | 0.9 | 0 |
| 후 | `/ko/dt_explain.html` | 3 | 12.9 | 606.2 | 609.7 | 976.0 | 976.0 | 미관측 | 0.9 | 0 |
| 후 | `/ko/tova/index.html` | 1 | 5.7 | 1,176.1 | 1,744.7 | 1,152.0 | 4,204.0 | 미관측 | 1.2 | 2 |
| 후 | `/ko/tova/index.html` | 2 | 3.7 | 1,454.8 | 2,056.8 | 1,412.0 | 1,412.0 | 미관측 | 1.1 | 2 |
| 후 | `/ko/tova/index.html` | 3 | 4.1 | 965.1 | 1,537.8 | 976.0 | 976.0 | 미관측 | 1.1 | 2 |
| 후 | `/ko/gaia/index.html` | 1 | 3.9 | 1,673.4 | 2,276.4 | 1,648.0 | 1,648.0 | 2,279.2 | 17.7 | 1 |
| 후 | `/ko/gaia/index.html` | 2 | 5.0 | 1,159.3 | 2,184.1 | 1,112.0 | 1,460.0 | 2,192.6 | 17.8 | 1 |
| 후 | `/ko/gaia/index.html` | 3 | 3.9 | 1,613.4 | 2,189.6 | 1,576.0 | 1,576.0 | 2,205.8 | 17.4 | 1 |
| 후 | `/ko/egbim/primary.html` | 1 | 3.8 | 1,840.5 | 7,725.3 | 1,796.0 | 3,264.0 | 미관측 | 9.2 | 0 |
| 후 | `/ko/egbim/primary.html` | 2 | 3.7 | 2,027.9 | 7,705.9 | 1,616.0 | 3,380.0 | 미관측 | 9.2 | 0 |
| 후 | `/ko/egbim/primary.html` | 3 | 3.6 | 2,042.1 | 7,714.8 | 2,016.0 | 3,380.0 | 미관측 | 9.2 | 0 |
| 후 | `/recruit/br_recruit.html` | 1 | 4.2 | 2,082.1 | 2,490.8 | 1,780.0 | 2,464.0 | 미관측 | 2.6 | 0 |
| 후 | `/recruit/br_recruit.html` | 2 | 4.9 | 2,226.0 | 2,635.8 | 2,120.0 | 2,600.0 | 미관측 | 2.6 | 0 |
| 후 | `/recruit/br_recruit.html` | 3 | 7.1 | 1,843.6 | 2,489.1 | 2,056.0 | 2,404.0 | 미관측 | 2.6 | 0 |

## 느린 개별 요청: 개선 전 각 페이지 1회차

완료된 Resource Timing 요청 중 duration 상위 5개입니다. 다운로드 중인 대형 영상은 이 목록에 없을 수 있습니다. 외부 서버는 크기/세부 타이밍을 공개하지 않을 수 있습니다.

| 페이지 | 리소스 | 요청 시작 (ms) | 소요 (ms) | transferSize (bytes) |
|---|---|---:|---:|---:|
| `/ko/index.html` | `/assets/js/lib/jquery-3.6.1.min.js` | 155.0 | 468.7 | 89964 |
| `/ko/index.html` | `/assets/js/lib/gsap.min.js` | 155.1 | 452.7 | 72523 |
| `/ko/index.html` | `/assets/js/lib/scrolltrigger.min.js` | 155.1 | 433.0 | 43689 |
| `/ko/index.html` | `/assets/font/NotoKR-Bold/notokr-bold.woff2` | 897.4 | 394.0 | 135268 |
| `/ko/index.html` | `/assets/js/common.js` | 155.8 | 384.4 | 12589 |
| `/en/index.html` | `/assets/font/NotoKR-Bold/notokr-bold.woff2` | 845.9 | 402.8 | 135268 |
| `/en/index.html` | `/assets/font/NotoKR-Regular/notokr-regular.woff2` | 845.6 | 371.0 | 135260 |
| `/en/index.html` | `/assets/js/lib/jquery-3.6.1.min.js` | 91.1 | 356.4 | 89964 |
| `/en/index.html` | `/assets/js/lib/gsap.min.js` | 91.5 | 339.9 | 72523 |
| `/en/index.html` | `/assets/js/lib/scrolltrigger.min.js` | 92.0 | 301.4 | 43689 |
| `/ko/br_value.html` | `/assets/font/NotoKR-Regular/notokr-regular.woff2` | 741.1 | 501.5 | 135260 |
| `/ko/br_value.html` | `/assets/font/NotoKR-Bold/notokr-bold.woff2` | 741.7 | 501.1 | 135268 |
| `/ko/br_value.html` | `/assets/font/NotoKR-Light/notokr-light.woff2` | 741.4 | 500.7 | 131396 |
| `/ko/br_value.html` | `/assets/font/NotoKR-Medium/notokr-medium.woff2` | 740.9 | 385.6 | 134136 |
| `/ko/br_value.html` | `/assets/js/lib/jquery-3.6.1.min.js` | 85.4 | 341.2 | 89964 |
| `/ko/dt_explain.html` | `/assets/font/NotoKR-Light/notokr-light.woff2` | 775.6 | 507.4 | 131396 |
| `/ko/dt_explain.html` | `/assets/font/NotoKR-Bold/notokr-bold.woff2` | 776.4 | 506.9 | 135268 |
| `/ko/dt_explain.html` | `/assets/font/NotoKR-Regular/notokr-regular.woff2` | 774.8 | 476.6 | 135260 |
| `/ko/dt_explain.html` | `/assets/font/NotoKR-Medium/notokr-medium.woff2` | 773.5 | 446.9 | 134136 |
| `/ko/dt_explain.html` | `/assets/js/lib/jquery-3.6.1.min.js` | 110.5 | 345.4 | 89964 |
| `/ko/tova/index.html` | `www.googletagmanager.com/gtag/js` | 83.6 | 578.2 | 0 |
| `/ko/tova/index.html` | `/ko/tova/css/style.css` | 85.9 | 576.6 | 196842 |
| `/ko/tova/index.html` | `/ko/tova/js/jquery-3.6.1.min.js` | 86.7 | 411.8 | 89964 |
| `/ko/tova/index.html` | `/ko/tova/js/common.js` | 87.4 | 410.7 | 87628 |
| `/ko/tova/index.html` | `/ko/tova/font/NotoKR-Bold/notokr-bold.woff2` | 914.3 | 392.4 | 135268 |
| `/ko/gaia/index.html` | `www.googletagmanager.com/gtag/js` | 90.8 | 726.4 | 0 |
| `/ko/gaia/index.html` | `cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js` | 96.4 | 719.9 | 29391 |
| `/ko/gaia/index.html` | `www.google-analytics.com/g/collect` | 1978.0 | 507.7 | 0 |
| `/ko/gaia/index.html` | `/ko/gaia/font/NotoKR-Medium/notokr-medium.woff2` | 1258.6 | 448.1 | 134136 |
| `/ko/gaia/index.html` | `/ko/gaia/css/style.css` | 92.8 | 447.1 | 257849 |
| `/ko/egbim/primary.html` | `/ko/egbim/img/printarea_img_01.png` | 1172.2 | 6506.4 | 1019673 |
| `/ko/egbim/primary.html` | `/ko/egbim/img/primary_style_bg.png` | 1149.4 | 6289.8 | 1043895 |
| `/ko/egbim/primary.html` | `/ko/egbim/img/primary_route_bg.png` | 1140.3 | 6137.5 | 981227 |
| `/ko/egbim/primary.html` | `/ko/egbim/img/printarea_img_02.png` | 1173.3 | 6133.5 | 661526 |
| `/ko/egbim/primary.html` | `/ko/egbim/img/primary_block_bg.png` | 1152.0 | 6128.2 | 906691 |
| `/recruit/br_recruit.html` | `/assets/img/recruit/recruit_intro_img02.jpg` | 99.8 | 12822.6 | 4212457 |
| `/recruit/br_recruit.html` | `/assets/img/recruit/recruit_intro_img01.jpg` | 99.7 | 12431.7 | 3757912 |
| `/recruit/br_recruit.html` | `/assets/img/recruit/recruit_intro_img04.jpg` | 100.0 | 11263.7 | 2874939 |
| `/recruit/br_recruit.html` | `/assets/img/recruit/recruit_intro_img03.jpg` | 99.9 | 10169.8 | 2416708 |
| `/recruit/br_recruit.html` | `/assets/img/recruit/recruit_sub3_ico_step05.svg` | 104.0 | 5901.3 | 2879 |

## 기존 오류 및 추가 개선 과제

- 채용 페이지의 개선 전 load 중앙값 약 13초는 원본 사진 4장이 다운로드 대역폭을 점유한 영향이 컸습니다. 이중 공통 모듈 실행은 urlParams 중복 선언 오류도 만들었습니다.
- 빈 main 컨테이너가 있는 국문·영문 페이지는 각 11개입니다: br_future, br_tech, br_value, dt_explain, dt_sw, dt_use, dx, sv_bigroom, sv_solution, sv_solution_construction, sv_solution_operation. 본문 복구는 성능 최적화와 별도 과제입니다.
- TOVA 파일명 불일치/누락은 필요한 영상 세트의 의도를 확인해야 하므로 임의로 다른 영상을 연결하지 않았습니다.
- 채용 지원 목록(recruit/recruit_apply.html)의 기존 assets/js/apply.js는 브라우저에서 Invalid or unexpected token을 발생시킵니다. Node 구문 검사에서도 400행 부근 오류를 검출했습니다. 이번에 수정한 채용 메인(recruit/br_recruit.html)과 다른 페이지이며 별도 수정이 필요합니다.
- GAIA/TOVA의 초기 play() 직후 pause() 호출은 AbortError를 발생시킵니다. 제품 페이지는 의도적인 2.8초 인트로 대기도 있습니다.
- 일부 빈 본문 페이지, 누락된 이미지/폰트는 아래 전체 브라우저 점검 결과를 확인해야 합니다. 404를 최적화 성공으로 간주하지 않습니다.
- EGBIM 주요기능의 약 7.7초 load는 0.66~1.04MB 규모의 배경/기능 이미지 여러 장이 주로 차지하며 이번에는 영상·채용 사진 외의 이미지를 변환하지 않아 거의 그대로 남았습니다.
- R2 배포 workflow는 HTML과 일부 공통 JS에 no-cache, no-store, must-revalidate를 설정합니다. 재방문 캐시 효과를 제한하지만 이번 cold-cache 전후 실험에서는 캐시를 항상 껐으므로 개선율에 반영하지 않았습니다.
- 대형 zip/백업/다운로드 파일은 실제 페이지에서 요청될 때만 초기 로딩에 영향을 줍니다. 저장소 용량과 페이지 전송량은 다릅니다.
- 추가 후보: 제품 영상도 비트레이트 축소, 동일 버전 CDN 라이브러리의 로컬 제공, 화면 아래 이미지/iframe 지연 로딩, 배포 캐시 정책 개선. 이번에는 대량 적용하지 않았습니다.

## 범위와 산출물

- [전체 파일 스캔 목록](performance-file-inventory.md): 개선 전 3,932개 파일 크기·참조 검사, HTML 239개(샘플·include 포함).
- [전체 페이지 브라우저 점검](performance-page-smoke.md): include 조각과 CKEditor 샘플을 제외한 모든 HTML. 백업·기타 페이지도 포함합니다.
- 주요 8개 경로의 성능 비교는 모든 페이지가 같은 속도로 개선됐다는 뜻이 아닙니다. 전체 페이지 점검은 초기 탐색 검사이며 모든 버튼/폼/스크롤 조합의 완전한 기능 테스트는 아닙니다.
- 원시 결과와 스크린샷: `artifacts/performance/{before,after}.json`, `before-*.png`, `after-*.png`. 로컬 산출물은 gitignore에 포함했습니다. 이 문서에는 각 측정값과 핵심 요청을 보존했습니다.

## 재현 방법

```powershell
python -m pip install --target .perf-tools playwright==1.62.0 imageio-ffmpeg==0.6.0
python scripts/performance_audit.py --inventory
# 개선 전 코드에서 실행
python scripts/performance_audit.py --label before --runs 3 --seconds 15
# 개선 적용 후 실행
python scripts/performance_audit.py --label after --runs 3 --seconds 15
python scripts/performance_audit.py --smoke --label smoke-after
python scripts/performance_inventory_report.py
python scripts/performance_report.py
```

설치된 Microsoft Edge가 필요합니다. before.json은 개선 전 코드에서 수집한 결과를 보존해야 합니다. 운영 주소 실측 시 --base https://도메인을 지정할 수 있지만 운영 배포 전·후를 별도로 측정해야 합니다.

## 배포 시 확인

`assets/media/`의 영상·포스터·채용 WebP 4장을 HTML과 함께 배포해야 합니다. 기존 `img` 디렉터리는 git 및 R2 동기화 제외 대상이므로 새 자산을 `assets/media`에 저장했습니다. 새 영상과 사진은 손실 압축이므로 큰 화면에서 화질을 확인하세요. 원본은 그대로 남아 있습니다.
