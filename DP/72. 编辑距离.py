#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/12
'''
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
'''
import functools
# class Solution:
#     @functools.lru_cache(None)
#     def minDistance(self, word1: str, word2: str) -> int:
#         if not word1 or not word2:
#             return len(word1) + len(word2)
#         if word1[0] == word2[0]:
#             return self.minDistance(word1[1:], word2[1:])
#         else:
#             inserted = 1 + self.minDistance(word1, word2[1:])
#             deleted = 1 + self.minDistance(word1[1:], word2)
#             replace = 1 + self.minDistance(word1[1:], word2[1:])
#             return min(inserted, deleted, replace)

# 字符串切片是o(n)，故改成索引号
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1

        return helper(0, 0)
