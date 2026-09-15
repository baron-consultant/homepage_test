# 배포 전 최종 점검 — 업로드 후 재확인

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
