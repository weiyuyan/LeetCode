#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/31
'''
给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。

返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。

 

示例 1：

输入：[1,17,8]
输出：2
解释：
[1,8,17] 和 [17,8,1] 都是有效的排列。
示例 2：

输入：[2,2,2]
输出：1
 

提示：

1 <= A.length <= 12
0 <= A[i] <= 1e9
'''
from typing import List
import math
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:

        len_list = len(A)
        if len_list == 0:
            return 0
        if len_list == 1:
            if math.sqrt(A[0]) % 1 == 0:
                return 1
            else:
                return 0
        self.res = 0
        A.sort()
        used = [False for _ in A]

        # def _judge(A: List[int]) -> int:
        #     '''
        #     先设计一个判断函数，用来判断是否是正方形排列数组
        #     :param A: 待判定数组
        #     :return: 0或1 其中0代表不是正方形排列 1代表是正方形排列
        #     '''
        #     for i in range(len(A)-1):
        #         if math.sqrt(A[i]+A[i+1]) % 1 != 0:
        #             return 0
        #     return 1

        def _new_judge(a: int, b: int) -> bool:
            '''
            先设计一个判断函数，用来判断相邻的两个数是否构成正方形排列
            :param a:
            :param b:
            :return:
            '''
            if math.sqrt(a+b) % 1 != 0:
                return False
            return True

        def _track_back(depth: int, path: List[int], used: List[bool]):
            '''
            回溯函数，用来求得无重复的排列数组，同时调用_judge函数计算res值
            :param depth: 当前树深度
            :param path: 当前遍历元素
            :param used: 元素使用情况
            :return:
            '''
            # 这里用到了剪枝
            if depth > 1 and not _new_judge(path[-1], path[-2]):
                return
            if depth == len_list:
                self.res += 1
                return
            for i in range(len_list):
                if not used[i]:
                    if i>0 and A[i]==A[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(A[i])
                    _track_back(depth+1, path, used)
                    # 回复原状
                    used[i] = False
                    path.pop()

        _track_back(0, [], used)
        return self.res

# 网友的另一种做法
# class Solution(object):
#
#     def numSquarefulPerms(self, A):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums = A
#         nums.sort()
#         res = []
#         def backtrack(nums, tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 # 去重
#                 if i and nums[i]==nums[i-1]:
#                     continue
#                 # 剪枝
#                 if not tmp or math.sqrt(tmp[-1]+nums[i]) % 1 == 0:
#                     backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
#         backtrack(nums, [])
#         return len(res)

if __name__ == '__main__':
    solution = Solution()
    res = solution.numSquarefulPerms([1,17,8])
    print(res)