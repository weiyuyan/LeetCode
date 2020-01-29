#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/29
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''
from typing import List
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         nums.sort()
#         used = [False for _ in range(n)]
#
#         def dfs(nums, size, depth, path, used, res):
#             res.append(path[:])
#             for i in range(size):
#                 if not used[i]:
#                     if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
#                         continue
#                     used[i] = True
#                     path.append(nums[i])
#                     dfs(nums, size, depth+1, path, used, res)
#                     used[i] = False
#                     path.pop()
#         dfs(nums=nums, size=n, depth=0, path=[], used=used, res=res)
#         return res


# 刚开始我们只有空集一个答案，循环所有可能的数字，每次循环我们对当前答案的每一种情况考虑加入从1到上限次该数字并更新答案即可
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        res = [[]]
        for i, v in dic.items():
            temp = res.copy()
            for j in res:
                for k in range(v):
                    temp.append(j+[i]*(k+1))
            res = temp
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.subsetsWithDup([1, 2, 2])
    print(res)