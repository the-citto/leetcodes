"""Benchmark Add Two Numebrs."""

from __future__ import annotations

import typing

import google_benchmark as benchmark

from leetcodes.lc_002_add_two_numbers import (
    add_two_numbers_v1,
    add_two_numbers_v2,
    add_two_numbers_v3,
    add_two_numbers_v4,
)

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from google_benchmark import (
        __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
    )


def setup_data(n: int) -> tuple[list[int], list[int]]:
    """Set up data."""
    l1 = [1] * n
    l2 = [1] * n
    return l1, l2


def common_params[T](f: Callable[..., T] | OptionMaker.Options) -> Callable[..., T] | OptionMaker.Options:
    """Decorate common params."""
    f = benchmark.option.range(16, 4096)(f)
    return benchmark.option.complexity(benchmark.oAuto)(f)


@benchmark.register
@common_params
def bc_add_two_numbers_v1(state: benchmark.State) -> None:
    """Benchmark Add Two Numebrs."""
    n = state.range(0)
    l1, l2 = setup_data(n)
    while state:
        add_two_numbers_v1(l1, l2)
    state.complexity_n = n


@benchmark.register
@common_params
def bc_add_two_numbers_v2(state: benchmark.State) -> None:
    """Benchmark Add Two Numebrs."""
    n = state.range(0)
    l1, l2 = setup_data(n)
    while state:
        add_two_numbers_v2(l1, l2)
    state.complexity_n = n


@benchmark.register
@common_params
def bc_add_two_numbers_v3(state: benchmark.State) -> None:
    """Benchmark Add Two Numebrs."""
    n = state.range(0)
    l1, l2 = setup_data(n)
    while state:
        add_two_numbers_v3(l1, l2)
    state.complexity_n = n


@benchmark.register
@common_params
def bc_add_two_numbers_v4(state: benchmark.State) -> None:
    """Benchmark Add Two Numebrs."""
    n = state.range(0)
    l1, l2 = setup_data(n)
    while state:
        add_two_numbers_v4(l1, l2)
    state.complexity_n = n
