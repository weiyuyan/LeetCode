#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/10
'''
设有 N×N 的方格图，我们在其中的某些方格中填入正整数，而其它的方格中则放入数字0。如下图所示：

某人从图中的左上角 A 出发，可以向下行走，也可以向右行走，直到到达右下角的 B 点。

在走过的路上，他可以取走方格中的数（取走后的方格中将变为数字0）。

此人从 A 点到 B 点共走了两次，试找出两条这样的路径，使得取得的数字和为最大。

输入格式
第一行为一个整数N，表示 N×N 的方格图。

接下来的每行有三个整数，第一个为行号数，第二个为列号数，第三个为在该行、该列上所放的数。

一行“0 0 0”表示结束。

输出格式
输出一个整数，表示两条路径上取得的最大的和。

数据范围
N≤10
输入样例：
8
2 3 13
2 6 6
3 5 7
4 4 14
5 2 21
5 6 4
6 3 15
7 2 14
0 0 0
输出样例：
67
'''
# from typing import List
# class Solution:
#     def fangge(self, a: List[List[int]]):
#         dp = [[0] for _ in range(len(a[0])+1) for _ in range(len(a)+1)]
#         res = 0
#         for i in range(1, len(dp)):
#             for j in range(1, len(dp[0])):
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + a[i-1][j-1]
#
#         pass

# 走两次：
# f[i1][j1][i2][j2] 表示所有从(1,1)(1,1)分别走到(i1,j1)、(i2,j2)的路径的最大值
# 由于 i1+j1 == i2+j2
# 设k = i1+j1 = i2+j2
# f[k][i1][i2]: 表示所有从(1,1)(1,1)分别走到(i1,k-i1)、(i2,k-i2)的路径的最大值

# 状态计算：
# 按最后一步是向下还是向右走，状态一共可以分为4种：
# ①下    下   f[k-1][i1-1][i2-1] + (w[i1][j1])【if i1==i2 and j1==j2】 / + (w[i1][j1]+w[i2][j2])【if i1!=i2 or j1!=j2】
# ②下    右   f[k-1][i1-1][i2] + (w[i1][j1])【if i1==i2 and j1==j2】 / + (w[i1][j1]+w[i2][j2])【if i1!=i2 or j1!=j2】
# ③右    下   f[k-1][i1][i2-1] + (w[i1][j1])【if i1==i2 and j1==j2】 / + (w[i1][j1]+w[i2][j2])【if i1!=i2 or j1!=j2】
# ④右    右   f[k-1][i1][i2] + (w[i1][j1])【if i1==i2 and j1==j2】 / + (w[i1][j1]+w[i2][j2])【if i1!=i2 or j1!=j2】
# 最后，四者求一个max

from typing import List
class Solution:
    def fangge(self, array: List[List[int]]):
        res = 0
        dp = [[[0 for _ in range(len(array)+1)] for _ in range(len(array)+1)] for _ in range(len(array)*2+2)]

        for k in range(2, len(dp)):
            for i1 in range(1, len(dp[0])):
                for i2 in range(1, len(dp[0][0])):
                    j1 = k-i1
                    j2 = k-i2
                    if j1>=1 and j1<=len(array) and j2>=1 and j2<=len(array):
                        t = array[i1-1][j1-1]
                        if j1 != j2:
                            t += array[i2-1][j2-1]

                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2-1]+t)
                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2]+t)
                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2-1]+t)
                        dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2]+t)
                        res = max(res, dp[k][i1][i2])
        return res

if __name__ == '__main__':
    solution = Solution()
    N = int(input())
    array = [[0 for _ in range(N)] for _ in range(N)]
    while True:
        row, col, val = list(map(int, input().split()))
        if row==0 and col==0 and val==0: break
        array[row-1][col-1] = val

    res = solution.fangge(array)
    print(res)
