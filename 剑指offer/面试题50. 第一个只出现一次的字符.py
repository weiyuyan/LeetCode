#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/3
'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "

限制：

0 <= s 的长度 <= 50000
'''
# 思路：哈希表用作辅助空间
class Solution:
    def firstUniqChar(self, s: str) -> str:
        hash_dict = {}
        for char in s:
            if char in hash_dict:
                hash_dict[char]+=1
            else:
                hash_dict[char]=1
        for char in s:
            if hash_dict[char]==1: return char
        return ' '

solution = Solution()
s = 'abaccdeff'
res = solution.firstUniqChar(s)
print(res)