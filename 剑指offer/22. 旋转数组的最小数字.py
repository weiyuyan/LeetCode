#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/11
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

输入一个升序的数组的一个旋转，输出旋转数组的最小元素。

例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

数组可能包含重复项。

注意：数组内所含元素非负，若数组大小为0，请返回-1。

样例
输入：nums=[2,2,2,0,1]

输出：0
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        if n < 0:
            return -1
        while n > 0 and nums[0] == nums[n]:
            n -= 1
        if nums[n] >= nums[0]:
            return nums[0]
        l, r= 0, n
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid
        return nums[r]




solution = Solution()
nums = [4, 5, 6, 7, 1, 2, 3]
res = solution.findMin(nums)
print(res)