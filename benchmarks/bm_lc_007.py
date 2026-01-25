"""Benchmark Reverse Integer."""

from __future__ import annotations

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_007_reverse_integer

Args = tuple[int]


class BenchmarkLc007ReverseInteger(BenchmarkBase[*Args, int]):
    """BenchmarkLc007ReverseInteger."""

    funcs = (lc_007_reverse_integer.reverse_integer_v1, lc_007_reverse_integer.reverse_integer_v2)

    @classmethod
    def _data(cls, n: int) -> Args:
        return (n,)


BenchmarkLc007ReverseInteger.register()
