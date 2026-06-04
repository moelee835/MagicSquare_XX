from _approval import assert_matches_golden, format_contract_output
from control import SquareValidator


def test_d_val_07_violating_lines_includes_diagonal(grid_g2: list[list[int]]) -> None:
    # Given: G2 — Mom S2 대각선-only-fail 격자
    # When: SquareValidator.get_violating_lines(grid_g2)
    # Then: ↙ 또는 ↘ 대각선 1개 포함
    lines = SquareValidator.get_violating_lines(grid_g2)
    assert "diag_se" in lines or "diag_sw" in lines

    actual = format_contract_output(violating_lines=lines)
    assert_matches_golden(actual, "d_val_07_g2_violating_lines.approved.txt")
