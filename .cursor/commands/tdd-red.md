# TDD RED — 실패 테스트 먼저

MagicSquare_1004 Dual-Track TDD **RED 단계만**. `.cursorrules` 및 `.cursor/skills/magic-square-tdd/SKILL.md`와 함께 적용한다.

---

## 필수 선언

응답 **첫 줄** (코드·테스트 변경 전):

```
Phase: red | Layer: entity|control|boundary | Track: Logic|UI
```

- 한 턴에 **RED 하나** · 테스트 ID(`D-*` / `U-*`) **하나**
- v0.1 Logic 우선: `Layer: control` · `Track: Logic` · `tests/control/test_d_*.py`

---

## 절차

1. **ID 확인** — `.cursor/skills/magic-square-tdd/reference.md`에서 `D-*`(Logic) 또는 `U-*`(UI) 선택. 이미 구현된 ID는 건너뛰지 말고 **다음 미작성 ID**를 고른다.
2. **기존 테스트 읽기** — `tests/{entity|control|boundary}/` 파일명·픽스처·assert 스타일을 따른다.
3. **AAA 테스트 작성** — Arrange(픽스처 격자) · Act(검증 호출) · Assert(기대 결과). Logic Track은 **실제 객체·픽스처만** — 도메인 Mock 금지.
4. **Mom Test (v0.1 Red)** — 첫 Red는 **D-001**: 대각선 1개만 합≠34 격자 → **실패** 기대 (PRD F5, S2).
5. **pytest 실행** — 아래 bash 예시로 **FAIL 확인** (`ImportError` · `AssertionError` · `ModuleNotFoundError` 모두 유효한 Red).
6. **`src/` 수정 금지** — 이번 턴 diff는 `tests/`(·공유 픽스처)만.

---

## pytest 예시 (bash)

프로젝트 루트에서:

```bash
# 최초 1회
pip install -e ".[dev]"

# RED 직후 — 해당 layer만
pytest tests/control/ -v --tb=short

# 단일 테스트 (디버깅)
pytest tests/control/test_d_validator_diagonal_only_fail.py::test_d001_diagonal_only_fail -v --tb=short

# entity layer
pytest tests/entity/ -v --tb=short

# UI Track (boundary)
pytest tests/boundary/ -v --tb=short
```

**기대:** 새 테스트 **FAILED** (또는 import 실패). `passed`면 assert가 약하거나 이미 구현됨 — Red 아님.

---

## 보고

RED 턴 마무리 시:

```markdown
## RED 보고

- **선언:** Phase: red | Layer: … | Track: …
- **테스트 ID:** D-xxx (또는 U-xxx)
- **pytest:** `…` → FAILED — (한 줄 요약: AssertionError / ImportError 등)
- **변경 파일:** tests/… 만 (src/ 없음)
- **다음:** GREEN — 대상 Layer · 테스트 ID
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` 수정 | GREEN에서 최소 구현 |
| Logic Track **Domain Mock** (`MagicSquare`, `SquareValidator` 스텁 등) | Dual-Track 규칙 |
| assert 완화 · `@pytest.mark.skip` · `xfail` | 가짜 Green |
| GREEN/REFACTOR 코드·다음 Phase 테스트 동시 작성 | Phase 하나씩 |
| E001~E007 Logic 테스트 | boundary 전담 |
| PRD 비목표 (솔버 · GridUI 일괄) | v0.1 범위 밖 |
