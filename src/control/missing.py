from entity.constants import MagicConstant


def find_not_exist_nums(grid: list[list[int]]) -> list[int]:
    """Return missing values from 1..16 not present in filled cells (I7)."""
    blank = MagicConstant.BLANK_CELL
    lo, hi = MagicConstant.CELL_MIN, MagicConstant.CELL_MAX
    present = {cell for row in grid for cell in row if cell != blank}
    return [value for value in range(lo, hi + 1) if value not in present]
