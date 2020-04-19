#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/17
'''
给定一个长度为 N 的数组，数组中的第 i 个数字表示一个给定股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润，你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。一次买入卖出合为一笔交易。

输入格式
第一行包含整数 N 和 k，表示数组的长度以及你可以完成的最大交易数量。

第二行包含 N 个不超过 10000 的正整数，表示完整的数组。

输出格式
输出一个整数，表示最大利润。

数据范围
1≤N≤105,
1≤k≤100
输入样例1：
3 2
2 4 1
输出样例1：
2
输入样例2：
6 2
3 2 6 5 0 3
输出样例2：
7
样例解释
样例1：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

样例2：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
共计利润 4+3 = 7.
'''
# 状态机：①手中有货 ②手中无货
# 状态转换：手中有货→手中无货（+w[i]）    ||    手中有货→手中有货（+0）（持有，所以资金不发生变化）
#          手中无货→手中有货（-w[i]）    ||    手中无货→手中无货（+0）
# 我们用0表示手中无货，1表示手中有货

# 状态表示：dp[i][j][0|1] 表示已经进行到第i天，且完成了j-1笔交易，正在进行第j笔交易，且手中有货|无货的买法的集合  属性：max
# 状态计算：dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+w[i])
#          dp[i][j][1] = max(dp[i-1][j-1][0]-w[i], dp[i-1][j][1])

from typing import List
class Solution:
    def stock_predict(self, stocks: List[int], k: int):
        res = 0
        dp = [[[float('-inf')for _ in range(2)] for _ in range(k+1)] for _ in range(len(stocks)+1)]
        for i in range(len(dp)):
            dp[i][0][0] = 0

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+stocks[i-1])
                dp[i][j][1] = max(dp[i-1][j-1][0]-stocks[i-1], dp[i-1][j][1])
                res = max(res, dp[i][j][0], dp[i][j][1])
        return res

if __name__ == '__main__':
    solution = Solution()
    num, k = map(int, input().split())
    stocks = list(map(int, input().split()))
    res = solution.stock_predict(stocks, k)
    print(res)
