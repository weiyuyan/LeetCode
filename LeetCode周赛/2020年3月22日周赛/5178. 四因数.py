#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/22
'''
给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。

如果数组中不存在满足题意的整数，则返回 0 。

示例：

输入：nums = [21,4,7]
输出：32
解释：
21 有 4 个因数：1, 3, 7, 21
4 有 3 个因数：1, 2, 4
7 有 2 个因数：1, 7
答案仅为 21 的所有因数的和。


提示：

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
'''
import math
from typing import List
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = []
        # 求因数
        for num in nums:
            tmp_factor = []
            factor_num = 0
            for i in range(1, int(math.sqrt(num))+1):
                if num%i == 0:
                    a = num//i
                    if a != i:
                        tmp_factor.append(a)
                        tmp_factor.append(i)
                        factor_num += 2
                    else:
                        tmp_factor.append(a)
                        factor_num += 1
                if len(tmp_factor) > 4:
                    break
            if factor_num==4:
                res.append(tmp_factor)
        return sum(sum(i) for i in res)

solution = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
res = solution.sumFourDivisors(nums)
print(res)

