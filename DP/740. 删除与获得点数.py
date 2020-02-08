#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/8
'''
给定一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1:

输入: nums = [3, 4, 2]
输出: 6
解释:
删除 4 来获得 4 个点数，因此 3 也被删除。
之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
示例 2:

输入: nums = [2, 2, 3, 3, 3, 4]
输出: 9
解释:
删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
注意:

nums的长度最大为20000。
每个整数nums[i]的大小都在[1, 10000]范围内。
'''
'''
class Solution(object):
    def deleteAndEarn(self, nums):
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)
'''
import collections
from typing import List
class Solution:
    # 官方解答
    # def deleteAndEarn(self, nums: List[int]) -> int:
    #     count = collections.Counter(nums)
    #     prev = None
    #     avoid = using = 0
    #     for k in sorted(count):
    #         if k-1 != prev:
    #             avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
    #         else:
    #             avoid, using = max(avoid, using), k * count[k] + avoid
    #         prev = k
    #     return max(avoid, using)

    # 修改第198T，即可解决本题
    # 如 [2, 2, 3, 3, 3, 4]，改成[0, 0, 2, 3, 1]，代表0有0个，1有0个，2有2个，3有3个，4有1个
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) != 0:
            nums.sort()
        else:
            return 0
        count = collections.Counter(nums)
        max_num = max(count)
        min_num = min(count)
        a_list = [count[i]*i for i in range(min_num, max_num+1)]
        # 至此、问题转换成了第198：打家劫舍问题
        res = self.rob(a_list)
        return res


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max((nums[0] + nums[2]), nums[1])

        money = [nums[0], nums[1], nums[2] + nums[0]]  # 初始化money数组
        for i in range(3, len(nums)):
            money.append(max(money[i - 2], money[i - 3]) + nums[i])

        return max(money)


if __name__ == '__main__':
    nums = []
    solution = Solution()
    res = solution.deleteAndEarn(nums)
    print(res)