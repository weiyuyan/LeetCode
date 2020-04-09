#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/9
'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''
# 回溯法
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res = []
        self.back_track(0, [], 0, 0)
        return self.res

    def back_track(self, depth: int, res: List[str], left: int, right: int):
        if depth>=self.n*2:
            if left==self.n and right==self.n:
                self.res.append(''.join(res))
                return
            else:
                return
        if right>left or right>self.n or left>self.n:
            return
        else:
            res.append('(')
            self.back_track(depth+1, res, left+1, right)
            res.pop()
            res.append(')')
            self.back_track(depth+1, res, left, right+1)
            res.pop()

if __name__ == '__main__':
    solution = Solution()
    n = 3
    res = solution.generateParenthesis(n)
    print(res)



