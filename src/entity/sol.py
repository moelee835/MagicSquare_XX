from entity.constants import MagicConstant
from entity.loc import find_blank_coords


def _candidate_from_line(
    grid: list[list[int]],
    *,
    row: int | None = None,
    col: int | None = None,
    skip_row: int,
    skip_col: int,
) -> int:
    target = MagicConstant.TARGET_SUM
    blank = MagicConstant.BLANK_CELL
    size = MagicConstant.GRID_SIZE
    total = 0
    if row is not None:
        for c in range(size):
            if c == skip_col:
                continue
            value = grid[row][c]
            if value != blank:
                total += value
    else:
        assert col is not None
        for r in range(size):
            if r == skip_row:
                continue
            value = grid[r][col]
            if value != blank:
                total += value
    return target - total


def _candidate_at(grid: list[list[int]], row_1: int, col_1: int) -> int:
    """Infer fill value for one blank using a line with a single blank (I8)."""
    row = row_1 - MagicConstant.COORD_BASE
    col = col_1 - MagicConstant.COORD_BASE
    size = MagicConstant.GRID_SIZE
    blank = MagicConstant.BLANK_CELL

    row_blanks = sum(1 for c in range(size) if grid[row][c] == blank)
    if row_blanks == 1:
        return _candidate_from_line(grid, row=row, skip_row=row, skip_col=col)

    col_blanks = sum(1 for r in range(size) if grid[r][col] == blank)
    if col_blanks == 1:
        return _candidate_from_line(grid, col=col, skip_row=row, skip_col=col)

    raise ValueError(f"Step A cannot fix candidate at ({row_1},{col_1})")


def solve_step_a(grid: list[list[int]]) -> list[int]:
    """Step A: blank coords + candidate numbers → int[6] 1-index (I6, I8)."""
    blanks = find_blank_coords(grid)
    result: list[int] = []
    for row_1, col_1 in blanks:
        value = _candidate_at(grid, row_1, col_1)
        result.extend([row_1, col_1, value])
    return result
