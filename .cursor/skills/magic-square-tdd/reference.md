# D-* Logic 테스트 ID

| ID | 계층 | 요약 |
|----|------|------|
| D-001 | control | 대각선 1개만 합≠34 → **실패** (Red / Mom S2) |
| D-002 | control | 슬라이드 정답 격자 → **통과** (Green / Mom S3) |
| D-003 | control | 행 1개 합≠34 → 실패 + 위반 선 식별 |
| D-004 | control | 열 1개 합≠34 → 실패 + 위반 선 식별 |
| D-005 | control | 10선 모두 합=34 → 통과 |
| D-006 | control | OO 과제 픽스처 재현 (Mom S1) |
| D-007 | entity | `MagicSquare` 4×4·빈칸 2·1~16 (v0.2+) |
| D-008 | control | `MagicConstant` SSOT — 34/16/4 리터럴 산재 없음 |
