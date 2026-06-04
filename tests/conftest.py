import pytest


@pytest.fixture
def grid_g0() -> list[list[int]]:
    """G0 — 완성 마방진(슬라이드 정답), row-major 4×4 (설계표 RED-Design-Tables.md)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1 — OO 과제: 빈칸 0×2, row-major 4×4 (설계표 RED-Design-Tables.md)."""
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g2() -> list[list[int]]:
    """G2 — Mom S2: G0 기반 ↙(diag_sw) 합≠34 (행·열·↘는 34 유지 목표에 가깝게 1칸 교란)."""
    return [
        [16, 3, 2, 12],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g3() -> list[list[int]]:
    """G3 — G0 기반 행 1개 합≠34 (row-major 4×4)."""
    return [
        [16, 3, 2, 14],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g4() -> list[list[int]]:
    """G4 — G0 기반 열 1개 합≠34 (row-major 4×4)."""
    return [
        [15, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g5() -> list[list[int]]:
    """G5 — G0 기반 1~16 중복 (두 칸 동일 값)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 16],
    ]


@pytest.fixture
def grid_g6() -> list[list[int]]:
    """G6 — 범위 위반: 값 17 포함 (row-major 4×4)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 17],
    ]


@pytest.fixture
def grid_g1_oo_filled() -> list[list[int]]:
    """G1 채움 — OO 정답(G0 동일): Step A [2,2,10,3,3,7] → 10선 통과 (Mom S1 · D-VAL-06)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_no_solution() -> list[list[int]]:
    """해 없는 격자 후보 — D-SOL-03 (GREEN에서 유효성·E006 연계 확정)."""
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 2],
    ]
