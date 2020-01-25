#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/25
'''
给你一个回文字符串 palindrome ，请你将其中 一个字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。

请你返回结果字符串。如果无法做到，则返回一个空串。



示例 1：

输入：palindrome = "abccba"
输出："aaccba"
示例 2：

输入：palindrome = "a"
输出：""

提示：

1 <= palindrome.length <= 1000
palindrome 只包含小写英文字母。
'''


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        for i in range(len(palindrome)):
            if palindrome[i] != 'a' and i != len(palindrome) // 2:
                new_palindrome = list(palindrome)
                new_palindrome[i] = 'a'
                return ''.join(new_palindrome)

        if len(palindrome)>1:
            new_palindrome = list(palindrome)
            new_palindrome[-1] = 'b'
            return ''.join(new_palindrome)

        return ''

if __name__ == '__main__':
    palindrome = "aba"
    solution = Solution()
    a = solution.breakPalindrome(palindrome)
    print(a)