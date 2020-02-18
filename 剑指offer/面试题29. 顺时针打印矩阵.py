#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/18
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
'''
from typing import List

# 我用的递归，思路错了，有点没考虑周全
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         flag = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#         print_list = []
#         self.back_track(0, 0, matrix, flag, print_list)
#         return print_list
#
#     def back_track(self, row: int, col: int, matrix: List[List[int]], flag: List[List[bool]], print_list: List[int]):
#         '''
#
#         :param row: 当前行
#         :param col: 当前列
#         :param matrix: 矩阵
#         :param flag: 标记点
#         :param print_list: 要输出的目标列表
#         :return:
#         '''
#         # 方向：右→下→左→上
#         if row<0 or row>=len(matrix) or col<0 or col>=len(matrix[0]) or flag[row][col]: return
#         print_list.append(matrix[row][col])
#         flag[row][col] = True
#         self.back_track(row, col+1, matrix, flag, print_list)
#         self.back_track(row+1, col, matrix, flag, print_list)
#         self.back_track(row, col-1, matrix, flag, print_list)
#         self.back_track(row-1, col, matrix, flag, print_list)


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []    # 排除特殊情况

        row, col = len(matrix), len(matrix[0])
        res = []

        flag = [[False for _ in range(col)] for _ in range(row)]
        direction_row = [-1, 0, 1, 0]  # 上右下左
        direction_col = [0 ,1, 0, -1]  # 上右下左

        x = 0; y= 0; direction = 1  # direction 的0,1,2,3分别代表上右下左四个方向。初始方向是向右

        for i in range(row*col):
            # 该点可以打印，flag置True
            res.append(matrix[x][y])
            flag[x][y] = True
            a = x + direction_row[direction]
            b = y + direction_col[direction]
            if a < 0 or a >= row or b < 0 or b >= col or flag[a][b]:
                direction = (direction+1) % 4   # 转变方向
                x += direction_row[direction]
                y += direction_col[direction]
                continue

            x += direction_row[direction]
            y += direction_col[direction]
        return res




solution = Solution()
matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res = solution.spiralOrder(matrix)
print(res)
