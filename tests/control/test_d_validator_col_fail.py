from _approval import assert_matches_golden, format_contract_output
from control import SquareValidator


def test_d_val_04_validate_false_col_violation(grid_g4: list[list[int]]) -> None:
    # Given: G4 — 열 1개 합≠34
    # When: SquareValidator.validate(grid_g4)
    # Then: False + 위반 열 선 식별
    result = SquareValidator.validate(grid_g4)
    lines = SquareValidator.get_violating_lines(grid_g4)
    assert result is False
    assert "col1" in lines

    actual = format_contract_output(validate=result, violating_lines=lines)
    assert_matches_golden(actual, "d_val_04_g4_col_violation.approved.txt")
