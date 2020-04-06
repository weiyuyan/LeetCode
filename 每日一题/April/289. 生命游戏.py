#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/4
'''
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

 

示例：

输入：
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
 

进阶：

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？

'''
from typing import List

# 方法一：遍历数组的每个元素进行判断
# 为了避免边界问题，先将上下左右各扩展一维
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        _board = [[0 for _ in range(len(board[0])+2)] for _  in range(len(board)+2)]
        for i in range(1, len(_board)-1):
            for j in range(1, len(_board[0])-1):
                _board[i][j] = board[i-1][j-1]

        for i in range(1, len(_board)-1):
            for j in range(1, len(_board[0])-1):
                tmp = 0
                # 周围8个方向
                if _board[i - 1][j] == 1: tmp += 1
                if _board[i + 1][j] == 1: tmp += 1
                if _board[i][j - 1] == 1: tmp += 1
                if _board[i][j + 1] == 1: tmp += 1
                if _board[i - 1][j - 1] == 1: tmp += 1
                if _board[i - 1][j + 1] == 1: tmp += 1
                if _board[i + 1][j - 1] == 1: tmp += 1
                if _board[i + 1][j + 1] == 1: tmp += 1

                if _board[i][j] == 1:
                    # 活细胞
                    if tmp<2 or tmp>3: board[i-1][j-1] = 0
                if _board[i][j] == 0:
                    # 死细胞
                    if tmp==3:
                        board[i-1][j-1] = 1


if __name__ == '__main__':
    solution = Solution()
    arr = [[]]
    solution.gameOfLife(arr)
    print(arr)
