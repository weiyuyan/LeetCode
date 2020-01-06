#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/6

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {'1': '',
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z'],
                    '0': '',
                    }
        output = []
        def backtrack(tmp_result, digits):
            if len(digits) == 0:
                output.append(tmp_result)
            else:
                for letter in num_dict[digits[0]]:
                    backtrack(tmp_result + letter, digits[1:])
        if digits:
            backtrack('', digits)
        return output

if __name__ == '__main__':
    solution = Solution()
    result = solution.letterCombinations('23')
    print(result)



