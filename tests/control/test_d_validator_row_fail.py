from _approval import assert_matches_golden, format_contract_output
from control import SquareValidator


def test_d_val_03_validate_false_row_violation(grid_g3: list[list[int]]) -> None:
    # Given: G3 — 행 1개 합≠34
    # When: SquareValidator.validate(grid_g3)
    # Then: False + 위반 행 선 식별
    result = SquareValidator.validate(grid_g3)
    lines = SquareValidator.get_violating_lines(grid_g3)
    assert result is False
    assert "row1" in lines

    actual = format_contract_output(validate=result, violating_lines=lines)
    assert_matches_golden(actual, "d_val_03_g3_row_violation.approved.txt")
