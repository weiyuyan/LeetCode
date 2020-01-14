#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/14

'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        q = 0
        if (needle==''):
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[q]:
                for j in range(len(needle)):
                    if i+j >= len(haystack):
                        return -1
                    if (haystack[i+j]==needle[j]):
                        pass
                        if j == len(needle) - 1:
                            return i
                    else:
                        break
            else:
                pass
        return -1

if __name__ == '__main__':
    haystack = ""
    needle = "123"
    solution = Solution()
    i = solution.strStr(haystack, needle)
    print(i)

