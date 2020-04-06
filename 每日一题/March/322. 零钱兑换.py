#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/3
'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

'''
# 背包问题：
# 状态表示：①：集合f[i][j]表示只看前i个硬币能填满容量为j（amount）的背包所用硬币数的集合     ②属性：min
# 状态计算：f[i][j] = min(f[i-1][j]，f[i][j-a[k]+1] for k in range(1, i+1) )
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0
        coins.sort()
        if coins[0]>amount: return -1


        # dp = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins)+1)]
        # dp[1][coins[0]] = 1
        # for i in range(amount):
        #     dp[0][i] = 0
        # for j in range(len(coins)+1):
        #     dp[j][0] = 0
        #
        # for i in range(1, len(coins)+1):
        #     for j in range(amount+1):
        #         for k in range(i):
        #             if j-coins[k] >= 0:
        #                 dp[i][j] = min(dp[i][j], dp[i][j-coins[k]]+1)
        # print(dp)
        _dp = [float('inf') for _ in range(amount+1)]
        _dp[0] = 0
        for j in range(amount+1):
            for k in range(len(coins)):
                if j-coins[k] >= 0:
                    _dp[j] = min(_dp[j], _dp[j-coins[k]]+1)
        print(_dp)

        # if dp[-1][-1] == float('inf'): return -1
        # else:
        #     return dp[-1][-1]

        if _dp[-1] == float('inf'): return -1
        else:
            return _dp[-1]

if __name__ == '__main__':
    solution = Solution()
    coins = [84,457,478,309,350,349,422,469,100,432,188]
    amount = 6993
    res = solution.coinChange(coins, amount)
    print(res)