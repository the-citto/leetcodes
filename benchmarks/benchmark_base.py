"""Benchamrk leetcodes."""

from __future__ import annotations

import abc
import typing

import google_benchmark as benchmark

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from google_benchmark import (
        __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
    )


class BenchmarkBase[*P, T](abc.ABC):
    """BenchmarkBase."""

    funcs: tuple[Callable[[*P], T], ...]
    best_only = False
    bm_range = (1 << 4, 1 << 19)

    @classmethod
    @abc.abstractmethod
    def _data(cls, n: int) -> tuple[*P]:
        """Return benchmark data."""

    @classmethod
    def _params(
        cls,
        f: Callable[[benchmark.State], None] | OptionMaker.Options,
    ) -> Callable[[benchmark.State], None] | OptionMaker.Options:
        f = benchmark.option.range(*cls.bm_range)(f)
        return benchmark.option.complexity(benchmark.oAuto)(f)

    @classmethod
    def _bm_name(cls, func_name: str) -> str:
        func_v = func_name.split("_")[-1]
        return f"{cls.__name__}_{func_v}"

    @classmethod
    def _bm_factory(cls, target_func: Callable[[*P], T]) -> None:
        def _make_bm(
            f: Callable[[*P], T],
        ) -> Callable[[benchmark.State], None]:
            def _bm_wrapper(state: benchmark.State) -> None:
                n = state.range(0)
                _data = cls._data(n)
                while state:
                    f(*_data)
                state.items_processed = state.iterations * n
                state.complexity_n = n

            # func_v = f.__name__.split("_")[-1]
            # _bm_wrapper.__name__ = f"{cls.__name__}_{func_v}"
            _bm_wrapper.__name__ = cls._bm_name(f.__name__)  # ty: ignore [unresolved-attribute]
            return _bm_wrapper

        bm_func: Callable[[benchmark.State], None] | OptionMaker.Options = _make_bm(target_func)
        bm_func = cls._params(bm_func)
        benchmark.register(bm_func)

    @classmethod
    def register(cls) -> None:
        """Register functions."""
        if cls.best_only:
            cls._bm_factory(cls.funcs[-1])
        else:
            for target_func in cls.funcs:
                cls._bm_factory(target_func)
