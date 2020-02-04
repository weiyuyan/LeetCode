#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/2
'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

'''

from typing import List

class Solution:
    # 回溯法 + 前缀树
    # 我们把所有单词构造成前缀树
    # 再遍历 board 用DFS分别在前缀树上跑
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w, {})
            t["end"] = 1
        # print(trie)

        res = []
        row = len(board)
        col = len(board[0])
        def dfs(i, j, trie, s):
            c = board[i][j]
            if c not in trie: return
            trie = trie[c]
            if "end" in trie and trie["end"] == 1:
                res.append(s+c)
                trie['end'] = 0
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != "#":
                    dfs(tmp_i, tmp_j, trie, s + c)
            board[i][j] = c
        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res


if __name__ == '__main__':
    solution = Solution()
    board =\
[
  ['A','A','C','E'],
  ['Z','A','C','S'],
  ['B','D','E','E']
]
    word = ['AAD', '123']
    res = solution.findWords(board, word)
    print(res)