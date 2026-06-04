# ECB · 계약 리뷰 (코드 수정 금지)

MagicSquare_1004 **ECB·도메인 계약** 위반만 검사한다. **파일 수정·리팩터·테스트 추가 금지** — 읽기·grep·분석만.

`.cursorrules`, `docs/PRD.md`가 계약의 SSOT.

---

## 필수 선언

응답 **첫 줄**:

```
Mode: review-ecb | Scope: src/ tests/ (또는 사용자 지정 경로)
```

---

## 절차

1. **범위 읽기** — `src/entity/`, `src/control/`, `src/boundary/`, `tests/entity/`, `tests/control/`, `tests/boundary/` (또는 사용자가 지정한 diff·경로).
2. **5항목 스캔** — 아래 체크리스트 각각 grep·import·리터럴·Mock 사용 여부 확인.
3. **위반만 표로 출력** — 위반 **0건**이면 `위반 없음` 한 줄 + 스캔 범위만 보고.
4. **수정 제안 금지** — 코드 블록으로 패치·diff 제시하지 않는다. (사용자가 별도 요청할 때만)

---

## 체크리스트 (계약)

| # | 항목 | 계약 | 스캔 방법 |
|---|------|------|-----------|
| 1 | **import 방향** | `boundary → control → entity`만. **역방향 import 금지**. `entity`는 `control`·`boundary` import **금지** | `src/**` import 문; entity가 상위 계층 참조 여부 |
| 2 | **entity E001~E005** | E001~E007 **boundary 전담**. entity는 E001~E005 **처리·발생·변환 금지** (입력 형식·크기·빈칸 수·범위·중복) | `src/entity/`, `tests/entity/`에서 E001~E005·동등 검증 로직 |
| 3 | **int[6] 1-index** | 솔버/채움 성공 출력 `[r1,c1,n1,r2,c2,n2]`, 행·열 **1~4 (1-index)** | 반환·assert·문서화된 API에서 0-index 좌표·길이≠6 |
| 4 | **MagicConstant SSOT** | **34**, **16**, 격자 **4**는 `MagicConstant`(동등 SSOT)에서만. **리터럴 산재 금지** | `src/`, `tests/`에서 `34`·`16`·`4` 리터럴 (테스트 픽스처 격자 값 제외 — **도메인 상수**만) |
| 5 | **Logic Track Domain Mock** | `tests/entity/`, `tests/control/`(`test_d_*`)에서 `MagicSquare`·`SquareValidator` 등 **도메인 Mock/스텁 금지** | `unittest.mock`, `MagicMock`, `@patch`, 수동 스텁 클래스 |

**MagicConstant SSOT 예외 (위반 아님):** 테스트 픽스처 격자 셀 값(1~16), 좌표 assert의 1~4, `MagicConstant` 정의 파일 내부 리터럴.

---

## 보고 형식 (위반만)

위반이 **있을 때만** 아래 표를 채운다. 항목별 위반 0건이면 **그 표 생략**.

### import 방향

| 파일 | 줄(또는 심볼) | 위반 내용 |
|------|---------------|-----------|
| … | … | … |

### entity E001~E005

| 파일 | 줄(또는 심볼) | 위반 내용 |
|------|---------------|-----------|
| … | … | … |

### int[6] 1-index

| 파일 | 줄(또는 심볼) | 위반 내용 |
|------|---------------|-----------|
| … | … | … |

### MagicConstant SSOT

| 파일 | 줄(또는 심볼) | 위반 내용 |
|------|---------------|-----------|
| … | … | … |

### Logic Track Domain Mock

| 파일 | 줄(또는 심볼) | 위반 내용 |
|------|---------------|-----------|
| … | … | … |

### 요약

| 항목 | 위반 건수 |
|------|-----------|
| import 방향 | N |
| entity E001~E005 | N |
| int[6] 1-index | N |
| MagicConstant SSOT | N |
| Logic Track Domain Mock | N |

---

## 금지

| 금지 | 이유 |
|------|------|
| **코드·테스트 수정** | review 전용 Command |
| 스타일·네이밍·성능 등 계약 외 리뷰 | 범위 밖 |
| 위반 없을 때 장문 칭찬·개선 아이디어 | 위반만 보고 |
| git commit | 사용자 요청 시에만 |
