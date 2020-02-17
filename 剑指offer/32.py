#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/17
from typing import List
class Solution(object):
    def exchange(self, nums: List[int]) -> List[int]:
        """
        :type array: List[int]
        :rtype: void
        """
        # 这次要用到双指针
        # p, q = 0, len(array)-1
        # while(p<q):
        #     if array[p] % 2 == 0:
        #         if array[q] % 2 == 0:
        #             q -= 1
        #         else:
        #             array[p], array[q] = array[q], array[p]
        #             p += 1
        #             q -= 1
        #     else:
        #         p += 1

        p, q = 0, len(nums) - 1
        while (p < q):
            if self.judge(nums[p]):
                if self.judge(nums[q]):
                    q -= 1
                else:
                    nums[p], nums[q] = nums[q], nums[p]
                    p += 1
                    q -= 1
            else:
                p += 1
        return nums

    # 可扩展的方法，这里提出了一个通用的框架
    def judge(self, x) -> bool:
        return True if x % 2 == 0 else False
        # return True if x % 3 == 0 else False
solution = Solution()
res = solution.exchange([1, 2, 3, 4])
print(res)