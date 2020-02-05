#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/5
'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''
# 与121题的区别：①可以买卖多次  ②有冷却期（cooldown）
from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         sold = 0
#         rest = 0
#         hold = float('-inf')
#         for price in prices:
#             prev_sold = sold
#             sold = hold + price
#             hold = max(hold, rest-price)
#             rest = max(rest, prev_sold)
#         return max(rest, sold)
pass

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 新建一个额外数组，存储价格的差
#         money = []
#         for i in range(1, len(prices)):
#             money.append(prices[i]-prices[i-1])
#
#         # 开始动态规划
#         flag = 0
#         for i in range(len(money)):
#             if money[i] >= 0 and flag==0:
#                 money[i] += money[i-1]
#             if money[i] >= 0 and flag == 1:
#                 money[i] += money[i-2]
#                 flag = 0
#             if money[i] < 0 and flag == 0:
#                 money[i] = 0
#                 continue
#             if money[i] < 0 and flag == 1:
#                 money[i] = money[i-1]
#                 flag =






if __name__ == '__main__':
    # solution = Solution()
    # res = solution.maxProfit([1,2,3,0,2])
    # print(res)
