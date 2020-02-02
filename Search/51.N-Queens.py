#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/1
'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

'''
from typing import List
# 又不会了，草！（一种植物）
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#
#         all_res = []
#
#         # 首先维护一个used表, True表示可以使用，False表示不可以使用
#         used = [[True for _ in range(n)] for _ in range(n)]
#         print(used)
#
#         # 构建棋盘
#         chess_res = [['.' for _ in range(n)] for _ in range(n)]
#         # print(chess_res)
#         # print(sum(used[0]))
#
#         # 回溯函数
#         def _back_track(depth, used: List[List[bool]], chess_res: List[List[str]]):
#             if depth == n:
#                 all_res.append(chess_res[:])
#                 return
#             # 在该行平行寻找
#             for i in range(n):
#                 if used[depth][i]:
#                     tmp = used[:]  # 纪录临时状态
#                     # 如果有可行解，改变used[depth][i]行、列及斜边状态
#                     # i是列，depth是行
#                     # 改变行
#                     used[depth] = [False for _ in range(n)]
#                     # 改变列
#                     for _ in range(n):
#                         used[_][i] = False
#                     # 改变左斜
#                     pass
#                     for j in range(min(depth, n-1))
#                     #改变右斜
#                     pass
#
#                     pass

# LeetCode官方的
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         def could_place(row, col):
#             return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
#
#         def place_queen(row, col):
#             queens.add((row, col))
#             cols[col] = 1
#             hill_diagonals[row - col] = 1
#             dale_diagonals[row + col] = 1
#
#         def remove_queen(row, col):
#             queens.remove((row, col))
#             cols[col] = 0
#             hill_diagonals[row - col] = 0
#             dale_diagonals[row + col] = 0
#
#         def add_solution():
#             solution = []
#             for _, col in sorted(queens):
#                 solution.append('.' * col + 'Q' + '.' * (n - col - 1))
#             output.append(solution)
#
#         def backtrack(row=0):
#             for col in range(n):
#                 if could_place(row, col):
#                     place_queen(row, col)
#                     if row + 1 == n:
#                         add_solution()
#                     else:
#                         backtrack(row + 1)
#                     remove_queen(row, col)
#
#         cols = [0] * n
#         hill_diagonals = [0] * (2 * n - 1)
#         dale_diagonals = [0] * (2 * n - 1)
#         queens = set()
#         output = []
#         backtrack()
#         return output

# 看了花花的视频自己写一个
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.board = ['' for _ in range(n)]
        # 行变量不用设置，有for循环
        # 只需要设置列变量和主(hill)副(dale)对角线标量
        col = [True for _ in range(n)]
        hill_diagonals = [True for _ in range(2*n-1)]
        dale_diagonals = [True for _ in range(2*n-1)]
        solve = []

        def _updateBoard(x: int, y: int, update: bool):
            '''
            更新board棋盘，如果update是True那就更新（置False），如果update是False就取消更新（置True）
            :param x: 行坐标
            :param y: 列坐标
            :param update: 是否更新，即添置新元素，True为是，False为撤回添加元素
            :return:
            '''
            if update:
                col[y] = False
                hill_diagonals[x+y] = False
                dale_diagonals[y-x+n-1] = False
                # board[x][y] = 'Q'
                self.board[x] += '.' * x + 'Q' + '.' * (n-x-1)
            else:
                col[y] = True
                hill_diagonals[x+y] = True
                dale_diagonals[y-x+n-1] = True
                # board[x][y] = '.'
                self.board[x] += ''
        def _back_track(depth: int):
            '''
            回溯函数
            :param depth:  当前深度
            :return:
            '''
            if depth == n:  # 满足条件、退出
                solve.append(self.board[:])
                self.board = ['' for _ in range(n)]
                return
            for y in range(n):
                if col[y] and hill_diagonals[y+depth] and dale_diagonals[depth-y+n-1]:
                    _updateBoard(depth, y, update=True)
                    _back_track(depth+1)
                    _updateBoard(y, depth, update=False)
        _back_track(0)
        return solve





if __name__ == '__main__':
    solution = Solution()
    output = solution.solveNQueens(4)
    print(output)