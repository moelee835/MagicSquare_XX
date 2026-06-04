"""Golden master approval helpers — fixed contract text format."""

from __future__ import annotations

import difflib
import os
from pathlib import Path

_GOLDEN_ROOT = Path(__file__).resolve().parent / "golden"


def format_contract_output(
    *,
    int6: list[int] | tuple[int, ...] | None = None,
    coords: list[tuple[int, int]] | None = None,
    size: tuple[int, int] | None = None,
    blank_count: int | None = None,
    filled_count: int | None = None,
    validate: bool | None = None,
    violating_lines: list[str] | None = None,
    missing: list[int] | None = None,
    line_sums: list[int] | None = None,
    error: str | None = None,
) -> str:
    """Serialize solver/boundary output for golden comparison.

    Fixed line-oriented format (UTF-8, LF, trailing newline):
    - ``int6: r1,c1,n1,r2,c2,n2`` — six comma-separated ints (1-index)
    - ``coords: r1,c1,r2,c2,...`` — blank cell coords (1-index, row-major)
    - ``size: rows,cols`` · ``blank_count: N`` · ``filled_count: N`` — entity contract
    - ``validate: true|false`` · ``violating_lines: name,...`` — control validator
    - ``missing: n1,n2,...`` · ``line_sums: s1,s2,...`` — control finder / 10선
    - ``error: NONE`` on success, or ``error: E00x CODE_NAME`` on failure
    """
    lines: list[str] = []
    if int6 is not None:
        values = list(int6)
        if len(values) == 0:
            lines.append("int6:")
        elif len(values) != 6:
            raise ValueError(f"int6 must have length 6, got {len(values)}")
        else:
            lines.append("int6: " + ",".join(str(v) for v in values))
    if coords is not None:
        if len(coords) == 0:
            lines.append("coords:")
        else:
            flat = [str(v) for pair in coords for v in pair]
            lines.append("coords: " + ",".join(flat))
    if size is not None:
        lines.append(f"size: {size[0]},{size[1]}")
    if blank_count is not None:
        lines.append(f"blank_count: {blank_count}")
    if filled_count is not None:
        lines.append(f"filled_count: {filled_count}")
    if validate is not None:
        lines.append(f"validate: {'true' if validate else 'false'}")
    if violating_lines is not None:
        names = sorted(violating_lines)
        if len(names) == 0:
            lines.append("violating_lines:")
        else:
            lines.append("violating_lines: " + ",".join(names))
    if missing is not None:
        if len(missing) == 0:
            lines.append("missing:")
        else:
            lines.append("missing: " + ",".join(str(v) for v in missing))
    if line_sums is not None:
        lines.append("line_sums: " + ",".join(str(v) for v in line_sums))
    has_payload = any(
        x is not None
        for x in (
            int6,
            coords,
            size,
            blank_count,
            filled_count,
            validate,
            violating_lines,
            missing,
            line_sums,
        )
    )
    if error is not None:
        lines.append(f"error: {error}")
    elif has_payload:
        lines.append("error: NONE")
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
