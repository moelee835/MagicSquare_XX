from _approval import assert_matches_golden, format_contract_output
from control import SquareValidator


def test_d_val_06_validate_oo_g1_filled(grid_g1_oo_filled: list[list[int]]) -> None:
    # Given: G1 채움 — OO 과제 조건 재현 (Mom S1)
    # When: SquareValidator.validate(grid_g1_oo_filled)
    # Then: True (10선 규칙 통과)
    result = SquareValidator.validate(grid_g1_oo_filled)
    assert result is True

    actual = format_contract_output(validate=result)
    assert_matches_golden(actual, "d_val_06_g1_oo_validate.approved.txt")
