"""Golden master approval helpers — fixed contract text format."""

from __future__ import annotations

import difflib
import os
from pathlib import Path

_GOLDEN_ROOT = Path(__file__).resolve().parent / "golden"


def format_contract_output(
    *,
    int6: list[int] | tuple[int, ...] | None = None,
    error: str | None = None,
) -> str:
    """Serialize solver/boundary output for golden comparison.

    Fixed line-oriented format (UTF-8, LF, trailing newline):
    - ``int6: r1,c1,n1,r2,c2,n2`` — six comma-separated ints (1-index coords)
    - ``error: NONE`` on success, or ``error: E00x CODE_NAME`` on failure
    """
    lines: list[str] = []
    if int6 is not None:
        values = list(int6)
        if len(values) != 6:
            raise ValueError(f"int6 must have length 6, got {len(values)}")
        lines.append("int6: " + ",".join(str(v) for v in values))
    if error is None and int6 is not None:
        lines.append("error: NONE")
    elif error is not None:
        lines.append(f"error: {error}")
    return "\n".join(lines) + "\n"


def assert_matches_golden(actual: str, relative: str) -> None:
    """Compare *actual* text to ``tests/golden/{relative}``.

    When ``UPDATE_GOLDEN=1`` is set in the environment, write *actual* to the
    golden file instead of asserting (baseline refresh — not manual edit).
    """
    golden_path = _GOLDEN_ROOT / relative
    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual, encoding="utf-8", newline="\n")
        return

    if not golden_path.is_file():
        raise AssertionError(
            f"Golden file missing: {golden_path}\n"
            "Set UPDATE_GOLDEN=1 and re-run pytest to generate the baseline."
        )

    expected = golden_path.read_text(encoding="utf-8")
    if actual != expected:
        diff = "".join(
            difflib.unified_diff(
                expected.splitlines(keepends=True),
                actual.splitlines(keepends=True),
                fromfile=f"golden/{relative}",
                tofile="actual",
            )
        )
        raise AssertionError(f"Golden mismatch for {relative}\n{diff}")
