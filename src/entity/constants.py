"""Entity-layer SSOT for grid and cell domain constants (I9)."""


class MagicConstant:
    GRID_SIZE: int = 4
    BLANK_CELL: int = 0
    COORD_BASE: int = 1  # 1-index row/col (I6)
    TARGET_SUM: int = 34
    CELL_MAX: int = 16
