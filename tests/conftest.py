import pytest


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1 — OO 과제: 빈칸 0×2, row-major 4×4 (설계표 RED-Design-Tables.md)."""
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]
