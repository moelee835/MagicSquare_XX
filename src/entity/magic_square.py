from entity.constants import MagicConstant


class MagicSquare:
    """4×4 partial magic square grid (I1~I3). Boundary-valid grids only."""

    def __init__(self, grid: list[list[int]]) -> None:
        self._grid = [list(row) for row in grid]

    @property
    def grid(self) -> list[list[int]]:
        return self._grid

    @property
    def row_count(self) -> int:
        return len(self._grid)

    @property
    def col_count(self) -> int:
        size = MagicConstant.GRID_SIZE
        if not self._grid:
            return 0
        return len(self._grid[0]) if all(len(row) == len(self._grid[0]) for row in self._grid) else 0

    @property
    def blank_count(self) -> int:
        blank = MagicConstant.BLANK_CELL
        return sum(cell == blank for row in self._grid for cell in row)

    def filled_values(self) -> list[int]:
        blank = MagicConstant.BLANK_CELL
        return [cell for row in self._grid for cell in row if cell != blank]
