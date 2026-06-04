from _approval import assert_matches_golden, format_contract_output
from control import SquareValidator


def test_d_val_01_validate_false_on_g2(grid_g2: list[list[int]]) -> None:
    # Given: G2 — Mom S2 대각선-only-fail 격자
    # When: SquareValidator.validate(grid_g2)
    # Then: False
    result = SquareValidator.validate(grid_g2)
    assert result is False

    actual = format_contract_output(validate=result)
    assert_matches_golden(actual, "d_val_01_g2_validate.approved.txt")
