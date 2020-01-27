#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/27
'''
给定一个长度为 n+1 的数组nums，数组中所有的数均在 1∼n 的范围内，其中 n≥1。

请找出数组中任意一个重复的数，但不能修改输入的数组。

样例
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。

返回 2 或 3。
思考题：如果只能使用 O(1) 的额外空间，该怎么做呢？
'''
# 分治法
class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        left = 1
        right = len(nums) - 1
        while(left < right):
            mid = (right+left) // 2
            count = 0
            for x in nums:
                if x >= left and x <= mid:
                    count += 1
            if count > mid - left + 1:
                right = mid
            else:
                left = mid + 1
        return right
solution = Solution()
res = solution.duplicateInArray([1,2,3,3,4,5])
print(res)
