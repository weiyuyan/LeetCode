#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/29
'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

'''
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
        pass
        repository = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        def track_back(depth, tmp_repository, tmp_res):
            if sum(tmp_res)>n or depth>k:
                return
            if sum(tmp_res)==n and depth==k:
                res.append(tmp_res[:])
                return
            for i in range(len(tmp_repository)):
                track_back(depth+1, tmp_repository[i+1:], tmp_res+[tmp_repository[i]])

        for i in range(9):
            track_back(1, repository[i+1:], [i+1])

        return res
solution = Solution()
res = solution.combinationSum3(3, 9)
print(res)