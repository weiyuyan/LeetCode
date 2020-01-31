#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/31
'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

测试用例形式：
[
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
'''
from typing import List
# 核心思路：搜索+剪枝+回溯
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#
#         def _back_track(row=0, column=0):
#             '''
#             回溯函数
#             :param row: row表示行
#             :param column: column表示列
#             :return:
#             '''

NUM = [str(x) for x in range(1, 10)]
class Solution:
    def solveSudoku(self, in_board: list) -> None:
        pre = self.file_the_singlesolu_hole(in_board) # 把能填的先填上减少回溯
        # 新建可用列表
        avaliable_row = [set(str(x) for x in range(1, 10)) for _ in range(9)]
        avaliable_col = [set(str(x) for x in range(1, 10)) for _ in range(9)]
        avaliable_cube = [set(str(x) for x in range(1, 10)) for _ in range(9)]
        empty_hole = [(i, j) for i in range(9) for j in range(9) if in_board[i][j] == '.']  # local to file
        for i in range(9):  # 更新可用列表
            for j in range(9):
                if in_board[i][j] != '.':
                    avaliable_row[i].remove(in_board[i][j])
                    avaliable_col[j].remove(in_board[i][j])
                    avaliable_cube[(i//3)*3+j//3].remove(in_board[i][j])
        def getback(times):  # 填充次数等于洞洞长度就是整完了，返回
            if times == len(empty_hole):
                return True
            i, j = empty_hole[times]
            for to_file in avaliable_row[i] & avaliable_col[j] & avaliable_cube[(i//3)*3+j//3]:
                avaliable_row[i].remove(to_file)
                avaliable_col[j].remove(to_file)
                avaliable_cube[(i//3)*3+j//3].remove(to_file)
                in_board[i][j] = to_file
                if getback(times+1):
                    return True
                # 回溯
                avaliable_row[i].add(to_file)
                avaliable_col[j].add(to_file)
                avaliable_cube[(i//3)*3+j//3].add(to_file)
            return False

        getback(0)

    # 这段是真你妈强，作者的思路和代码能力，，厉害！
    def file_the_singlesolu_hole(self, in_board: list):  # 把能填的填上,直到需要猜
        temp = 81
        while True:
            num_of_black = 0    # 黑盒，这里只不确定位置的数量
            for i in range(len(in_board)):
                for j in range(len(in_board[0])):
                    if in_board[i][j] == '.':
                        solut = self.get_solu(i, j, in_board)
                        if len(solut) == 1:
                            in_board[i][j] = solut[0]   # 只有一个选择，那就直接放进去
                        else: num_of_black += 1
            if num_of_black < temp: temp = num_of_black
            else: break
        return True

    def get_solu(self, i, j, in_board):  # 给一个坐标，得到该点可能的解
        row = [x for x in in_board[i] if x != '.']
        # 这里zip函数将这个矩阵按列排开，很灵性，可以想象一把菜刀将几颗并排的葱切断
        # 思考：话说矩阵转置的话用这种方法正合适
        clo = [x for x in list(zip(*in_board))[j] if x != '.']
        # 这里两个for循环，类似这样
        # for m in range(3):
        #     for n in range(3):
        cube = [in_board[3*(i//3)+m][3*(j//3)+n] for m in range(3) for n in range(3)
                if in_board[3*(i//3)+m][3*(j//3)+n] != '.']
        # 这里*将列表解压为一个个元素，然后用一个元组合并
        return [x for x in NUM if x not in (*row, *clo, *cube)]
    # 这段代码绝了，真他妈强

    def sudoku_print(self, in_board: list):  # 用来打印
        for _ in in_board:
            print(_)

if __name__ == '__main__':
    solution = Solution()
    in_board = [
["5",".",".",".",".",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".",".",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".",".","1",".",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
    solution.solveSudoku(in_board)

    solution.sudoku_print(in_board)