"""2. Add Two Numbers.

URL:
    https://leetcode.com/problems/add-two-numbers
"""

from __future__ import annotations

import itertools


def add_two_numbers_v1(l1: list[int], l2: list[int]) -> list[int]:
    """Add two numbers."""
    val_out = 0
    for exp, val in enumerate(l1):
        val_out += val * 10**exp
    for exp, val in enumerate(l2):
        val_out += val * 10**exp
    out: list[int] = []
    while val_out > 0:
        out.append(val_out % 10)
        val_out = val_out // 10
    return out or [0]


def add_two_numbers_v2(l1: list[int], l2: list[int]) -> list[int]:
    """Add two numbers."""
    out: list[int] = []
    carry = 0
    i, j = 0, 0
    while i < len(l1) or j < len(l2) or carry:
        v1 = l1[i] if i < len(l1) else 0
        v2 = l2[j] if j < len(l2) else 0
        total = v1 + v2 + carry
        carry = total // 10
        out.append(total % 10)
        i += 1
        j += 1
    return out


def add_two_numbers_v3(l1: list[int], l2: list[int]) -> list[int]:
    """Add two numbers."""
    l1_len = len(l1)
    l2_len = len(l2)
    max_len = max(l1_len, l2_len)
    _l1 = [*l1, *[0] * (max_len - l1_len)]
    _l2 = [*l2, *[0] * (max_len - l2_len)]
    out: list[int] = []
    carry = 0
    for i in range(max_len):
        el = _l1[i] + _l2[i] + carry
        out.append(el % 10)
        carry = el // 10
    if carry:
        out.append(carry)
    return out


def add_two_numbers_v4(l1: list[int], l2: list[int]) -> list[int]:
    """Add two numbers."""
    out: list[int] = []
    carry = 0
    for val_1, val_2 in itertools.zip_longest(l1, l2, fillvalue=0):
        el = val_1 + val_2 + carry
        out.append(el % 10)
        carry = el // 10
    if carry:
        out.append(carry)
    return out


# dev
