#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2019/8/3

import time
from typing import List
1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    return [i, i + j + 1]

    def tow_sum_with_dict(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, m in enumerate(nums):
            _dict[m] = i

        for i, m in enumerate(nums):
            j = _dict.get(target - m)
            if j is not None and i != j:
                return [i, j]

    def tow_sum_with_dict2(self, nums: List[int], target: int) -> List[int]:

        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:
                return [_dict.get(target - m), i]
            _dict[m] = i



def main():
    nums = [2,5,5,7]
    target = 10
    solution = Solution()

    # print(solution.twoSum(nums, target))

    print(solution.tow_sum_with_dict(nums, target))
    print(solution.tow_sum_with_dict2(nums, target))

if __name__ == '__main__':
    main()
