#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/15
'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
通过次数18,423提交次数44,615
'''
# 方法：动态规划
# 我认为要执行两次动态规划：从前往后扫和从后往前扫描
# 状态表示：dp[i][j]表示到第i行第j列为止，a[i][j]距离四个方向的0的距离   属性：min
# 状态计算：从前往后： dp[i][j] = min(dp[i-1][j], dp[i][j-1]) if a[i][j]==1 else 0
#          从后往前： dp[i][j] = min(dp[i+1][j], dp[i][j+1]) if a[i][j]==1 else 0

from typing import List
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 上下左右各填一行，防止边界溢出
        dp = [[999999 for _ in range(len(matrix[0])+2)] for _ in range(len(matrix)+2)]

        # 从上到下，从左到右
        for i in range(1, len(dp)-1):
            for j in range(1, len(dp[0])-1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
                elif matrix[i-1][j-1] == 0:
                    dp[i][j] = 0

        # 从下到上，从右到左
        for i in range(len(dp)-2, 0, -1):
            for j in range(len(dp[0])-2, 0, -1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i][j], min(dp[i+1][j], dp[i][j+1])+1)
                elif matrix[i-1][j-1] == 0:
                    dp[i][j] = 0
        res = []
        for i in range(1, len(dp)-1):
            tmp = []
            for j in range(1, len(dp[0])-1):
                tmp.append(dp[i][j])
            res.append(tmp[:])

        return res

if __name__ == '__main__':
    solution = Solution()
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = solution.updateMatrix(matrix)
    print(res)