from _approval import assert_matches_golden, format_contract_output
from control import SquareValidator
from entity.constants import MagicConstant


def test_d_val_05_ten_lines_sum_34_on_g0(grid_g0: list[list[int]]) -> None:
    # Given: G0 — 완성 마방진
    # When: 10선(행4·열4·대각↘·↙) 각 합 검사
    # Then: 모두 MagicConstant.TARGET_SUM(34)
    target = MagicConstant.TARGET_SUM
    sums = SquareValidator.ten_line_sums(grid_g0)
    assert all(total == target for total in sums)

    actual = format_contract_output(line_sums=sums)
    assert_matches_golden(actual, "d_val_05_g0_ten_lines.approved.txt")
