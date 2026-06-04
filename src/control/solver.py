from entity.constants import MagicConstant
from entity.sol import solve_step_a

from control.validator import SquareValidator


class SolveError(Exception):
    """Control-layer solve failure (boundary maps to E006)."""


class Solver:
    @staticmethod
    def _apply_step_a(grid: list[list[int]], step: list[int]) -> list[list[int]]:
        filled = [list(row) for row in grid]
        for index in range(0, len(step), 3):
            row_1, col_1, value = step[index], step[index + 1], step[index + 2]
            base = MagicConstant.COORD_BASE
            row = row_1 - base
            col = col_1 - base
            filled[row][col] = value
        return filled

    @staticmethod
    def solve(grid: list[list[int]]) -> list[int]:
        try:
            step = solve_step_a(grid)
        except ValueError as exc:
            raise SolveError(str(exc)) from exc
        filled = Solver._apply_step_a(grid, step)
        if not SquareValidator.validate(filled):
            raise SolveError("no valid solution")
        return step
