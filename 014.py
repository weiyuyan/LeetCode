#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/4
'''
Title: 最长公共子串
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
'''
from typing import List
class Solution:
    '''
    其思想是使用Python自带的min max函数对字符串取最大最小值，
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    '''
    利用python的zip函数，把str看成list然后把输入看成二维数组，
    左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
    '''
    def longestCommonPrefix2(self, strs):
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

if __name__ == '__main__':
    solution = Solution()
    result = solution.longestCommonPrefix2(["flower","flowg","flight"])
    print(result)