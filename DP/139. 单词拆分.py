#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/9
'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

'''
from typing import List
# 动态规划
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         num = len(s)
#         memory = [False for _ in range(num+1)]
#         memory[0] = True
#         for i in range(num):
#             for j in range(i+1, num+1):
#                 if memory[i] and s[i: j] in wordDict:
#                     memory[j] = True
#         return memory[num]
pass

# 记忆化递归
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         num = len(s)
#         import functools
#         @functools.lru_cache(None)
#         def back_track(tmp_s):
#             res = False
#             if tmp_s == '':
#                 return True
#             for i in range(1, num+1):
#                 if tmp_s[:i] in wordDict:
#                     res = (back_track(tmp_s[i:]) or res)
#             return res
#
#         return back_track(s)








class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        num = len(s)
        # 记忆化功能
        #
        import functools
        #
        @functools.lru_cache(None)
        def back_track(tmp_s):
            if not(tmp_s):
                return True
            res = False
            for i in range(1, num+1):
                if tmp_s[:i] in wordDict:
                    res = back_track(tmp_s[i:]) or res
            return res

        return back_track(s)

solution = Solution()
res = solution.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"])
print(res)