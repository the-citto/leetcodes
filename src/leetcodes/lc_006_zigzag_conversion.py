"""6. Zigzag Conversion.

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
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
