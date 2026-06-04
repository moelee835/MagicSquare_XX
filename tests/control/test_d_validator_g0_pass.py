from _approval import assert_matches_golden, format_contract_output
from control import SquareValidator


def test_d_val_02_validate_true_on_g0(grid_g0: list[list[int]]) -> None:
    # Given: G0 — 슬라이드 정답 격자
    # When: SquareValidator.validate(grid_g0)
    # Then: True (Mom S3 · GREEN 시나리오)
    result = SquareValidator.validate(grid_g0)
    assert result is True

    actual = format_contract_output(validate=result)
    assert_matches_golden(actual, "d_val_02_g0_validate.approved.txt")
