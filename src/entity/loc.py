from entity.constants import MagicConstant


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return blank cell coordinates as 1-index (row, col) in row-major order."""
    blanks: list[tuple[int, int]] = []
    size = MagicConstant.GRID_SIZE
    blank = MagicConstant.BLANK_CELL
    base = MagicConstant.COORD_BASE
    for row in range(size):
        for col in range(size):
            if grid[row][col] == blank:
                blanks.append((row + base, col + base))
    return blanks
