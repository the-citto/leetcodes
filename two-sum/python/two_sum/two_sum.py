"""Two Sum."""




class TwoSum:
    """Apply constraints."""

    min_nums_len: int = 2
    max_nums_len: int = 10**4
    min_val: int = -(10**9)
    max_val: int = 10**9

    def __init__(self, *, nums: list[int], target: int) -> None:
        """Init."""
        nums_len = len(nums)
        if not (self.min_nums_len <= nums_len <= self.max_nums_len):
            err_msg = (
                f"expected '{self.min_nums_len} <= count of nums <= {self.max_nums_len:_}' "
                f"but received {nums_len} elements"
            )
            raise ValueError(err_msg)
        min_num = min(nums)
        val_err_msg = f"expected '{self.min_val:_} <= num <= {self.max_val:_}' but received num with value"
        if min_num < self.min_val:
            err_msg = f"{val_err_msg} '{min_num}'"
            raise ValueError(err_msg)
        max_num = max(nums)
        if max_num > self.max_val:
            err_msg = f"{val_err_msg} '{max_num}'"
            raise ValueError(err_msg)
        if not self.min_val <= target <= self.max_val:
            err_msg = f"expected '{self.min_val:_} <= count of nums <= {self.max_val:_}' but received {target = }"
            raise ValueError(err_msg)
        self.nums = nums
        self.target = target

    def algo_1(self) -> list[int]:
        """Calculate."""
        for id1, num1 in enumerate(self.nums):
            for id2, num2 in enumerate(self.nums):
                if id1 == id2:
                    continue
                if num1 + num2 == self.target:
                    return [id1, id2]
        err_msg = f"target '{self.target}' unobtainable with given nums"
        raise ValueError(err_msg)

    # def algo_2(self) -> list[int]:
    #     """Calculate."""
    #     for id1, num1 in enumerate(self.nums):
    #         for num2 in self.nums[id1 + 1:]:
    #             if num1 + num2 == self.target:
    #                 return [id1, self.nums.index(num2)]
    #     err_msg = f"target '{self.target}' unobtainable with given nums"
    #     raise ValueError(err_msg)
    #
    # def algo_3(self) -> list[int]:
    #     """Calculate."""
    #     for id1, num1 in enumerate(self.nums):
    #         if self.target - num1 in self.nums[id1+1:]:
    #             return [id1, self.nums.index(self.target - num1)]
    #     err_msg = f"target '{self.target}' unobtainable with given nums"
    #     raise ValueError(err_msg)
    #
    # def algo_4(self) -> list[int]:
    #     """Calculate."""
    #     for id1, num1 in enumerate(self.nums):
    #         num2 = self.target - num1
    #         if num2 in self.nums[id1+1:]:
    #             return [id1, self.nums.index(num2)]
    #     err_msg = f"target '{self.target}' unobtainable with given nums"
    #     raise ValueError(err_msg)

    def algo_2_2(self) -> list[int]:
        """Calculate."""
        for id1, num1 in enumerate(self.nums[::-1]):
            for num2 in self.nums:
                if num1 + num2 == self.target:
                    return [self.nums.index(num2), len(self.nums) - id1 - 1]
        err_msg = f"target '{self.target}' unobtainable with given nums"
        raise ValueError(err_msg)

    def algo_2_3(self) -> list[int]:
        """Calculate."""
        for id_, num in enumerate(self.nums):
            if self.target - num in self.nums[id_+1:]:
                return [id_, len(self.nums) - self.nums[::-1].index(self.target - num) - 1]
        err_msg = f"target '{self.target}' unobtainable with given nums"
        raise ValueError(err_msg)

    def algo_2_4(self) -> list[int]:
        """Calculate."""
        for id_, num in enumerate(self.nums):
            if self.target - num in self.nums[id_+1:]:
                return [id_, self.nums[id_+1:].index(self.target - num) + id_+1]
        err_msg = f"target '{self.target}' unobtainable with given nums"
        raise ValueError(err_msg)






def _main() -> None:
    import time
    foo = TwoSum(nums=[*range(4_999), 10_000, 100_000, *range(4_999)], target=110_000)
    start_time = time.perf_counter()
    print(f"{foo.algo_2_2() = }")
    print(time.perf_counter() - start_time)

    start_time = time.perf_counter()
    print(f"{foo.algo_2_3() = }")
    print(time.perf_counter() - start_time)

    start_time = time.perf_counter()
    print(f"{foo.algo_2_4() = }")
    print(time.perf_counter() - start_time)

    start_time = time.perf_counter()
    print(f"{foo.algo_1() = }")
    print(time.perf_counter() - start_time)







