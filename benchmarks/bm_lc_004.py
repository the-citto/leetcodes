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


# from __future__ import annotations
#
# import random
# import typing
#
# import google_benchmark as benchmark
#
# from leetcodes.lc_004_median_of_two_sorted_arrays import (
#     median_of_two_sorted_arrays_v1,
#     median_of_two_sorted_arrays_v2,
#     median_of_two_sorted_arrays_v3,
#     median_of_two_sorted_arrays_v4,
# )
#
# if typing.TYPE_CHECKING:
#     from collections.abc import Callable
#
#     from google_benchmark import (
#         __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
#     )
#
#
# def setup_data(n: int) -> tuple[list[int], list[int]]:
#     """Set up data."""
#     full_list = sorted(random.sample(range(n * 10), n))
#     return full_list[::2], full_list[1::2]
#
#
# def common_params[T](f: Callable[..., T] | OptionMaker.Options) -> Callable[..., T] | OptionMaker.Options:
#     """Decorate common params."""
#     f = benchmark.option.range(1 << 4, 1 << 11)(f)
#     return benchmark.option.complexity(benchmark.oAuto)(f)
#
#
# # @benchmark.register
# @common_params
# def bm_lc_004_v1(state: benchmark.State) -> None:
#     """Benchmark Two Sum."""
#     n = state.range(0)
#     nums1, nums2 = setup_data(n)
#     while state:
#         median_of_two_sorted_arrays_v1(nums1, nums2)
#     state.complexity_n = n
#
#
# # @benchmark.register
# @common_params
# def bm_lc_004_v2(state: benchmark.State) -> None:
#     """Benchmark Two Sum."""
#     n = state.range(0)
#     nums1, nums2 = setup_data(n)
#     while state:
#         median_of_two_sorted_arrays_v2(nums1, nums2)
#     state.complexity_n = n
#
#
# # @benchmark.register
# @common_params
# def bm_lc_004_v3(state: benchmark.State) -> None:
#     """Benchmark Two Sum."""
#     n = state.range(0)
#     nums1, nums2 = setup_data(n)
#     while state:
#         median_of_two_sorted_arrays_v3(nums1, nums2)
#     state.complexity_n = n
#
#
# @benchmark.register
# @common_params
# def bm_lc_004_v4(state: benchmark.State) -> None:
#     """Benchmark Two Sum."""
#     n = state.range(0)
#     nums1, nums2 = setup_data(n)
#     while state:
#         median_of_two_sorted_arrays_v4(nums1, nums2)
#     state.complexity_n = n
