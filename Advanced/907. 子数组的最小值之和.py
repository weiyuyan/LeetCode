#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/21
'''
给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。

由于答案可能很大，因此返回答案模 10^9 + 7。

 

示例：

输入：[3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
 

提示：

1 <= A <= 30000
1 <= A[i] <= 30000

'''
# 方法一：暴力法
# 这种方法会造成超时
from typing import List
# class Solution:
#     def sumSubarrayMins(self, A: List[int]) -> int:
#         A_len = len(A)
#         res = 0
#         for i in range(A_len):
#             for j in range(i, A_len):
#                 res += min(A[i:j+1])
#                 # print(A[i:j+1])
#         return res


# 方法二：单调栈
# 不会
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        stack = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while stack and A[stack[-1]] > x:
                j = stack.pop()
                k = stack[-1]
                res += A[j] * (i - j) * (j - k)
            stack.append(i)
        return res % (10 ** 9 + 7)


solution = Solution()
res = solution.sumSubarrayMins([3,1,2,4])
print(res)