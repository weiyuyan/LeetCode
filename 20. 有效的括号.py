#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/12
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

'''
class Solution:
    def isValid(self, s: str) -> bool:
        symbol_list = ['(', ')', '[', ']', '{', '}']
        result = []
        for char in s:
            if char in symbol_list:
                if len(result) == 0:
                    result.append(char)
                elif char == ')' and result[-1] =='(':
                    result.pop(-1)
                elif char == ']' and result[-1] =='[':
                    result.pop(-1)
                elif char == '}' and result[-1] =='{':
                    result.pop(-1)
                else:
                    result.append(char)
        if len(result) == 0:
            return True
        else:
            return False
if __name__ == '__main__':
    solution = Solution()
    s = "()"
    result = solution.isValid(s)
    print(result)