"""Benchmark Two Sum."""

from __future__ import annotations

import typing

import google_benchmark as benchmark

from leetcodes.lc_001_two_sum import (
    two_sum_v1,
    two_sum_v2,
    two_sum_v3,
    two_sum_v4,
)

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from google_benchmark import (
        __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
    )


def setup_data(n: int) -> tuple[list[int], int]:
    """Set up data."""
    nums = list(range(n))
    target = (n - 1) + (n - 2)
    return nums, target


def common_params[T](f: Callable[..., T] | OptionMaker.Options) -> Callable[..., T] | OptionMaker.Options:
    """Decorate common params."""
    f = benchmark.option.range(16, 4096)(f)
    return benchmark.option.complexity(benchmark.oAuto)(f)


@benchmark.register
@common_params
def bm_two_sum_v1(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums, target = setup_data(n)
    while state:
        two_sum_v1(nums, target)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_two_sum_v2(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums, target = setup_data(n)
    while state:
        two_sum_v2(nums, target)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_two_sum_v3(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums, target = setup_data(n)
    while state:
        two_sum_v3(nums, target)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_two_sum_v4(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums, target = setup_data(n)
    while state:
        two_sum_v4(nums, target)
    state.complexity_n = n
