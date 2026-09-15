# Laragon 이미지 404 / R2 연결 확인

확인일: 2026-09-15. 코드 기준: `homepage_test/main`의 `cebb14b`와 로컬 성능 개선 작업.

## 결론

이번 로컬 이미지 오류는 R2 바인딩 변경 때문이 아니라 **접속 주소에 따른 경로 차이와 로컬 이미지 누락**으로 재현됐습니다. Laragon Apache와 Python 미리보기 서버는 로컬 디스크를 읽으며 R2를 직접 조회하지 않습니다.

Laragon에서는 **[http://baron.test/ko/index.html](http://baron.test/ko/index.html)** 로 접속하세요. 기존 가상 호스트의 DocumentRoot는 `C:/laragon/www/baron`입니다.

## 실제 요청 비교

| 요청 | 결과 |
|---|---|
| `http://localhost/assets/img/logo_c.svg` | 404 |
| `http://localhost/baron/assets/img/logo_c.svg` | 200 |
| `http://baron.test/ko/index.html` | 200 |
| 로컬 `/ko/kngil/img/logo_kngil.svg` — 복원 전 | 404, 파일 없음 |
| [운영 사이트의 같은 KNGIL 로고](https://baroncs.co.kr/ko/kngil/img/logo_kngil.svg) | 200, image/svg+xml |
| [운영 사이트의 KNGIL 기능 이미지](https://baroncs.co.kr/ko/kngil/img/primary/img_area_01.png) | 200, image/png |

`localhost/baron`으로 접속하면 HTML의 `/assets/...`는 `localhost/assets/...`로 해석됩니다. `baron.test`는 프로젝트 자체가 사이트 루트이므로 이 차이가 없습니다. 다른 Laragon 프로젝트에 영향을 주는 전역 rewrite는 추가하지 않았습니다.

`.gitignore`의 `**/img/` 때문에 새로운 이미지 폴더는 git pull로 내려오지 않습니다. R2 배포 workflow도 `img/*`, `*/img/*`를 제외하므로 GitHub에서 이미지를 자동 보충하는 구조가 아닙니다.

## R2 설정 확인 범위

- [wrangler.toml](../cloudflare-worker/wrangler.toml)의 Worker 이름: `baron-auth-gateway`
- 바인딩: `SITE_BUCKET`
- 설정된 버킷 이름: **`baron-hompage-test`** (파일에 적힌 정확한 문자열)
- [R2 배포 workflow](../.github/workflows/deploy-r2.yml)의 업로드 버킷: GitHub Actions Secret `CF_R2_BUCKET` 값
- 실제 Cloudflare 대시보드 바인딩이나 GitHub Secret 값은 직접 조회하지 않았으므로, 두 배포 설정의 현재 운영 값이 일치한다고 단정하지 않습니다. 이번 로컬 오류는 이 값에 의존하지 않습니다.
- `test.baroncs.co.kr`은 이번 실행 환경에서 DNS 조회 실패로 HTTP 응답을 확인하지 못했습니다.
- R2 버킷·Worker·배포 설정을 변경하거나 배포하지 않았습니다.

## 수행한 복원

- 현재 HTML/CSS와 브라우저 오류에서 발견한 누락 이미지 참조 230개 확인.
- 공개 운영 사이트에서 HTTP 200과 이미지 Content-Type이 확인된 **211개 / 59,497,809 bytes**를 로컬에 복원.
- 기존 로컬 파일은 덮어쓰지 않았습니다. 로그인 리다이렉트는 따라가지 않았습니다.
- 19개 이미지 참조는 운영에서도 404여서 복원하지 못했습니다. 정적 CSS의 미사용 참조도 포함될 수 있으므로 19개 모두 화면에서 깨진다는 뜻은 아닙니다.
- 복원한 `img` 파일은 기존 Git 제외 정책을 따릅니다. 이미 운영 사이트에 있는 파일을 로컬로 복사한 작업입니다.

## 브라우저 재검증

- 국문·영문 메인, GAIA 메인, EGBIM 주요기능: 관측한 HTTP 오류 0, 깨진 img 요소 0.
- KNGIL 6개 페이지: 깨진 img 요소 0. 주요기능 화면의 복원 전 깨진 img 요소 36개가 모두 사라졌습니다.
- KNGIL 가이드 모달의 `kngil_guide_poster.jpg`는 운영에서도 404입니다. `kngil_guide.mp4`는 로컬 404, 운영 HEAD 요청 403입니다. 이 가이드 자료는 별도로 남아 있습니다.
- 확인 페이지: analysis, buy, primary, provided, results, value. 최초 진입 후 2초 관측이며 모든 모달·로그인 동작을 검증한 것은 아닙니다.

## 다시 복원할 때

```powershell
# 누락 참조 개수만 확인
python scripts/restore_local_images.py
# 공개 운영 이미지 중 로컬에 없는 파일만 복원
python scripts/restore_local_images.py --download
```

진단 원시 결과는 `artifacts/performance/r2-image-probes.json`, `local-image-audit.json`, `restored-local-images.json`, `local-image-after.json`에 보관했습니다.

## 운영에서도 404인 이미지 참조

- `/asset/img/pr/pr_intro_bg.png`
- `/en/egbim/img/btn_next.png`
- `/en/egbim/img/btn_prev.png`
- `/en/gaia/img/ico_network_bulit.svg`
- `/en/gaia/img/logo_gaia.svg`
- `/img/captcha2.png`
- `/ko/egbim/img/btn_next.png`
- `/ko/egbim/img/btn_prev.png`
- `/ko/egbim/img/value_feature_bg.jpg`
- `/ko/gaia/img/ico_network_bulit.svg`
- `/ko/gaia/img/logo_gaia.svg`
- `/ko/kngil/img/buy_intro_bg.png`
- `/ko/kngil/img/ico_pripary_civil.svg`
- `/ko/kngil/img/ico_pripary_command.svg`
- `/ko/kngil/img/ico_pripary_my.svg`
- `/ko/kngil/img/primary_intro_bg.png`
- `/ko/kngil/img/primary_menu_bg.png`
- `/ko/kngil/img/primary_route_bg.png`
- `/ko/kngil/img/video/kngil_guide_poster.jpg`
