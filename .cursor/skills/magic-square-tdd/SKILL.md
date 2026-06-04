---
name: magic-square-tdd
description: MagicSquare_1004 Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. TDD, RED/GREEN/REFACTOR, SquareValidator, Logic/UI 트랙, pytest, ECB 계층 작업 시 사용.
---

# MagicSquare_1004 — Dual-Track TDD·ECB

프로젝트 루트 [`.cursorrules`](../../../.cursorrules), [`docs/PRD.md`](../../../docs/PRD.md)와 함께 적용한다.

## 언제 이 Skill을 켜는지

다음 **하나라도** 해당하면 이 Skill을 읽고 따른다.

| 트리거 | 예시 |
|--------|------|
| TDD Phase 작업 | Red/Green/Refactor, 실패 테스트 먼저, 최소 구현 |
| Logic·UI 트랙 | `test_d_*` / `test_u_*`, entity/control/boundary 테스트 |
| ECB 구현 | `src/entity`, `src/control`, `src/boundary` 코드·테스트 추가 |
| v0.1 핵심 | `SquareValidator`, 10선·34, Mom Test 픽스처 |
| pytest 루프 | 어떤 테스트를 언제 돌릴지 확인할 때 |

**켜지 않을 때:** 문서만 수정, README/보고서 작성, git commit(사용자 요청 시), PRD 비목표(솔버·GridUI 일괄 구현) 제안.

---

## 매 턴 선언 (필수)

코드·테스트 변경 **전** 응답 맨 앞에 한 줄:

```
Phase: RED|GREEN|REFACTOR · Layer: entity|control|boundary · Track: Logic|UI
```

한 턴에 **Phase 하나**만. Layer·Track이 섞이면 범위를 나눠 순차 진행한다.

---

## Logic Track vs UI Track

| | **Logic Track** | **UI Track** |
|--|-----------------|--------------|
| **대상 계층** | entity, control | boundary |
| **테스트 ID** | `D-*` | `U-*` |
| **파일명** | `test_d_*.py` | `test_u_*.py` |
| **디렉터리** | `tests/entity/`, `tests/control/` | `tests/boundary/` |
| **Mock** | **도메인 Mock 금지** — 실제 객체·픽스처만 | **Mock 허용** — control/entity 스텁 가능 |
| **v0.1 우선** | `tests/control/` — `SquareValidator` | 이후 (boundary 미착수 시 UI Phase 금지) |

---

## ECB · Mock · E001~E007

### ECB 의존 방향

```
boundary → control → entity
```

| 계층 | 역할 | import 규칙 |
|------|------|-------------|
| entity | `MagicSquare`, `Cell`, 도메인 규칙·상태 | **control·boundary import 금지** |
| control | `SquareValidator`, `MissingFinder`, `Solver` | entity만 호출 |
| boundary | CLI/UI, E001~E007, 입출력 변환 | control 호출 |

**역방향 import 금지.** 숫자 **34**, **16**, 격자 **4**는 `MagicConstant`(SSOT)에서만 — 리터럴 산재 금지.

### Mock 정책

| 위치 | 허용 | 금지 |
|------|------|------|
| Logic (`tests/entity/`, `tests/control/`) | 실제 domain 객체, PRD 픽스처 | `MagicSquare`·`SquareValidator` 등 **도메인 Mock/스텁** |
| UI (`tests/boundary/`) | control/entity Mock·스텁 | boundary가 entity를 **직접** 우회 호출 |

### E001~E007

| 코드 | 처리 계층 | entity/control |
|------|-----------|----------------|
| E001~E007 | **boundary 전담** — 발생·변환·표시 | Logic 테스트·구현에서 **발생·처리 금지** |
| E001~E005 | 입력 형식·크기·빈칸 수·범위·중복 사전 검증 | entity **E001~E005 처리 금지** |
| 유효 격자 | boundary 통과 후 | control·entity만 수신 |

boundary 실패 시 control·entity로 **내려보내지 않는다.**

### TDD 금지 (모든 Phase)

- assert 완화, `@pytest.mark.skip`, `xfail`
- “일단 통과” 더미 구현
- Phase 건너뛰기 (Red 없이 Green, Green 없이 Refactor)
- PRD 비목표 범위 일괄 구현

---

## RED — 5~7단계

1. **범위 고정** — 이번 턴 Layer·Track·테스트 ID(`D-*`/`U-*`) 하나만. [reference.md](reference.md)에서 ID 확인.
2. **기존 코드 읽기** — 해당 계층 `src/`, `tests/` 파일·컨벤션 확인.
3. **Mom Test 연결** — v0.1 Red = **대각선-only-fail** 격자 (PRD F5, S2).
4. **실패 테스트 작성** — `test_d_*.py` 또는 `test_u_*.py`에 **아직 없는** 동작만 assert. Logic은 Mock 없이 픽스처.
5. **pytest 실행** — 아래 [Test/Review Loop](#testreview-loop) “RED 직후” 명령. **실패 확인** (ImportError·AssertionError OK).
6. **구현 코드 작성 금지** — Red 턴에는 테스트(·픽스처)만 diff.
7. **Red 보고** — 실패 메시지·대상 테스트 ID·다음 Green 범위를 한 줄로 명시.

---

## GREEN — 5~7단계

1. **Red 테스트 목록 확인** — 방금 실패한 테스트만 Green 대상. 범위 밖 파일 수정 금지.
2. **최소 구현** — Red를 통과시키는 **가장 작은** 코드만 `src/{layer}/`에 추가.
3. **Mom Test Green** — 슬라이드/과제 **정답 격자** 통과 테스트 포함 (PRD F6, T2).
4. **SSOT·ECB 준수** — `MagicConstant` 사용, 역방향 import·entity E001~E005 처리 없음.
5. **pytest 실행** — “GREEN 직후” 명령. **전부 passed** 확인.
6. **테스트 추가 금지** — Green 턴에 새 Red 테스트 넣지 않음.
7. **Green 보고** — passed 개수·구현 파일·Refactor 후보(중복·상수·이름)만 간단히.

---

## REFACTOR — 5~7단계

1. **Green 상태 확인** — Refactor 시작 전 full suite **passed** (아래 Loop “REFACTOR 전”).
2. **동작 불변** — 테스트 assert·공개 API 시그니처 변경 금지 (내부 구조만).
3. **허용 Refactor** — 중복 제거, `MagicConstant` 정리, private 헬퍼 추출, ECB 경계 명확화.
4. **금지 Refactor** — 새 기능, boundary/UI 선행, Entity 분리 일괄(v0.2 전제) — **한 Refactor 턴에 한 종류**.
5. **테스트 코드 정리** — 픽스처 공통화·이름 정리 (동작 동일).
6. **pytest 실행** — “REFACTOR 직후” + 필요 시 full suite. **여전히 passed**.
7. **Refactor 보고** — 변경 요약·다음 Phase(Red 또는 다음 Layer) 제안.

---

## Test/Review Loop

작업 디렉터리: 프로젝트 루트. 최초 1회: `pip install -e ".[dev]"`.

| 시점 | 명령 | 기대 |
|------|------|------|
| **RED 직후** | `pytest tests/{layer}/ -v --tb=short` | 새 테스트 **FAILED** (0 tests collected면 경로·파일명 점검) |
| **GREEN 직후** | `pytest tests/{layer}/ -v` | 해당 layer **passed** |
| **REFACTOR 전** | `pytest -v` | **전체 passed** (Harness만: 0건·exit 5 = 테스트 미작성) |
| **REFACTOR 직후** | `pytest -v` | **전체 passed** |
| **Phase 완료·리뷰** | `pytest -v --tb=short` | 회귀 없음; 실패 시 **해당 Phase로 롤백** |
| **Logic만 스모크** | `pytest tests/control/ tests/entity/ -v` | UI 미착수 시 |
| **단일 테스트** | `pytest tests/control/test_d_xxx.py::test_name -v` | 한 ID 디버깅 |

**Review Loop 규칙**

- Red → Green → Refactor **순서 고정**. failed 상태에서 Refactor 시작 금지.
- layer 작업 중에는 **해당 layer pytest**로 빠르게 돌리고, Refactor·완료 보고 전 **full `pytest -v`**.
- exit code **5** (no tests collected): 테스트 파일 미작성 — Red 4단계로 복귀.

---

## 완료 보고 항목

Phase 또는 Layer 단위 작업을 마칠 때 아래를 포함한다.

```markdown
## TDD 완료 보고

- **Phase / Layer / Track:** …
- **테스트 ID:** D-xxx (또는 U-xxx)
- **pytest:** `…` → N passed / 실패 시 메시지
- **변경 파일:** tests/…, src/…
- **Mom Test:** S1|S2|S3 연결 (해당 시)
- **ECB 점검:** 역방향 import 없음 · MagicConstant SSOT · E001~E007 boundary 전담
- **Mock 점검:** Logic Mock 없음 / UI Mock 사용 시 대상 명시
- **다음 Phase:** RED|GREEN|REFACTOR · 대상 Layer · 테스트 ID
```

git commit은 **사용자 요청 시에만**.

---

## 참고

- D-* 테스트 ID 목록: [reference.md](reference.md)
- Command 파일(`.cursor/commands/`): **아직 없음** — 본 Skill만 따른다.
