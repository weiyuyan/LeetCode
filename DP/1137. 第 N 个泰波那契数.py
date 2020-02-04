#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/3
'''
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537
 

提示：

0 <= n <= 37
答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
'''
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         res = [0, 1, 1]
#         for _ in range(n-2):
#             res.append(0)
#         for i in range(3, n+1):
#             res[i] = res[i-1] + res[i-2] + res[i-3]
#         return res[n]

# 2333，O(1)做法，要啥自行车
class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415,
	223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601,
	334745777, 615693474, 1132436852, 2082876103]
        return res[n]
if __name__ == '__main__':
    solution = Solution()
    res = solution.tribonacci(25)
    print(res)