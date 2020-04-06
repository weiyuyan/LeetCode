#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/10
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
'''
from typing import List
class Solution:
    '''
    对于一个节点来说，它到 0 的距离可以通过邻居的最近距离计算，在这种情况下最近距离是邻居的距离 + 1。
因此，这就让我们想到了动态规划！
对于每个 1，到 0 的最短路径可能从任意方向。所以我们需要检查所有 4 个方向。在从上到下的迭代中，
我们需要检查左边和上方的最短路径；我们还需要另一个从下往上的循环，检查右边和下方的方向。

算法

从上至下、从左至右迭代整个矩阵：

更新

\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j-1],\text{dist}[i-1][j])+1)dist[i][j]=min(dist[i][j],min(dist[i][j−1],dist[i−1][j])+1)

最近距离考虑上方邻居和左侧邻居距离 + 1，这在前面的迭代中已经计算完成。

从下到上、从右至左迭代整个矩阵：

更新

\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j+1],\text{dist}[i+1][j])+1)dist[i][j]=min(dist[i][j],min(dist[i][j+1],dist[i+1][j])+1)

最近距离考虑下方邻居和右侧邻居距离 + 1，这在前面的迭代中已经计算完成
    '''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j]=1000000 if matrix[i][j]!=0 else 0

        # 从上→下，从左→右
        for i in range(len(res)):
            for j in range(len(res[0])):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j], matrix[i-1][j], matrix[i+1][j],
                                       matrix[i][j-1], matrix[i][j+1])+1

        # 从下→上，从右→左
        for i in range(len(res)-1, -1, -1):
            for j in range(len(res[0])-1, -1, -1):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j], matrix[i-1][j], matrix[i+1][j],
                                       matrix[i][j-1], matrix[i][j+1])+1


        print(res)
solution = Solution()
matrix = [[0, 1, 2, 3], [3, 4, 5, 6]]
solution.updateMatrix(matrix)