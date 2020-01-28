#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/27
'''
请实现一个函数，把字符串中的每个空格替换成"%20"。

你可以假定输入字符串的长度最大是1000。
注意输出字符串的长度可能大于1000。

样例
输入："We are happy."

输出："We%20are%20happy."
'''
# 双指针法
class Solution(object):
    def replaceSpaces(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for char in s:
            if char == ' ':
                res += '%20'
            else:
                res += char
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.replaceSpaces('  ')
    print(res)