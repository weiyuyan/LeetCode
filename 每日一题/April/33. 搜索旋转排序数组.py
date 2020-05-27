#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/29
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
通过次数116,097提交次数307,648
'''
from typing import List
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if nums[0] < nums[-1]:
#             res = self.forward_binary_search(nums, target, 0, len(nums))
#             return res
#         if nums[0] >
#
#         # 首先要找到在哪个位置做了旋转
#         # 把一个数组分为两部分，然后分别进行二分查找
#         pos = self.find(nums, 0, len(nums)-1)
#         a = nums[:pos]
#         b = nums[pos:]
#
#         resa = self.forward_binary_search(a, target, 0, len(a))
#         resb = self.binary_search(b, target, 0, len(b))
#         return max(resa, resb, -1)
#
#     def find(self, nums: List[int], l: int, r: int):
#         # i:当前位置
#         # 找到数组旋转的位置，0表示没有旋转
#         # 进行二分查找，mid = (l+r)//2 如果nums[mid]<nums[0]，那么旋转的位置是在mid左边，在[0,mid]内寻找
#         # 如果nums[mid]>nums[0]，那么旋转的位置在mid的右边，在[mid+1, len(num)]寻找
#         mid = (l+r) >> 1
#         while(l<mid):
#             if nums[mid]<nums[0]:
#                 return self.find(nums, l, mid)
#             else:
#                 return self.find(nums, mid+1, r)
#
#         return mid
#
#
#     def forward_binary_search(self, nums: List[int], target: int, left: int, right: int):
#         mid = (left+right) >> 1
#
#         pass
#
# if __name__ == '__main__':
#     solution = Solution()
#     nums = [7,6,5,4,3,2,1]
#     # target = 0
#     # res = solution.find(nums, 0, 6)
#     # print(nums[:3])
#     res = solution.find(nums,0, 6)
#     print(res)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
