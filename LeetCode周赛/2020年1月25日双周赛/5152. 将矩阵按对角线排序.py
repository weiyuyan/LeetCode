#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/25
'''
给你一个 m * n 的整数矩阵 mat ，请你将同一条对角线上的元素（从左上到右下）按升序排序后，返回排好序的矩阵。
输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]


提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
'''

from typing import List
class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            return []
        col = len(matrix)
        row = len(matrix[0])
        nums = col * row
        m = n = 0
        flag = True
        res = []
        for i in range(nums):
            res.append(matrix[m][n])
            if flag:
                m -= 1
                n += 1
            else:
                m += 1
                n -= 1
            if m >= col:
                m -= 1
                n += 2
                flag = True
            elif n >= row:
                m += 2
                n -= 1
                flag = False
            if m < 0:
                m = 0
                flag = False
            elif n < 0:
                n = 0
                flag = True
        return res

solution = Solution()
res = solution.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])