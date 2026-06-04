from _approval import assert_matches_golden, format_contract_output
from entity import MagicSquare
from entity.constants import MagicConstant


def test_d_ent_01_magic_square_from_g1(grid_g1: list[list[int]]) -> None:
    # Given: G1 — 4×4·빈칸 2·1~16 (I1~I3)
    # When: MagicSquare(grid_g1)
    # Then: 4×4·빈칸 2개·채워진 칸 1~16 계약
    ms = MagicSquare(grid_g1)
    size = MagicConstant.GRID_SIZE
    assert ms.row_count == size
    assert ms.col_count == size
    assert all(len(row) == size for row in ms.grid)
    assert ms.blank_count == MagicConstant.EXPECTED_BLANK_COUNT
    filled = ms.filled_values()
    lo, hi = MagicConstant.CELL_MIN, MagicConstant.CELL_MAX
    assert all(lo <= value <= hi for value in filled)
    assert len(filled) == len(set(filled))

    actual = format_contract_output(
        size=(ms.row_count, ms.col_count),
        blank_count=ms.blank_count,
        filled_count=len(filled),
    )
    assert_matches_golden(actual, "d_ent_01_g1_magic_square.approved.txt")
