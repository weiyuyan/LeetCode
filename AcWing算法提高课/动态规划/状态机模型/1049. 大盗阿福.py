#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/17
'''
阿福是一名经验丰富的大盗。趁着月黑风高，阿福打算今晚洗劫一条街上的店铺。

这条街上一共有 N 家店铺，每家店中都有一些现金。

阿福事先调查得知，只有当他同时洗劫了两家相邻的店铺时，街上的报警系统才会启动，然后警察就会蜂拥而至。

作为一向谨慎作案的大盗，阿福不愿意冒着被警察追捕的风险行窃。

他想知道，在不惊动警察的情况下，他今晚最多可以得到多少现金？

输入格式
输入的第一行是一个整数 T，表示一共有 T 组数据。

接下来的每组数据，第一行是一个整数 N ，表示一共有 N 家店铺。

第二行是 N 个被空格分开的正整数，表示每一家店铺中的现金数量。

每家店铺中的现金数量均不超过1000。

输出格式
对于每组数据，输出一行。

该行包含一个整数，表示阿福在不惊动警察的情况下可以得到的现金数量。

数据范围
1≤T≤50,
1≤N≤105
输入样例：
2
3
1 8 2
4
10 7 6 14
输出样例：
8
24
样例解释
对于第一组样例，阿福选择第2家店铺行窃，获得的现金数量为8。

对于第二组样例，阿福选择第1和4家店铺行窃，获得的现金数量为10+14=24。
'''
# 状态表示：dp[i]表示抢劫前i家店铺的所有情况      属性：max
# 状态计算：一共有两个状态：①抢劫第i家店铺     ②不抢劫第i家店铺
# dp[i] = max(dp[i-1], dp[i-2]+a[i])
from typing import List
class Solution:
    def rob(self, market: List[int]):
        dp = [0 for _ in range(len(market))]
        if len(market) <= 2:
            return max(market) if market else 0

        dp[0] = market[0]
        dp[1] = max(market[0], market[1])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+market[i])
        return dp[-1]

# 方法二：状态机
# 把每个操作作为一个状态 比如买卖股票：只有先买了以后才能再卖
# 状态机描述的是一个过程，而不是结果，是一个动作
# 状态机和状态压缩dp其实是一种另类的状态表示方式

# 本题呢，主要有两个状态：我们记为zero和one
# 对于dp[i]的状态，zero表示未选择第i个店铺，one代表选择了第i个店铺
# 对于zero状态，它的下一个状态dp[i+1]，可以选择zero，也可以选择one
# 对于one状态，它的下一个状态dp[i+1]，只能选择zero
# 所以我们的状态机一共有：两个点，三条边

# 所以，dp是二维的：dp[i][0/1]
# dp[i][0] = max(dp[i-1][0], dp[i-1][1])
# dp[i][1] = dp[i-1][0]+w[i]
from typing import List
class Solution:
    def rob(self, market: List[int]):
        dp = [[0 for _ in range(2)] for _ in range(len(market)+1)]
        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + market[i-1]
        return max(dp[-1])

if __name__ == '__main__':
    solution = Solution()
    res = []
    groups = int(input())
    for i in range(groups):
        num = int(input())
        market = list(map(int, input().split()))
        res.append(solution.rob(market))

    for j in res:
        print(j)
