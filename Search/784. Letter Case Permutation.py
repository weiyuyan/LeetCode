#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/29
'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. 
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

'''
from typing import List
# class Solution:
#     def letterCasePermutation(self, S: str) -> List[str]:
#         number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#         res = []
#         def track_back(tmp_repository: str, tmp_res: str):
#             if len(tmp_repository) == 0:
#                 res.append(tmp_res[:])
#                 return
#             if tmp_repository[0] not in number:
#                 track_back(tmp_repository[1:], tmp_res+tmp_repository[0].lower())
#                 track_back(tmp_repository[1:], tmp_res+tmp_repository[0].upper())
#             else:
#                 track_back(tmp_repository[1:], tmp_res + tmp_repository[0])
#         track_back(S, '')
#         return res

# class Solution:
#     def letterCasePermutation(self, S: str) -> List[str]:
#         res = [S]
#         tmp_res = []
#         for i, c in enumerate(S):
#             if c.isalpha():
#                 for s in res:
#                     tmp_res.append(s[:i] + s[i].swapcase()+s[i+1:])
#                 res.extend(tmp_res)
#             tmp_res = []
#         return res

# 上一程序的精简版
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                res.extend([s[:i]+s[i].swapcase()+s[i+1:] for s in res])
        return res


solution = Solution()
res = solution.letterCasePermutation('a1b2')
print(res)
