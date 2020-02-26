#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/25
'''
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 
提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/
'''

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 思路：遍历nums数组，不断将nums[i]驾到tmp_max上。
        # 如果tmp_max > result，更新result
        # 如果tmp_max <= 0 tmp_max置0, i += 1
        if not nums: return []
        tmp_max = 0
        result = nums[0]
        for i in range(len(nums)):
            tmp_max += nums[i]
            if tmp_max > result: result = tmp_max
            if tmp_max <= 0: tmp_max = 0

        return result
