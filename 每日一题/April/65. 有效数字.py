#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/7
'''
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。

更新于 2015-02-10:
C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。

通过次数11,441提交次数60,683
'''
# 正则表达式法
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r'\s*[+-]?([\d]+(\.[\d]*)?|\.[\d]+)(e[+-]?[\d]+)? *$', s))


class Automaton:
    def __init__(self):
        self.state = 'start'
        # 从目前来看一共有七个状态，6种输入情况
        # 状态：start、signed、pre_e_number、after_e_number、pre_dot_number、after_dot_number、end
        # 输入情况：①' '    ②+/-    ③ 'e'    ④ '.'    ⑤ number    ⑥ other
        self.table = {
            'start': ['start', 'signed', 'end', 'after_dot_number', 'pre_e_number', 'end'],
            'signed': ['end', 'end', 'end', 'after_dot_number', 'pre_e_number', 'end'],
            'pre_e_number': ['end', 'end', 'after_e_number', 'after_dot_number', 'pre_e_number', 'end'],
            'after_e_number': ['end', 'end', 'end', 'end', 'after_e_number', 'end'],
            'pre_dot_number': ['end', 'end', 'after_e_number', 'after_dot_number', 'pre_dot_number', 'end'],
            'after_dot_number': ['end', 'end', 'after_e_number', 'end', 'after_dot_number', 'end'],
            'end': []
        }

    def get_state(self, c: str):
        if c == ' ': return 0
        if c == '+' or c == '-': return 1
        if c == 'e': return 2
        if c == '.': return 3
        if c.isdigit(): return 4
        else: return 5

    def get(self, c: str):
        stat = self.get_state(c)
        self.state = self.table[self.state][stat]
        return self.state

class Solution:
    def isNumber(self, s: str) -> bool:
        automaton = Automaton()
        s = s.strip()
        if '.e' in s:return False
        if s in ['.', 'e', '+', '-', '']: return False
        if s[-1] in ['e', '+', '-']: return False
        for char in s:
            state = automaton.get(char)
            if state == 'end':
                return False
            # if state == 'after_e_number' and automaton.pre_e_number == 0:
            #     return False
        return True

if __name__ == '__main__':
    solution = Solution()
    s = '.e1'
    res = solution.isNumber(s)
    print(res)