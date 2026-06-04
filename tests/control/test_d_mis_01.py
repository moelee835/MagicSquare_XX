from _approval import assert_matches_golden, format_contract_output
from control import find_not_exist_nums


def test_d_mis_01_find_not_exist_nums_g1(grid_g1: list[list[int]]) -> None:
    # Given: G1 — 빈칸 2개
    # When: find_not_exist_nums(grid_g1)
    # Then: [7, 10] 오름차순 (I7)
    result = find_not_exist_nums(grid_g1)
    assert result == [7, 10]

    actual = format_contract_output(missing=result)
    assert_matches_golden(actual, "d_mis_01_g1_missing.approved.txt")
