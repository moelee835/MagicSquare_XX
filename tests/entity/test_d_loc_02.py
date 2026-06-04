from _approval import assert_matches_golden, format_contract_output
from entity import find_blank_coords


def test_d_loc_02_blank_coords_empty_on_g0(grid_g0: list[list[int]]) -> None:
    # Given: G0 격자 (빈칸 0개)
    # When: find_blank_coords(grid_g0) 호출
    # Then: [] 반환
    result = find_blank_coords(grid_g0)
    assert result == []

    actual = format_contract_output(coords=result)
    assert_matches_golden(actual, "d_loc_02_g0_blank_coords.approved.txt")
