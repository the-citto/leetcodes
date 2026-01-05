"""Benchmark Two Sum."""

from __future__ import annotations

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_001_two_sum

Args = tuple[list[int], int]


class BenchmarkLc001TwoSum(BenchmarkBase[*Args, list[int]]):
    """BenchmarkLc001TwoSum."""

    funcs = (
        lc_001_two_sum.two_sum_v1,
        lc_001_two_sum.two_sum_v2,
        lc_001_two_sum.two_sum_v3,
        lc_001_two_sum.two_sum_v4,
    )

    @classmethod
    def _data(cls, n: int) -> Args:
        nums = list(range(n))
        target = (n - 1) + (n - 2)
        return nums, target


BenchmarkLc001TwoSum.register()
