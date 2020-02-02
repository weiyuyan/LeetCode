#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/1
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''
from typing import List

class Solution:
    # 回溯法
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_char = len(word)
        # 引入used来剪枝
        def back_track(x, y, d):
            if not out_of_bound(x, y): return False
            if word[d] != board[y][x]: return False

            if d == num_char-1: return True

            # 复原现场
            board[y][x] = 0
            found = back_track(x-1, y, d+1) \
                   or back_track(x+1, y, d+1) \
                   or back_track(x, y-1, d + 1) \
                   or back_track(x, y+1, d + 1)
            board[y][x] = word[d]
            return found

        def out_of_bound(x, y):
            if y >= len(board) or y < 0 or x >= len(board[y]) or x < 0:
                return False
            else:
                return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if back_track(j, i, 0): return True
        return False

if __name__ == '__main__':
    solution = Solution()
    board =\
[
  ['A','A','C','E'],
  ['Z','A','C','S'],
  ['B','D','E','E']
]
    word = "AAD"
    res = solution.exist(board, word)
    print(res)

