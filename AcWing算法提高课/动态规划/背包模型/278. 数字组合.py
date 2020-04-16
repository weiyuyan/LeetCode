#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
给定N个正整数A1,A2,…,AN，从中选出若干个数，使它们的和为M，求有多少种选择方案。

输入格式
第一行包含两个整数N和M。

第二行包含N个整数，表示A1,A2,…,AN。

输出格式
包含一个整数，表示可选方案数。

数据范围
1≤N≤100,
1≤M≤10000,
1≤Ai≤1000
输入样例：
4 4
1 1 2 2
输出样例：
3
'''
# 状态表示：①集合：dp[i][j]表示所有只从前i个数字中选，并且总体积恰好为j的方案数  ②属性：count
# 状态计算：分为两个状态：不包括i的所有选法；不包括i的所有选法
# dp[i][j] = dp[i-1][j] + dp[i-1][j-a[i]]

from typing import List
class Solution:
    def choose_num(self, nums: List[int], M: int):
        # 初始化
        dp = [[0 for _ in range(M+1)] for _ in range(len(nums)+1)]
        dp[0][0] = 1

        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[-1][-1]

# 优化
from typing import List
class Solution:
    def choose_num(self, nums: List[int], M: int):
        dp = [0 for _ in range(M+1)]
        dp[0] = 1

        for i in range(len(nums)):
            v = nums[i]
            for j in range(M, v-1, -1):
                dp[j] += dp[j-v]
        return dp[-1]



if __name__ == '__main__':
    solution = Solution()
    N, M = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    res = solution.choose_num(nums, M)
    print(res)