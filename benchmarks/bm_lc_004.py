"""Benchmark Median of Two Sorted Arrays."""

from __future__ import annotations

import random

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_004_median_of_two_sorted_arrays

Args = tuple[list[int], list[int]]


class BenchmarkLc004MedianOfTwoSortedArrays(BenchmarkBase[*Args, float]):
    """BenchmarkLc004MedianOfTwoSortedArrays."""

    funcs = (
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v1,
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v2,
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v3,
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v4,
    )

    @classmethod
    def _data(cls, n: int) -> Args:
        full_list = sorted(random.sample(range(n * 10), n))
        return full_list[::2], full_list[1::2]


BenchmarkLc004MedianOfTwoSortedArrays.register()
