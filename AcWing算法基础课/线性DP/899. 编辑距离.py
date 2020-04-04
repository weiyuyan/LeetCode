#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/30
'''
给定n个长度不超过10的字符串以及m次询问，每次询问给出一个字符串和一个操作次数上限。

对于每次询问，请你求出给定的n个字符串中有多少个字符串可以在上限操作次数内经过操作变成询问给出的字符串。

每个对字符串进行的单个字符的插入、删除或替换算作一次操作。

输入格式
第一行包含两个整数n和m。

接下来n行，每行包含一个字符串，表示给定的字符串。

再接下来m行，每行包含一个字符串和一个整数，表示一次询问。

字符串中只包含小写字母，且长度均不超过10。

输出格式
输出共m行，每行输出一个整数作为结果，表示一次询问中满足条件的字符串个数。

数据范围
1≤n,m≤1000,

输入样例：
3 2
abc
acd
bcd
ab 1
acbd 2
输出样例：
1
3
'''
# 这道题实际上是把编辑距离求若干次就行
# 时间复杂度：1000^2 * 10 * 10 = 1x10^8

class Solution:
    def minEditDistance(self, A: str, B: str):
        # 将A字符串经过若干次操作变成B字符串
        m = len(A)
        n = len(B)
        # 因为涉及到i-1操作和j-1操作，为了避免边界问题，dp数组统一后移一位
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # 初始化数组
        for i in range(m+1):
            dp[i][0] = i    # 这里表示：A长i，B长0，那么由A变到B需要i步骤（i个删除操作）
        for j in range(n+1):
            dp[0][j] = j    # 这里表示：A长0，B长j，那么由A变到B需要j步骤（j个增加操作）

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
                if A[i-1] == B[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    n, m = map(int, input().split())
    s_arr = []
    for i in range(n):
        s_arr.append(input())

    for i in range(m):
        in_li = input().split()
        s = in_li[0]
        limit = int(in_li[1])
        count = 0
        for string in s_arr:
            if solution.minEditDistance(string, s) <= limit:
                count += 1
        print(count)
