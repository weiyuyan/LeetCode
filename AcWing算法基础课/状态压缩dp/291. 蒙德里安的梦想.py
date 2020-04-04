#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/31
'''
求把N*M的棋盘分割成若干个1*2的的长方形，有多少种方案。

例如当N=2，M=4时，共有5种方案。当N=2，M=3时，共有3种方案。

如下图所示：

2411_1.jpg

输入格式
输入包含多组测试用例。

每组测试用例占一行，包含两个整数N和M。

当输入用例N=0，M=0时，表示输入终止，且该用例无需处理。

输出格式
每个测试用例输出一个结果，每个结果占一行。

数据范围
1≤N,M≤11
输入样例：
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
输出样例：
1
0
1
2
3
5
144
51205
'''
# 这是一个非常经典的状态压缩dp问题
# 核心：先放横着的，再放竖着的。总方案数：等于只放横着的小方块的合法方案数
# 问题：如何判断当前的方案是合法的？（即当前摆完横着的小方块后，剩余的位置能否填充满竖着的小方块）
# 怎么判断呢？可以按列来看，每一列内部所有连续得、空着的小方块个数是偶数个

# 状态表示：（化零为整）①集合f[i][j]表示已经将前i-1列摆好，且从第i-1列伸出到第i列的状态是j的所有方案
# 限制：假设k是上一个状态，即f[i-1][k]，那么j&k 必须== 0（j和k不能在同一行都有1）
# 限制：每一列所有连续空着的位置的长度必须是偶数
# 本题中摆满(nxm)棋盘的方案为f[m][0]：前m-1列已经摆好，且从第m-1列伸出到第m列的状态是0，即没有任何伸出

# 状态计算：（化整为零）
# f[i][j] = f[i-1][k] for k in range(2^11)
# 时间复杂度：11x2^11x2^11（四千万）

class Solution:
    def Mendelian(self, n, m):
        st = [True for i in range(1 << n)]
        if n | m:  # n||m
            for i in range(1 << n):
                cnt = 0
                for j in range(n):
                    if (i >> j) & 1:
                        if cnt & 1: st[i] = False
                        cnt = 0
                    else:
                        cnt += 1
                if cnt & 1: st[i] = False

            # 初始化dp数组
            dp = [[0 for i in range(1 << n)] for j in range(m + 1)]
            dp[0][0] = 1

            # 状态计算
            for i in range(1, m + 1):
                for j in range(0, 1 << n):
                    for k in range(0, 1 << n):
                        if ((j & k) == 0) and st[j | k]:
                            dp[i][j] += dp[i - 1][k]
            return dp[m][0]
        pass

if __name__ == '__main__':
    solution = Solution()
    res = []
    while(1):
        a, b = list(map(int, input().split()))
        if a==0 and b==0:
            break
        else:
            res.append(solution.Mendelian(a, b))

    for i in res:
        print(i)
