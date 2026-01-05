"""Benchmark Add Two Numebrs."""

from __future__ import annotations

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_002_add_two_numbers

Args = tuple[list[int], list[int]]


class BenchmarkLc002AddTwoNumbers(BenchmarkBase[*Args, list[int]]):
    """BenchmarkLc002AddTwoNumbers."""

    funcs = (
        lc_002_add_two_numbers.add_two_numbers_v1,
        lc_002_add_two_numbers.add_two_numbers_v2,
        lc_002_add_two_numbers.add_two_numbers_v3,
        lc_002_add_two_numbers.add_two_numbers_v4,
    )

    @classmethod
    def _data(cls, n: int) -> Args:
        l1 = [1] * n
        l2 = [1] * n
        return l1, l2


BenchmarkLc002AddTwoNumbers.register()
