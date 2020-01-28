#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/26
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''

# DFS
from typing import List
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         def dfs(digits, d, l, cur, ans):
#             if l == len(digits):
#                 if l>0: ans.append("".join(cur))
#                 return
#             for c in d[ord(digits[l]) - ord('0')]:
#                 cur[l] = c
#                 dfs(digits, d, l+1, cur, ans)
#         d = [" ", "", "abc", "def", "ghi", "jkl",
#              "mno", "pqrs", "tuv","wxyz"]
#         cur = [' ' for _ in range(len(digits))]
#         ans = []
#         dfs(digits, d, 0, cur, ans)
#         return ans

# BFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno",
             "pqrs", "tuv", "wxyz"]
        ans = [""]
        for digit in digits:
            tmp = []
            for s in ans:
                for c in d[ord(digit) - ord('0')]:
                    tmp.append(s+c)
            ans = tmp
        return ans

solution = Solution()
res = solution.letterCombinations('23')
print(res)