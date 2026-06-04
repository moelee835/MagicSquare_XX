# MagicSquare_XX

4×4 **마방진(Magic Square)** 학습·설계 프로젝트. Mom Test로 문제를 검증한 뒤, **10개 선(행4·열4·대각2) 합 34** 검증에 우선 범위를 둡니다.

| 항목 | 내용 |
|------|------|
| 워크북 ID | MagicSquare_1004 |
| 현재 단계 | 문제 정의 · PRD v0.1 (구현 전) |
| 설계 관점 | ECB (Entity–Control–Boundary) — 단계적 적용 |

---

## 문제 한 줄

OO 과제에서 빈 칸 2개를 채운 뒤 합을 맞췄다고 생각했지만 **대각선 검산을 하나 빠뜨려**, 틀린 상태로 **20분**을 쓴 뒤에야 틀림을 알게 되는 패턴을 줄이는 것이 목표입니다.

**v0.1 초점:** 자동 풀이·GUI가 아니라 **검증 규칙(Rule) + Command + Test Loop**.

---

## 도메인

| 규칙 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (중복 없음) |
| 목표 합 | **34** (각 선) |
| 빈 칸 | `0` × **2** |
| 검증 선 | **10선** — 행 4, 열 4, 대각선 ↘·↙ 각 1 |

예시(슬라이드): 빈 칸 2개를 채워 모든 선의 합이 34가 되도록 맞춥니다.

---

## 프로젝트 구조

```
MagicSquare_XX/
├── README.md
├── docs/
│   └── PRD.md                          # 제품 요구사항 v0.1
├── Report/
│   ├── 01.MagicSquare_1004-MomTest-보고서.md
│   └── 01.MagicSquare_ProblemDefinition_Report.md
└── Prompting/
    └── 01.MagicSquare_1004-Export-Transcript.md
```

| 폴더 | 용도 |
|------|------|
| `docs/` | PRD, 요구사항·AC |
| `Report/` | Mom Test, 문제 정의 보고서 |
| `Prompting/` | Cursor 대화 Export |

> `src/`, `tests/` — PRD v0.1 구현 시 추가 예정 (`SquareValidator`, pytest 등).

---

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | v0.1 범위, 기능·도메인 요구사항, 성공 기준(AC) |
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test + R-G-I-O + 8계층(세션 3) |
| [Report/01.MagicSquare_1004-MomTest-보고서.md](Report/01.MagicSquare_1004-MomTest-보고서.md) | STEP 1 인터뷰 원문 정리 |
| [Prompting/01.MagicSquare_1004-Export-Transcript.md](Prompting/01.MagicSquare_1004-Export-Transcript.md) | 세션 대화 Export |

---

## v0.1 범위

### 포함

- **Rule:** 10선 합 34, 1~16 유일성, 빈 칸 2개
- **Command:** CLI 또는 `pytest` 단일 진입점으로 검증
- **Test Loop:** 대각선-only-fail(Red) → 정답 격자(Green)

### 제외 (표면 문제 — 하지 않음)

- 자동 채우기·솔버 앱
- GridUI / PyQt 편집기
- ECB 전 클래스 일괄 구현 (`MissingFinder`, `Solver`, …)

---

## ECB 맵 (참고)

| 구분 | 후보 | v0.1 |
|------|------|------|
| Entity | `MagicSquare`, `Cell`, `SolveResult` | 이후 |
| Control | `SquareValidator` | **우선** |
| Control | `MissingFinder`, `Solver` | 이후 |
| Boundary | `GridUI`, `InputHandler`, `ResultDisplay` | 이후 |

---

## 로드맵 (개략)

1. **v0.1** — Rule · Command · Test Loop ([PRD](docs/PRD.md))
2. **v0.2+** — `SquareValidator` ECB 정리, Entity
3. **v0.3+** — Solver, MissingFinder
4. **v1.0** — Boundary UI (별 범위)

---

## Mom Test 증거 (요약)

1. “지난주 OO 과제에서”
2. “빈칸 2개 넣고 행·열·대각선 합 맞췄는데”
3. “대각선 하나를 빼먹어서 20분 날렸다.”

---

## 라이선스 / 기여

저장소 정책이 정해지면 이 섹션을 갱신합니다.
