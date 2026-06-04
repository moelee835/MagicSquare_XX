import pytest

from _approval import assert_matches_golden, format_contract_output
from control import SolveError, Solver


def test_d_sol_03_solve_fails_no_solution(grid_no_solution: list[list[int]]) -> None:
    # Given: 해 없는 격자 후보
    # When: Solver.solve(grid_no_solution) / solution()
    # Then: control 실패 (boundary E006 연계)
    with pytest.raises(SolveError):
        Solver.solve(grid_no_solution)

    actual = format_contract_output(error="E006 SOLVE_FAILED")
    assert_matches_golden(actual, "d_sol_03_no_solution.approved.txt")
