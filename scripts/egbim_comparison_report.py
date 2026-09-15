"""Write the measured before/after summary without treating timeouts as zero."""
import json
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
folder = ROOT / 'artifacts/performance/egbim-interface-comparison'
rows = json.loads((folder / 'measurements.json').read_text(encoding='utf-8'))
assert len(rows) == 6
before = [r for r in rows if r['mode'] == 'limited-before']
after = [r for r in rows if r['mode'] == 'limited-after']
assert all(r['metrics']['navigation']['loadEventEnd'] == 0 for r in before)
assert all(r['metrics']['navigation']['loadEventEnd'] > 0 for r in after)
load = median(r['metrics']['navigation']['loadEventEnd'] for r in after) / 1000
header = median(r['metrics']['headerReady'] for r in after) / 1000
before_lcp = median(r['metrics']['lcp']['ms'] for r in before) / 1000
after_lcp = median(r['metrics']['lcp']['ms'] for r in after) / 1000
assert all(r['metrics']['lcp']['url'].endswith('interface_intro_bg.perf.webp') for r in rows)
checks = json.loads((ROOT / 'artifacts/performance/egbim-interface-after/sequence-check.json').read_text())
assert len(checks) == 4 and all(r['passed'] for r in checks)
text = f'''# EG-BIM 인터페이스 로딩 개선

## 원인

- 운영 페이지에서 스크롤 전 PNG 104장, 총 93.87 MB를 동시에 요청하는 코드 확인했음.
- 이미지 요청이 첫 화면 배경과 메뉴 다운로드를 지연시키는 원인으로 확인됐음.

## 적용 내용

- 한글·영문 페이지의 프레임 로딩을 현재 위치와 주변 프레임 중심으로 변경했음.
- 동시 다운로드를 최대 4개로 제한하고, 빠르게 이동하면 대기 목록을 최신 위치로 교체하도록 적용했음.
- 첫 화면에서는 기존 WebP 이미지를 유지하고, 스크롤로 해당 구간에 접근할 때 PNG 요청을 시작하도록 적용했음.
- 새 프레임의 다운로드·디코딩이 끝나면 표시하고, 실패하면 마지막 정상 이미지를 유지하도록 적용했음.
- 기존 영문 모바일 정적 이미지 동작을 유지했음.
- 한글·영문 HTML의 JS 주소에 버전을 추가해 이전 브라우저 캐시와 구분했음.
- 신규 이미지 생성 없이 기존 이미지 경로를 사용했으므로 추가 R2 이미지 업로드가 필요하지 않음.

## 전후 측정 결과

- 실제 HTTP 서버에서 수정 전 파일과 수정 후 파일을 같은 주소로 제공해 각각 3회 측정했음.
- Edge, 1365×768, 캐시 비활성화, 다운로드 10 Mbps, 지연 40 ms, CPU 4배 제한, 스크롤 없이 35초 관찰 조건을 적용했음.
- 아래 수치는 중앙값이며, 로컬 비교 결과로 운영 배포 후 실측값과 구분했음.

| 항목 | 개선 전 | 개선 후 |
|---|---:|---:|
| 페이지 load 완료 | 35초 내 미완료 | {load:.2f}초 |
| 첫 화면 배경 표시(LCP) | {before_lcp:.2f}초 | {after_lcp:.2f}초 |
| 초기 애니메이션 PNG 요청 | 104개 | 0개 |
| 35초 동안 수신한 데이터 | {median(r['receivedBytes'] for r in before)/1e6:.2f} MB, 다운로드 진행 중 | {median(r['receivedBytes'] for r in after)/1e6:.2f} MB, 로드 완료 |

- load 완료 시간은 관찰 하한 35초와 비교해도 최소 {35-load:.2f}초 단축됐음. 개선 전 정확한 완료 시간은 측정하지 않았음.
- 동일한 배경 이미지의 LCP는 약 {(1-after_lcp/before_lcp)*100:.1f}% 단축됐음.
- 개선 후 메뉴 표시 중앙값은 {header:.2f}초로 확인됐음.
- 수정 전 운영 서버에서도 동일한 제한 조건으로 3회 모두 35초 내 load 미완료를 확인했음.

## 검증 및 반영 상태

- 한글·영문 데스크톱과 모바일 4개 조건에서 초기 PNG 요청 0개와 정상 이미지 표시를 확인했음.
- 애니메이션 활성 화면에서 중간·마지막·역방향 프레임 표시, 요청 실패 시 정상 이미지 유지와 후속 프레임 복구를 검증했음.
- 테스트 중 동시 프레임 요청 최대 4개와 JavaScript 오류 0건을 확인했음.
- 전후 HTTP 성능 측정에서 HTTP 4xx/5xx 및 JavaScript 오류 0건을 확인했음.
- 이미지 원본 용량은 유지했으므로 느린 네트워크의 빠른 스크롤에서는 준비된 이미지를 유지하며 새 프레임을 기다릴 수 있음.
- 첫 화면 배경 약 2.91 MB는 남아 있어 추가 압축 검토 대상으로 정리했음.
- 로컬 파일에 적용 완료했으며, Git push 및 운영 배포는 진행하지 않았음.

측정 원본: `artifacts/performance/egbim-interface-comparison/measurements.json`에 기록했음.
기능 검증 원본: `artifacts/performance/egbim-interface-after/sequence-check.json`에 기록했음.
'''
(ROOT / 'docs/egbim-interface-improvement.md').write_text(text, encoding='utf-8')
print(json.dumps({'loadSeconds':load,'beforeLcpSeconds':before_lcp,'afterLcpSeconds':after_lcp,'headerSeconds':header}))
