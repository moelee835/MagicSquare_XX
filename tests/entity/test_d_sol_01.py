from _approval import assert_matches_golden, format_contract_output
from entity import solve_step_a


def test_d_sol_01_step_a_success(grid_g1: list[list[int]]) -> None:
    # Given: G1 (빈칸 2개)
    # When: solve_step_a — Step A 좌표·후보 확정 (I8)
    # Then: int[6] 1-index [2,2,10,3,3,7]
    result = solve_step_a(grid_g1)
    assert result == [2, 2, 10, 3, 3, 7]
    assert len(result) == 6

    actual = format_contract_output(int6=result)
    assert_matches_golden(actual, "d_sol_01_g1_step_a.approved.txt")
