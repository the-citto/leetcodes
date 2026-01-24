"""Test Zigzag Conversion."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_006_zigzag_conversion
from tests.test_base import TestBase

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestZigzagConversion[*P, T](TestBase[*P, T]):
    """TestZigzagConversion."""

    __test__ = True

    @pytest.fixture(
        params=[
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 1, "A"),
            ("ABCD", 1, "ABCD"),
            ("ABCDEFG", 3, "AEBDFCG"),
        ],
    )
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""
        return request.param

    @pytest.fixture(
        params=[
            lc_006_zigzag_conversion.zigzag_conversion_v1,
            lc_006_zigzag_conversion.zigzag_conversion_v2,
        ],
        ids=lambda p: p.__name__.split("_")[-1],
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    @typing.override
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        super().test_run(func, data)
