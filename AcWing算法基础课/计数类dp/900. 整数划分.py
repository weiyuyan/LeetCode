#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/31
'''
一个正整数n可以表示成若干个正整数之和，形如：n=n1+n2+…+nk，其中n1≥n2≥…≥nk,k≥1。

我们将这样的一种表示称为正整数n的一种划分。

现在给定一个正整数n，请你求出n共有多少种不同的划分方法。

输入格式
共一行，包含一个整数n。

输出格式
共一行，包含一个整数，表示总划分数量。

由于答案可能很大，输出结果请对109+7取模。

数据范围
1≤n≤1000
输入样例:
5
输出样例：
7
'''
# 状态表示：①集合：f[i]表示正整数i符合要求的划分数量      ②属性：count
# 状态计算：可以分成i份：从1~i划分，表示a[i]划分的第1个数，可以从i到1选
# f[i] = f[i]x1（划分的第一个数是i，所以就没了，所以==1） + f[i-1]x1 + f[i-2]x1 +...+ f[1]x1


# 解法一：可以把该题考虑为完全背包问题：
# 背包的总容量是n，有体积为1~n的货物若干，问刚好把背包填满有多少种方法
# 状态表示：①集合：f[i][j]表示从1~i中选，总体积恰好是j的选法的集合     ②属性：count
# 状态计算：将f[i][j]集合划分：最后一个物品（i）选几个。从0,1,2,...,s个
# f[i][j] = f[i-1][j] + f[i-1][j-i] + f[i-1][j-2i] +...+ f[i-1][j-s*i]
# f[i][j-i] = f[i-1][j-i] + f[i-1][j-2i] +...+ f[i-1][j-s*i]
# 所以，f[i][j]可以简化为f[i-1][j]+f[i][j-i]
class Solution:
    def splitNum(self, num: int):
        _mod = 1e9+7
        # dp = [[1 for _ in range(num+1)] for _ in range(num+1)]
        # for i in range(num+1):
        #     dp[0][i] = 0
        #     dp[i][0] = 0
        # for i in range(1, num+1):
        #     for j in range(i, num+1):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]
        dp = [0 for _ in range(num+1)]
        dp[0] = 1
        for i in range(1, num+1):
            for j in range(i, num+1):
                dp[j] = int((dp[j] + dp[j-i]) % _mod)
        # return int(divmod(dp[-1], _mod)[1])
        return dp[-1]



if __name__ == '__main__':
    solution = Solution()
    num = int(input())
    res = solution.splitNum(num)
    print(res)