#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/9
'''
给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。

学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。

学生必须坐在状况良好的座位上。



示例 1：



输入：seats = [["#",".","#","#",".","#"],
              [".","#","#","#","#","."],
              ["#",".","#","#",".","#"]]
输出：4
解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。
示例 2：

输入：seats = [[".","#"],
              ["#","#"],
              ["#","."],
              ["#","#"],
              [".","#"]]
输出：3
解释：让所有学生坐在可用的座位上。
示例 3：

输入：seats = [["#",".",".",".","#"],
              [".","#",".","#","."],
              [".",".","#",".","."],
              [".","#",".","#","."],
              ["#",".",".",".","#"]]
输出：10
解释：让学生坐在第 1、3 和 5 列的可用座位上。


提示：

seats 只包含字符 '.' 和'#'
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8
'''

# 思考：首先可以用DFS
from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        # 如果当前位置被占了，用*表示
        self.res = 0

        def could_place(row, col):
            # if row < len(seats)-1:
                # if seats[row-1] ==
            pass

        def place_queen(row, col):
            tmp = seats[row][col]
            seats[row][col] = '*'
            return tmp

        def remove_queen(row, col, tmp):
            seats[row][col] = tmp


        def backtrack(row=0, tmp_res=0, path=[]):
            if row == len(seats):
                self.res = max(self.res, tmp_res)
                return
            for col in range(len(seats[row])):
                if could_place(row, col):
                    tmp = place_queen(row, col)
                    backtrack(row + 1, tmp_res+1, path)
                    remove_queen(row, col, tmp)
        backtrack(0, 0, seats)
        return self.res

solution = Solution()
solution.maxStudents([["#",".","#","#",".","#"],
              [".","#","#","#","#","."],
              ["#",".","#","#",".","#"]])