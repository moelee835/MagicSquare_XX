# MagicSquare_XX

4×4 **마방진(Magic Square)** 학습·설계 프로젝트. Mom Test로 문제를 검증한 뒤, **10개 선(행4·열4·대각2) 합 34** 검증에 우선 범위를 둡니다.

| 항목 | 내용 |
|------|------|
| 워크북 ID | MagicSquare_1004 |
| 현재 단계 | STEP 10 — entity·control GREEN · Golden 15 baseline |
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
│   ├── PRD.md
│   ├── RED-Design-Tables.md
│   └── RED-TODO.md
├── src/entity/          # find_blank_coords, solve_step_a, MagicConstant
├── tests/entity/        # test_d_loc_*, test_d_sol_*
├── tests/golden/        # Golden Master baseline
├── Report/              # STEP 1~9 보고서
└── Prompting/           # 세션 Export
```

| 폴더 | 용도 |
|------|------|
| `docs/` | PRD, RED 설계표·ToDo |
| `src/entity/` | `find_blank_coords`, `solve_step_a`, `MagicConstant` |
| `tests/entity/` | Logic Track `D-LOC-*`, `D-SOL-*` |
| `tests/golden/` | Golden Master (`UPDATE_GOLDEN=1` 로만 baseline 갱신) |
| `Report/` | Mom Test, TDD STEP 보고서 |
| `Prompting/` | Cursor 대화 Export |

> `tests/control/` — v0.1 `SquareValidator` (**미착수**).

---

## 개발 환경 (가상환경)

프로젝트 루트에서 **`.venv`** 를 만들고, 그 안의 Python으로만 설치·테스트합니다.

### Windows (권장 — 실행 정책 오류 없음)

PowerShell 기본 정책이 **Restricted**이면 `Activate.ps1`·`setup.ps1`에서 **보안 오류(PSSecurityException)** 가 납니다. **`.cmd` / venv `python.exe` 직접 호출**을 쓰세요.

```powershell
cd MagicSquare_XX
.\scripts\setup.cmd
.\.venv\Scripts\python.exe -m pytest tests/entity/ -v
```

활성화가 필요하면 **CMD**에서: `.venv\Scripts\activate.bat` (`.ps1` 아님).

### Windows (PowerShell `.ps1` — 정책 허용 시만)

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned   # 관리자 불필요, 1회
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
python -m pytest tests/entity/ -v
```

> `Set-ExecutionPolicy RemoteSigned`만 쓰면 **LocalMachine** 변경 시도로 거부될 수 있습니다. 반드시 **`-Scope CurrentUser`** 를 붙이세요.

### macOS / Linux

```bash
cd MagicSquare_XX
chmod +x scripts/setup.sh
./scripts/setup.sh
source .venv/bin/activate
python -m pytest tests/entity/ -v
```

| 단계 | 설명 |
|------|------|
| `scripts/setup.cmd` (Win) / `setup.sh` | `.venv` 생성 + `pip install -e ".[dev]"` — **정책 무관** |
| `scripts/setup.ps1` | PowerShell 전용 (실행 정책 필요) |
| pytest (Win, 정책 제한 시) | `.\.venv\Scripts\python.exe -m pytest …` — **Activate.ps1 불필요** |
| npm/npx 보안 오류 | Node 설치의 `npm.ps1`도 동일 원인 — `npm.cmd -v` 사용 또는 위 CurrentUser 정책 |

Cursor/VS Code: 인터프리터 **`.venv\Scripts\python.exe`**. 터미널은 `Activate.ps1` 대신 venv Python 경로를 씁니다 (`python.terminal.activateEnvironment`: false).

---

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | v0.1 범위, 기능·도메인 요구사항, 성공 기준(AC) |
| [docs/RED-TODO.md](docs/RED-TODO.md) | RED/GREEN/REFACTOR 체크리스트 (완료 시 `[x]`) |
| [docs/RED-Design-Tables.md](docs/RED-Design-Tables.md) | Dual-Track RED 설계표·픽스처 G0~G6 |
| [Report/10.MagicSquare_1004-Entity-Control-Golden-보고서.md](Report/10.MagicSquare_1004-Entity-Control-Golden-보고서.md) | STEP 10 entity·control GREEN · Golden 15 |
| [Report/09.MagicSquare_1004-D-LOC-02-D-SOL-02-Golden-보고서.md](Report/09.MagicSquare_1004-D-LOC-02-D-SOL-02-Golden-보고서.md) | STEP 9 D-LOC-02 · D-SOL-02 Golden |
| [Report/08.MagicSquare_1004-GREEN-D-SOL-01-Golden-보고서.md](Report/08.MagicSquare_1004-GREEN-D-SOL-01-Golden-보고서.md) | STEP 8 D-SOL-01 Golden |
| [Report/07.MagicSquare_1004-GREEN-D-LOC-01-Venv-보고서.md](Report/07.MagicSquare_1004-GREEN-D-LOC-01-Venv-보고서.md) | STEP 7 D-LOC-01 · `.venv` |
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test + R-G-I-O + 8계층 |

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

## TDD 진행 체크리스트

상세 ToDo: [docs/RED-TODO.md](docs/RED-TODO.md)

| Test ID | Phase | 상태 | 비고 |
|---------|-------|------|------|
| D-LOC-01 | RED→GREEN | [x] | G1 → `[(2,2),(3,3)]` · STEP 7 |
| D-LOC-02 | RED→GREEN | [x] | G0 → `[]` · STEP 9 |
| D-SOL-01 | RED→GREEN | [x] | G1 Step A · golden `d_sol_01_g1_*` · STEP 8 |
| D-SOL-02 | RED→GREEN | [x] | G0 vacuous · golden `d_sol_02_g0_*` · STEP 9 |
| D-VAL-01~07 | RED→GREEN | [x] | `SquareValidator` · STEP 10 |
| D-MIS-01~02 | RED→GREEN | [x] | `find_not_exist_nums` · STEP 10 |
| D-SOL-03 | RED→GREEN | [x] | `SolveError` · STEP 10 |
| D-ENT-01 | RED→GREEN | [x] | `MagicSquare` · golden · STEP 10 |
| D-LOC-01/02 | Golden | [x] | `d_loc_*` baseline · STEP 10 |

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v   # 15 passed · Golden matched
```

---

## ECB 맵 (참고)

| 구분 | 후보 | 상태 |
|------|------|------|
| Entity | `find_blank_coords`, `solve_step_a`, `MagicSquare` | **GREEN** + Golden (STEP 7~10) |
| Control | `SquareValidator`, `MissingFinder`, `Solver` | **GREEN** + Golden (STEP 10) |
| Boundary | `GridUI`, E001~E007 | v1.0 |

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
