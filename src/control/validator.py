from entity.constants import MagicConstant


class SquareValidator:
    """10-line magic square validation (I4, I5)."""

    @staticmethod
    def _line_sums(grid: list[list[int]]) -> dict[str, int]:
        size = MagicConstant.GRID_SIZE
        sums: dict[str, int] = {}
        for row in range(size):
            sums[f"row{row + MagicConstant.COORD_BASE}"] = sum(grid[row])
        for col in range(size):
            sums[f"col{col + MagicConstant.COORD_BASE}"] = sum(
                grid[row][col] for row in range(size)
            )
        sums["diag_se"] = sum(grid[i][i] for i in range(size))
        sums["diag_sw"] = sum(grid[i][size - 1 - i] for i in range(size))
        return sums

    @staticmethod
    def ten_line_sums(grid: list[list[int]]) -> list[int]:
        return list(SquareValidator._line_sums(grid).values())

    @staticmethod
    def get_violating_lines(grid: list[list[int]]) -> list[str]:
        target = MagicConstant.TARGET_SUM
        return [
            name
            for name, total in SquareValidator._line_sums(grid).items()
            if total != target
        ]

    @staticmethod
    def validate(grid: list[list[int]]) -> bool:
        return len(SquareValidator.get_violating_lines(grid)) == 0
