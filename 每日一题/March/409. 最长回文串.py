#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/3
'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        a_dict = {}
        res = 0
        for char in s:
            if char in a_dict:
                a_dict[char] += 1
            else:
                a_dict[char] = 1
        for key in a_dict.keys():
            res += a_dict[key]//2 * 2

        return res if res==len(s) else res+1

if __name__ == '__main__':
    s = "ccc"
    solution = Solution()
    res = solution.longestPalindrome(s)
    print(res)

