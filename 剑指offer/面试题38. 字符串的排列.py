#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/20
'''
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 
限制：

1 <= s 的长度 <= 8

通过次数694提交次数1,295
'''
from typing import List

# 方法：使用递归
# class Solution:
#     def permutation(self, s: str) -> List[str]:
#         if not s: return []
#
#         self.res = []
#     def back_track(self, first: str, other: str, tmp_res: List[int]):
#         if not other:
#             self.res.append(tmp_res[:])
#             return
#
#         self.back_track(other[0], other[1:], tmp_res)
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return
        s=list(sorted(s))
        res=[]
        def helper(s,tmp):
            if not s: res.append(''.join(tmp))
            for i,char in enumerate(s):
                if i>0 and s[i]==s[i-1]:
                    continue
                helper(s[:i]+s[i+1:],tmp+[char])
        helper(s,[])
        return res

class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return
        s = list(sorted(s))
        res = []

        def helper(s, tmp):
            if not s: res.append(''.join(tmp))
            for i, char in enumerate(s):
                if i>0 and s[i]==s[i-1]:
                    continue
                helper(s[:i]+s[i+1:], tmp+[char])
        helper(s,[])
        return res


