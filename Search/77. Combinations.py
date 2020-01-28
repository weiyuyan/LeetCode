#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/28
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''
# 方法一：回溯法
from typing import List
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         def backtrack(first=1, curr=[]):
#             if len(curr) == k:
#                 res.append(curr[:])
#             for i in range(first, n+1):
#                 curr.append(i)
#                 backtrack(i+1, curr)
#                 curr.pop()
#         backtrack()
#         return res

# 方法二：字典序组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, k + 1)) + [n + 1]
        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return output



if __name__ == '__main__':
    solution = Solution()
    res = solution.combine(4, 2)
    print(res)





