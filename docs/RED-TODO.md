# MagicSquare_1004 — RED ToDo

> [README](../README.md) v0.1 · [RED 설계표](RED-Design-Tables.md) · `/tdd-red` Command  
> TDD 순서: **RED** (테스트만) → **GREEN** (최소 구현) → **REFACTOR** (동작 유지)  
> 완료 시 `- [ ]` → `- [x]`로 갱신.

---

## RED 단계 체크리스트 (v0.1 · README 기준)

> [README](../README.md) v0.1: **Rule + Command + Test Loop** · `SquareValidator`(control) 우선 · 솔버·GridUI·Boundary **제외**  
> Mom Test: “대각선 하나를 빼먹어서 20분” → 첫 RED = **대각선-only-fail** (S2)

### A. 범위 확인

| README v0.1 | RED에서 할 일 | 체크 |
|-------------|---------------|------|
| **Rule** — 10선 합 34, 1~16, 빈칸 2 | `SquareValidator` 실패 테스트 | - [ ] |
| **Command** — `pytest` 단일 진입점 | `tests/control/test_d_*.py` 추가 | - [ ] |
| **Test Loop** — 대각선-only-fail → 정답 격자 | **Red 먼저:** D-VAL-01 (G2) | - [ ] |
| 제외 — 솔버·GridUI·`MissingFinder` | RED 테스트 **작성하지 않음** | - [ ] |
| ECB — control `SquareValidator` **우선** | Layer: **control** · Track: **Logic** | - [ ] |

### B. Harness · 환경 (RED 착수 전)

- [x] `pip install -e ".[dev]"` — dev 의존성 설치 (`.venv` · STEP 7)
- [x] `pytest` 실행 — `tests/entity/` 4건 수집·passed (STEP 7~9)
- [x] `tests/control/` 디렉터리·`test_d_*.py` 명명 규칙 확인 (STEP 10 skeleton)
- [ ] 응답 선언: `Phase: red | Layer: control | Track: Logic`

### C. 픽스처 · Arrange (Logic Mock 금지)

- [x] **G2** — Mom S2: `grid_g2` (`conftest.py`) · GREEN에서 대각선-only 속성 확정
- [x] **G0** — 슬라이드 정답 (`tests/conftest.py` `grid_g0` · D-LOC-02 / D-SOL-02)
- [x] **G1** — OO 과제 빈칸 2개 (`grid_g1` · D-LOC-01 / D-SOL-01)
- [ ] 격자는 **실제 `list[list[int]]` 픽스처**만 — `SquareValidator` 스텁·Mock **금지**

### D. RED 테스트 작성 (한 턴 · 테스트 ID 하나)

| 순서 | Test ID | Given → Then | 파일 (예) | 체크 |
|------|---------|--------------|-----------|------|
| **1** | **D-VAL-01** (D-001) | G2 → `validate()` **False** | `tests/control/test_d_validator_diagonal_only_fail.py` | - [ ] |
| 2 | D-VAL-03 (D-003) | G3 → **False** + 위반 행 식별 | `tests/control/test_d_validator_row_fail.py` | - [ ] |
| 3 | D-VAL-04 (D-004) | G4 → **False** + 위반 열 식별 | `tests/control/test_d_validator_col_fail.py` | - [ ] |
| 4 | D-VAL-05 (D-005) | G0 → 10선 각각 합=34 | `tests/control/test_d_validator_ten_lines.py` | - [ ] |
| 5 | D-VAL-07 | G2 → `get_violating_lines()`에 대각선 포함 | `tests/control/test_d_validator_violating_lines.py` | - [ ] |
| 6 | D-VAL-06 (D-006) | OO G1 채움 → 재현 (Mom S1) | `tests/control/test_d_validator_oo_fixture.py` | - [ ] |

각 항목 작성 시:

- [ ] **AAA** — Arrange(픽스처) · Act(`SquareValidator`) · Assert(기대값)
- [ ] **아직 없는 동작**만 assert (기존 구현에 맞춘 약한 assert 금지)
- [ ] diff는 **`tests/`(·공유 fixture)만** — `src/` 변경 **0**

> **D-VAL-02**(정답 격자 → True)는 README Test Loop의 **Green** 시나리오 — D-VAL-01 RED·GREEN 완료 **후** Green Phase에서 진행 ([전체 ToDo](#전체-todo-red--green--refactor) 참고)

### E. RED 실행 · 실패 확인

- [ ] `pytest tests/control/ -v --tb=short` 실행
- [ ] 새 테스트 **FAILED** 확인 (`ImportError` · `ModuleNotFoundError` · `AssertionError` = 유효한 Red)
- [ ] **passed**면 Red 아님 — assert 강화 또는 이미 구현됨 → 재작성
- [ ] RED 보고: 테스트 ID · pytest 한 줄 요약 · 변경 파일 · 다음 GREEN 범위

### F. RED 금지 · README 제외 범위

- [ ] `src/` 수정 없음
- [ ] `@pytest.mark.skip` · `xfail` · assert 완화 없음
- [ ] **Track A** `U-*` (boundary, E001~E007) — v1.0까지 **RED 미착수**
- [ ] **Entity** `D-ENT-*` · **Solver** `D-MIS-*` · `D-SOL-*` — README·로드맵 **이후**
- [ ] 솔버 앱 · GridUI · ECB 전 클래스 일괄 RED **작성하지 않음**

### G. v0.1 RED 완료 기준 (Green 착수 전)

- [ ] D-VAL-01 RED: G2 → `validate()` False, pytest **FAILED**
- [ ] (선택) D-VAL-03~07 RED 테스트 추가·각각 **FAILED**
- [ ] Mom S2 연결: “대각선 빼먹음” 시나리오가 테스트로 고정됨
- [ ] → 다음: **GREEN** — D-VAL-01 최소 `SquareValidator` 구현 ([README Test Loop](../README.md#v01-범위) Green)

---

## 전체 ToDo (RED · GREEN · REFACTOR)

### 0. 사전 준비

- [x] `pip install -e ".[dev]"` — pytest Harness 확인 (`.venv`)
- [x] 공유 픽스처 정의 — **G0~G6, G1 채움, no_solution** (`tests/conftest.py`)
- [x] G2 격자 값 — `grid_g2` (G1+7·10 채움) · 대각선-only 속성은 GREEN에서 검증
- [x] `MagicConstant` SSOT (`src/entity/constants.py` · I9)

### 1. v0.1 — Track B · control · `SquareValidator`

| Test ID | ref | Phase | ToDo |
|---------|-----|-------|------|
| D-VAL-01 | D-001 | RED | - [ ] RED: G2 → `validate()` **False** (`tests/control/test_d_validator_diagonal_only_fail.py`) |
| D-VAL-01 | D-001 | GREEN | - [ ] GREEN: 10선 검증 최소 구현으로 D-VAL-01 통과 |
| D-VAL-02 | D-002 | RED | - [ ] RED: G0 → `validate()` **True** |
| D-VAL-02 | D-002 | GREEN | - [ ] GREEN: 정답 격자 통과 (Mom S3) |
| D-VAL-03 | D-003 | RED | - [ ] RED: G3 → **False** + 위반 **행** 식별 |
| D-VAL-03 | D-003 | GREEN | - [ ] GREEN: 행 위반 선 반환 |
| D-VAL-04 | D-004 | RED | - [ ] RED: G4 → **False** + 위반 **열** 식별 |
| D-VAL-04 | D-004 | GREEN | - [ ] GREEN: 열 위반 선 반환 |
| D-VAL-05 | D-005 | RED | - [ ] RED: G0 → 10선 각각 합=34 assert |
| D-VAL-05 | D-005 | GREEN | - [ ] GREEN: 10선 전수 검증 |
| D-VAL-06 | D-006 | RED | - [ ] RED: OO G1 채운 픽스처 → 재현 (Mom S1) |
| D-VAL-06 | D-006 | GREEN | - [ ] GREEN: OO 과제 조건 통과 |
| D-VAL-07 | — | RED | - [ ] RED: G2 → `get_violating_lines()`에 대각선 1개 포함 |
| D-VAL-07 | — | GREEN | - [ ] GREEN: 위반 선 목록 API |
| D-VAL-08 | D-008 | REFACTOR | - [ ] REFACTOR: `34`/`16`/`4` → `MagicConstant` SSOT (I9) |
| — | — | REFACTOR | - [ ] REFACTOR: control layer 중복 제거 · full `pytest -v` passed |

### 2. v0.2+ — Track B · entity · `MagicSquare`

- [ ] RED: D-ENT-01 — G1 → 4×4·빈칸2·1~16 (`tests/entity/test_d_magic_square.py`)
- [ ] GREEN: D-ENT-01 — `MagicSquare` 최소 구현
- [x] RED: D-LOC-01 — G1 → `find_blank_coords()` `[(2,2),(3,3)]` (I6) · STEP 6~7
- [x] GREEN: D-LOC-01 — 빈칸 좌표 탐색 · STEP 7
- [x] RED: D-LOC-02 — G0 → `find_blank_coords()` `[]` · STEP 9
- [x] GREEN: D-LOC-02 — 완성 격자 빈칸 없음 · STEP 9
- [ ] REFACTOR: entity layer · ECB import 방향 점검 (`/review-ecb`)

### 3. v0.3+ — Track B · control · `MissingFinder` · `Solver`

- [ ] RED: D-MIS-01 — G1 → `find_not_exist_nums()` `[7,10]` (I7)
- [ ] GREEN: D-MIS-01 — 누락 숫자 오름차순
- [ ] RED: D-MIS-02 — G0 → `[]`
- [ ] GREEN: D-MIS-02
- [x] RED: D-SOL-01 — G1 Step A 성공 (I8) · STEP 8
- [x] GREEN: D-SOL-01 — 솔버 Step A · STEP 8
- [x] RED: D-SOL-02 — G0 vacuous Step A + 출력 계약 (`test_d_sol_02`) · STEP 9 · G1 `[2,2,10,3,3,7]` 는 D-SOL-01·`d_sol_01_g1_*` golden
- [x] GREEN: D-SOL-02 — Golden `d_sol_02_g0_step_a.approved.txt` matched · STEP 9
- [ ] RED: D-SOL-03 — 해 없는 격자 → control 실패 (boundary E006 연계)
- [ ] GREEN: D-SOL-03
- [ ] REFACTOR: Solver · MissingFinder 경계 정리

### 4. v1.0 — Track A · boundary · UI/입출력

> **선행 조건:** v0.1 control Green 완료. E001~E007은 boundary 전담.

#### 입력 검증 (U-IN)

- [ ] RED: U-IN-01 — `grid=None` → E003 INVALID_NULL
- [ ] GREEN: U-IN-01
- [ ] RED: U-IN-02 — 3×4 → E001 INVALID_SIZE
- [ ] GREEN: U-IN-02
- [ ] RED: U-IN-03 — 빈칸 0개 (G0) → E002 INVALID_BLANKS
- [ ] GREEN: U-IN-03
- [ ] RED: U-IN-04 — 빈칸 3개 → E002 INVALID_BLANKS
- [ ] GREEN: U-IN-04
- [ ] RED: U-IN-05 — 값 17 → E004 INVALID_RANGE
- [ ] GREEN: U-IN-05
- [ ] RED: U-IN-06 — G5 중복 → E005 INVALID_DUPLICATE
- [ ] GREEN: U-IN-06
- [ ] RED: U-IN-07 — 잘못된 문자열 → E007 INVALID_FORMAT
- [ ] GREEN: U-IN-07

#### 출력 계약 (U-OUT)

- [ ] RED: U-OUT-01 — G1 solve → `len(result)==6`
- [ ] GREEN: U-OUT-01
- [ ] RED: U-OUT-02 — result 좌표 1-index (1~4)
- [ ] GREEN: U-OUT-02
- [ ] RED: U-OUT-03 — G2 validate → fail + 위반 선 표시
- [ ] GREEN: U-OUT-03

#### 흐름·ECB (U-FLOW)

- [ ] RED: U-FLOW-01 — `grid=None` → `SquareValidator` 0회 호출 (Mock)
- [ ] GREEN: U-FLOW-01
- [ ] RED: U-FLOW-02 — E001 입력 → control·entity 미전달
- [ ] GREEN: U-FLOW-02
- [ ] RED: U-FLOW-03 — G1 유효 → boundary → control 정상 위임
- [ ] GREEN: U-FLOW-03
- [ ] REFACTOR: boundary layer · E001~E007 매핑 문서화

### 5. 마일스톤

- [ ] **M1** — Mom S2: D-VAL-01 RED→GREEN (대각선-only-fail 차단)
- [ ] **M2** — Mom S3: D-VAL-02 GREEN (정답 격자 통과)
- [ ] **M3** — Mom S1: D-VAL-06 GREEN (OO 과제 재현)
- [ ] **M4** — v0.1 완료: `pytest tests/control/ -v` 전부 passed
- [x] **M5** — v0.2 entity: `pytest tests/entity/ -v` passed (4 tests · STEP 9)
- [ ] **M6** — v1.0 boundary: `pytest tests/boundary/ -v` passed
- [ ] **M7** — full suite: `pytest -v` passed + `/review-ecb` 위반 0

---

## 참고

- 설계표: [RED-Design-Tables.md](RED-Design-Tables.md)
- Logic ID: [reference.md](../.cursor/skills/magic-square-tdd/reference.md) `D-001`~`D-008` ↔ `D-VAL-*`
- Mom Test: S2→`D-VAL-01`, S3→`D-VAL-02`, S1→`D-VAL-06`
