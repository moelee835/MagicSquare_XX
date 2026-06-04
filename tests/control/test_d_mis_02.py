from _approval import assert_matches_golden, format_contract_output
from control import find_not_exist_nums


def test_d_mis_02_find_not_exist_nums_empty_g0(grid_g0: list[list[int]]) -> None:
    # Given: G0 — 완성 격자
    # When: find_not_exist_nums(grid_g0)
    # Then: []
    result = find_not_exist_nums(grid_g0)
    assert result == []

    actual = format_contract_output(missing=result)
    assert_matches_golden(actual, "d_mis_02_g0_missing.approved.txt")
