#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/15
'''
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：

在同一行的所有元素中最小
在同一列的所有元素中最大


示例 1：

输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
示例 2：

输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
示例 3：

输入：matrix = [[7,8],[1,2]]
输出：[7]


提示：

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5
矩阵中的所有元素都是不同的
'''
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minList = []    # 存放每一行的最小值
        maxList = []    # 存放每一列的最大值
        res = []
        for i in matrix:
            min_num = i[0]
            for j in range(len(i)):
                min_num = min(min_num, i[j])
            minList.append(min_num)

        for i in range(len(matrix[0])):
            max_num = matrix[0][i]
            for j in range(len(matrix)):
                max_num = max(max_num, matrix[j][i])
            maxList.append(max_num)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == minList[i] and matrix[i][j] == maxList[j]:
                    res.append(matrix[i][j])
        return res

solution = Solution()
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
res = solution.luckyNumbers(matrix)
print(res)