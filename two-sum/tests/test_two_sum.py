"""Test Two Sum."""

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from two_sum import two_sum



DataFixtureType = tuple[list[int], int, list[int]]


@pytest.fixture(params=[
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def data_outliers(request: pytest.FixtureRequest) -> DataFixtureType:
    """Return data outliers."""
    return request.param


@pytest.fixture(params=[
    ([*range(5_000), 10_000, 100_000], 110_000, [5_000, 5_001]),
    ([*range(4_999), 10_000, 100_000, *range(4_999)], 110_000, [4_999, 5_000]),
])
def data_benchmark(request: pytest.FixtureRequest) -> DataFixtureType:
    """Return data for benchmarks."""
    return request.param



data_failures = []



class TestTwoSumOutliers:
    """Test outliers TwoSum class methods."""

    @pytest.fixture()
    def two_sum_inst(self, data_outliers: DataFixtureType) -> two_sum.TwoSum:
        """Init class with constraints."""
        nums, target, self.expected = data_outliers
        return two_sum.TwoSum(nums=nums, target=target)

    def test_algo_1(self, two_sum_inst: two_sum.TwoSum) -> None:
        """Test."""
        assert two_sum_inst.algo_1() == self.expected

    def test_algo_2(self, two_sum_inst: two_sum.TwoSum) -> None:
        """Test."""
    #     assert two_sum_inst.algo_2() == self.expected
    #
    # def test_algo_3(self, two_sum_inst: two_sum.TwoSum) -> None:
    #     """Test."""
    #     assert two_sum_inst.algo_3() == self.expected
    #
    # def test_algo_4(self, two_sum_inst: two_sum.TwoSum) -> None:
    #     """Test."""
    #     assert two_sum_inst.algo_4() == self.expected

    def test_algo_2_2(self, two_sum_inst: two_sum.TwoSum) -> None:
        """Test."""
        assert two_sum_inst.algo_2_2() == self.expected

    def test_algo_2_3(self, two_sum_inst: two_sum.TwoSum) -> None:
        """Test."""
        assert two_sum_inst.algo_2_3() == self.expected

    def test_algo_2_4(self, two_sum_inst: two_sum.TwoSum) -> None:
        """Test."""
        assert two_sum_inst.algo_2_4() == self.expected



class TestTwoSumBenchmark:
    """Test and benchmark TwoSum class methods."""

    @pytest.fixture()
    def two_sum_inst(self, data_benchmark: DataFixtureType) -> two_sum.TwoSum:
        """Init class with constraints."""
        nums, target, self.expected = data_benchmark
        return two_sum.TwoSum(nums=nums, target=target)

    def test_algo_1(self, two_sum_inst: two_sum.TwoSum, benchmark: BenchmarkFixture) -> None:
        """Test."""
        result = benchmark(two_sum_inst.algo_1)
        assert result == self.expected

    def test_algo_2_2(self, two_sum_inst: two_sum.TwoSum, benchmark: BenchmarkFixture) -> None:
        """Test."""
        result = benchmark(two_sum_inst.algo_2_2)
        assert result == self.expected

    def test_algo_2_3(self, two_sum_inst: two_sum.TwoSum, benchmark: BenchmarkFixture) -> None:
        """Test."""
        result = benchmark(two_sum_inst.algo_2_3)
        assert result == self.expected

    def test_algo_2_4(self, two_sum_inst: two_sum.TwoSum, benchmark: BenchmarkFixture) -> None:
        """Test."""
        result = benchmark(two_sum_inst.algo_2_4)
        assert result == self.expected









