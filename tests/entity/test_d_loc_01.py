from _approval import assert_matches_golden, format_contract_output
from entity import find_blank_coords


def test_d_loc_01_blank_coords_row_major(grid_g1: list[list[int]]) -> None:
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    result = find_blank_coords(grid_g1)
    assert result == [(2, 2), (3, 3)]

    actual = format_contract_output(coords=result)
    assert_matches_golden(actual, "d_loc_01_g1_blank_coords.approved.txt")
