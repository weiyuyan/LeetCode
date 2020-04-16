#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
有一个箱子容量为 V，同时有 n 个物品，每个物品有一个体积（正整数）。

要求 n 个物品中，任取若干个装入箱内，使箱子的剩余空间为最小。

输入格式
第一行是一个整数 V，表示箱子容量。

第二行是一个整数 n，表示物品数。

接下来 n 行，每行一个正整数（不超过10000），分别表示这 n 个物品的各自体积。

输出格式
一个整数，表示箱子剩余空间。

数据范围
0<V≤20000,
0<n≤30
输入样例：
24
6
8
3
12
7
9
7
输出样例：
0
'''
# 状态表示：dp[i][j]表示只看前i个物品，且箱子体积为j的情况下，箱子剩余体积的集合  属性：min
# 状态计算：分为放第i个物品和不放第i个物品
# 放： dp[i][j] = dp[i-1][j-i] （前提：j >= i）
# 不放： dp[i][j] = dp[i-1][j]

# 真正的解法：
# 原题可以看成：背包问题，只不过价值变成了每个物品的体积
# 原题可以改为：在总体积不变的情况下，背包里物品的体积最大是多少

# from typing import List
# class Solution:
#     def box(self, stuff: List[int], space: int):
#         dp = [[float('inf') for _ in range(space+1)] for _ in range(len(stuff)+1)]
#         for i in range(len(dp)):
#             dp[i][0] = 0
#
#         for j in range(len(dp[0])):
#             dp[0][j] = j
#
#         for i in range(1, len(dp)):
#             for j in range(1, len(dp[0])):
#                 if j >= i:
#                     dp[i][j] = dp[i-1][j] - i
#                 else:
#                     dp[i][j] = min(dp[i][j], dp[i-1][j])
#         return dp[-1][-1]

from typing import List
class Solution:
    def box(self, stuff: List[int], space: int):
        dp = [[0 for _ in range(space+1)] for _ in range(len(stuff)+1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j >= stuff[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stuff[i-1]]+stuff[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    space = int(input())
    nums = int(input())
    stuff = []
    for i in range(nums):
        stuff.append(int(input()))
    res = solution.box(stuff, space)
    print(space-res)