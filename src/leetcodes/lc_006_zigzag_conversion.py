"""6. Zigzag Conversion.

URL:
    https://leetcode.com/problems/zigzag-conversion
"""

from __future__ import annotations


def zigzag_conversion_v1(s: str, num_rows: int) -> str:
    """Zigzag Conversion."""
    if num_rows == 1:
        return s
    grid: list[str] = [""] * num_rows
    row = 0
    direction = -1
    for char in s:
        grid[row] += char
        if row == 0 or row == num_rows - 1:
            direction = -direction
        row += direction
    return "".join(grid)


def zigzag_conversion_v2(s: str, num_rows: int) -> str:
    """Zigzag Conversion."""
    if num_rows == 1:
        return s
    grid: list[list[str]] = [[] for _ in range(num_rows)]
    row = 0
    direction = -1
    for char in s:
        grid[row].append(char)
        if row == 0 or row == num_rows - 1:
            direction = -direction
        row += direction
    return "".join(["".join(g) for g in grid])
