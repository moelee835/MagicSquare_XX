from _approval import assert_matches_golden, format_contract_output
from entity import solve_step_a


def test_d_sol_02_step_a_success(grid_g0: list[list[int]]) -> None:
    # Given: G0 (빈칸 0개 — 완성 격자)
    # When: solve_step_a — Step A (빈칸 없음)
    # Then: vacuous int[6] contract → [] · golden 고정
    result = solve_step_a(grid_g0)
    assert result == []

    actual = format_contract_output(int6=result)
    assert_matches_golden(actual, "d_sol_02_g0_step_a.approved.txt")
