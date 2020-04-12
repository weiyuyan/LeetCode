#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/11
'''
小渊和小轩是好朋友也是同班同学，他们在一起总有谈不完的话题。

一次素质拓展活动中，班上同学安排坐成一个 m 行 n 列的矩阵，而小渊和小轩被安排在矩阵对角线的两端，因此，他们就无法直接交谈了。

幸运的是，他们可以通过传纸条来进行交流。

纸条要经由许多同学传到对方手里，小渊坐在矩阵的左上角，坐标(1,1)，小轩坐在矩阵的右下角，坐标(m,n)。

从小渊传到小轩的纸条只可以向下或者向右传递，从小轩传给小渊的纸条只可以向上或者向左传递。 

在活动进行中，小渊希望给小轩传递一张纸条，同时希望小轩给他回复。

班里每个同学都可以帮他们传递，但只会帮他们一次，也就是说如果此人在小渊递给小轩纸条的时候帮忙，那么在小轩递给小渊的时候就不会再帮忙，反之亦然。 

还有一件事情需要注意，全班每个同学愿意帮忙的好感度有高有低（注意：小渊和小轩的好心程度没有定义，输入时用0表示），可以用一个0-100的自然数来表示，数越大表示越好心。

小渊和小轩希望尽可能找好心程度高的同学来帮忙传纸条，即找到来回两条传递路径，使得这两条路径上同学的好心程度之和最大。

现在，请你帮助小渊和小轩找到这样的两条路径。

输入格式
第一行有2个用空格隔开的整数 m 和 n，表示学生矩阵有 m 行 n 列。

接下来的 m 行是一个 m∗n 的矩阵，矩阵中第 i 行 j 列的整数表示坐在第 i 行 j 列的学生的好心程度，每行的 n 个整数之间用空格隔开。

输出格式
输出一个整数，表示来回两条路上参与传递纸条的学生的好心程度之和的最大值。

数据范围
1≤n,m≤50
输入样例：
3 3
0 3 9
2 8 5
5 7 0
输出样例：
34
'''
from typing import List
class Solution:
    def paper(self, student: List[List[int]]):
        res = 0
        dp = [[[0 for _ in range(len(student)+1)] for _ in range(len(student)+1)]\
              for _ in range(len(student)*2 + 2)]

        for k in range(1, len(dp)):
            for i1 in range(1, len(dp[0])):
                for i2 in range(1, len(dp[0][0])):
                    j1 = k-i1
                    j2 = k-i2
                    if j1>=1 and j1<=len(student[0]) and j2>=1 and j2<=len(student[0]):
                        t = student[i1-1][j1-1]
                        if i1 != i2:
                            t += student[i2-1][j2-1]

                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2-1]+t)
                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2-1]+t)
                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2]+t)
                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2]+t)
                        res = max(res, dp[k][i1][i2])
        return res

        # res = 0
        # dp = [[[0 for _ in range(len(array)+1)] for _ in range(len(array)+1)] for _ in range(len(array)*2+2)]
        #
        # for k in range(1, len(dp)):
        #     for i1 in range(1, len(dp[0])):
        #         for i2 in range(1, len(dp[0][0])):
        #             j1 = k-i1
        #             j2 = k-i2
        #             if j1>=1 and j1<=len(array) and j2>=1 and j2<=len(array):
        #                 t = array[i1-1][j1-1]
        #                 if j1 != j2:
        #                     t += array[i2-1][j2-1]
        #
        #                 dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2-1]+t)
        #                 dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2]+t)
        #                 dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2-1]+t)
        #                 dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2]+t)
        #                 res = max(res, dp[k][i1][i2])
        # return res

if __name__ == '__main__':
    solution = Solution()
    row, col = list(map(int, input().split()))
    arr = [[0 for _ in range(col+1)]]
    for i in range(row):
        arr.append([0]+list(map(int, input().split())))
    res = solution.paper(arr)
    print(res)