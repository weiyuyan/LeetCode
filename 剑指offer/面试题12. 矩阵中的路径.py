#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/12
'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，
每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/

'''


class Solution(object):
    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(self.dfs(matrix, string, 0, i, j)):
                    return True
        return False


    def dfs(self, matrix, string, depth, x, y):
        if (matrix[x][y] != string[depth]):
            return False
        if (depth == len(string)-1):
            return True
        dx = [-1, 1, 0, 0]  # x的上下左右
        dy = [0, 0, -1, 1]  # y的上下左右
        temp = matrix[x][y]
        matrix[x][y] = '*'
        for i in range(4):
            _x = x+dx[i]
            _y = y+dy[i]
            if (_x>=0 and _x<len(matrix) and _y>=0 and _y<len(matrix[0])):
                if self.dfs(matrix, string, depth+1, _x, _y):   return True
        matrix[x][y] = temp
        return False
solution = Solution()
matrix=[
  ["A"]]

str="A"
res = solution.hasPath(matrix=matrix, string=str)
print(res)