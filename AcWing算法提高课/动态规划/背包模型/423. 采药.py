#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/14
'''
辰辰是个天资聪颖的孩子，他的梦想是成为世界上最伟大的医师。

为此，他想拜附近最有威望的医师为师。

医师为了判断他的资质，给他出了一个难题。

医师把他带到一个到处都是草药的山洞里对他说：“孩子，这个山洞里有一些不同的草药，采每一株都需要一些时间，每一株也有它自身的价值。我会给你一段时间，在这段时间里，你可以采到一些草药。如果你是一个聪明的孩子，你应该可以让采到的草药的总价值最大。”

如果你是辰辰，你能完成这个任务吗？

输入格式
输入文件的第一行有两个整数T和M，用一个空格隔开，T代表总共能够用来采药的时间，M代表山洞里的草药的数目。

接下来的M行每行包括两个在1到100之间（包括1和100）的整数，分别表示采摘某株草药的时间和这株草药的价值。

输出格式
输出文件包括一行，这一行只包含一个整数，表示在规定的时间内，可以采到的草药的最大总价值。

数据范围
1 <= T <= 1000
1 <= M <= 100

输入样例：
70 3
71 100
69 1
1 2
输出样例：
3
'''
# 状态表示：①集合：dp[i][j]表示只看前i朵草药，且采药时间为j，能采到的草药的集合  ②属性：max
# 状态计算：（集合划分）是否采了第i朵草药
# dp[i][j] = max(dp[i-1][j]（没采）,dp[i-1][j-a[i]] + w[i])，其中a[i]是第i个草药的时间，w[i]是第i个草药的价值

from typing import List
class Solution:
    def get_herb(self, time: int, herbs: List[List[int]]):
        dp = [[0 for j in range(time+1)] for i in range(len(herbs)+1)]
        for i in range(1, len(dp)):
            for j in range(0, len(dp[0])):
                if j >= herbs[i-1][0]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-herbs[i-1][0]]+herbs[i-1][1])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

# 改成一维数组
class Solution:
    def get_herb(self, time: int, herbs: List[List[int]]):
        dp = [0 for _ in range(time+1)]
        for i in range(len(herbs)):
            t = herbs[i][0]
            val = herbs[i][1]
            for j in range(time, t-1, -1):
                dp[j] = max(dp[j], dp[j-t]+val)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    time, nums = list(map(int, input().split()))
    herbs = []
    for i in range(nums):
        herbs.append(list(map(int, input().split())))
    res = solution.get_herb(time, herbs)
    print(res)