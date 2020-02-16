#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/15
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
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

注意：本题与主站 65 题相同：https://leetcode-cn.com/problems/valid-number/

'''

'''
class Solution:
    def isNumber(self, s: str) -> bool:
        # 删去空格
        s = s.strip()

        # 是空则返回False
        if s == '': return False

        # 有无其他特殊字符
        repository = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e', 'E', '+', '-', '.']
        for str in s:
            if str not in repository:   return False

        # 将数字整体分为[A][.[B]][e|E][C]
        A, B, C = '', '', ''    # 初始化ABC
        A_B_C = s.split('e') if 'e' in s else s.split('E')
        if len(A_B_C) == 2: # 说明有e|E，A_B和C都有，但也有可能是空''
            if not A_B_C[0] or not A_B_C[1]: return False   # 如果有空元素，如 1e  e34  e  等    'e'切分的结果是['', '']
            A_B = A_B_C[0]
            C = A_B_C[1]
            # 将A、B划分出来
            A_B = A_B.split('.')
            if len(A_B) == 2:   # 说明有小数点
                A = A_B[0]
                B = A_B[1]
            if len(A_B) == 1:   # 说明没有小数点或者有小数点但没有整数 3、 .45     # 特殊：23. 怎么处理  .+1怎么处理
                if A_B_C[0][-1] == '.': return False    # 特殊：如23.
                if A_B_C[0][0] == '.': # 第一位是小数点.
                    B = A_B[0]  # 这个是小数位
                else:
                    A = A_B[0]  # 这个是整数位
            else: return False  # A_B里有不止一个小数点，返回False

        elif len(A_B_C) == 1: # 说明只有A_B或者只有C  如1.23   1.23e   e897
            A_B = A_B_C[0]
            # 将A、B划分出来
            A_B = A_B.split('.')
            if len(A_B) == 2:  # 说明有小数点或者有小数点但没有整数或小数或都没有 3. .45  .   # 特殊：23. 怎么处理  .+1怎么处理
                A = A_B[0]
                B = A_B[1]
                if not A and not B: return False
            elif len(A_B) == 1:  # 说明没有小数点
                if A_B_C[0][-1] == '.': return False  # 特殊：如23.
                if A_B_C[0][0] == '.':  # 第一位是小数点.
                    B = A_B[0]  # 这个是小数位
                else:
                    A = A_B[0]  # 这个是整数位
            else: return False    # 说明小数点>=3

        else: return False # 说明不止一个e|E，返回False


        # 下面开始写A、B和C的规则
        # A是整数部分，B是小数部分，C是e|E后面的整数部分

        # A（整数）的规则
        if A and ('+' in A[1:] or '-' in A[1:]): return False    # 如果含有多个正负号，返回False
        if len(A) == 1 and ('+' in A or '-' in A) and not B:  return False    # 只有符号，没有数字

        # B的规则
        if B and ('+' in B or '-' in B): return False  # 小数点里不能有正负号

        # C的规则
        if C and ('+' in C or '-' in C or '.' in C):  return False    # C里不可以有符号，只能是纯整数

        return True # 呼。。。


# 太他妈南了，我吐了！
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                if i > 0 and s[i-1] != 'e' or 'E':
                    return False
            elif char == '.':
                if met_dot or met_e: return False
                met_dot = True
            elif char == 'e' or 'E':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False # e后必须接，所以这时重置met_digit为False,以免e为最后一个char
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

import re
class Solution:
    p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
    def isNumber(self, s: str) -> bool:
        return bool(self.p.match(s.strip()))


solution = Solution()
res = solution.isNumber("0")
print(res)