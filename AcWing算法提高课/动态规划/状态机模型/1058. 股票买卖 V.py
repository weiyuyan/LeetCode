#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/23
'''
给定一个长度为 N 的数组，数组中的第 i 个数字表示一个给定股票在第 i 天的价格。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
输入格式
第一行包含整数 N，表示数组长度。

第二行包含 N 个不超过 10000 的正整数，表示完整的数组。

输出格式
输出一个整数，表示最大利润。

数据范围
1≤N≤105
输入样例：
5
1 2 3 0 2
输出样例：
3
样例解释
对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]，第一笔交易可得利润 2-1 = 1，第二笔交易可得利润 2-0 = 2，共得利润 1+2 = 3。
'''
# 本题有三个状态：手中有货、手中无货的第1天、手中无货的第>=2天
# 手中有货->手中无货的第1天 || 手中有货
# 手中无货的第1天 -> 手中无货的第>=2天
#  手中无货的第>=2天 -> 手中有货 || 手中无货的第>=2天
# 入口有1个：手中无货的第>=2天
# 出口有两个：手中无货的第1天、手中无货的第>=2天

# 状态表示：f[i][0] = max(f[i-1][0], f[i-1][2]+w[i])
#          f[i][1] = f[i-1][0] + w[i]
#          f[i][2] = max(f[i-1][1], f[i-1][2])

from typing import List
class Solution:
    def stock(self, price: List[int]):
        dp = [[0 for _ in range(3)] for _ in range(len(price)+1)]
        dp[0][0] = float('-inf')
        dp[0][1] = float('-inf')

        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                dp[i][0] = max(dp[i-1][0], dp[i-1][2]-price[i-1])
                dp[i][1] = dp[i-1][0] + price[i-1]
                dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])

if __name__ == '__main__':
    solution = Solution()
    num = int(input())
    prices = list(map(int, input().split()))
    res = solution.stock(prices)
    print(res)

