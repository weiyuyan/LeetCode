#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/23
'''
给你一个整数数组 digits，你可以通过按任意顺序连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。

由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。

如果无法得到答案，请返回一个空字符串。

示例 1：

输入：digits = [8,1,9]
输出："981"
示例 2：

输入：digits = [8,6,7,1,0]
输出："8760"
示例 3：

输入：digits = [1]
输出：""
示例 4：

输入：digits = [0,0,0,0,0,0]
输出："0"

提示：

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
返回的结果不应包含不必要的前导零。
'''
from typing import List
# 真傻逼呀，我写的程序
# class Solution:
#     def largestMultipleOfThree(self, digits: List[int]) -> str:
#         res = ''
#
#         # 思考：统计每个数字各有多少个
#         count_digit = dict()
#         for digit in range(10): count_digit[digit] = 0  # 初始化全部为0
#         for digit in digits: count_digit[digit] += 1
#
#
#         # 统计完成后计算它们的总和，看能否被3整除
#         digits_sum = 0
#         for digit in count_digit.keys():
#             digits_sum += digit * count_digit[digit]
#
#         if digits_sum % 3 == 0:
#             pass
#
#         elif digits_sum % 3 == 1:
#             # 去掉一个1 或者一个4 或者一个7
#             if count_digit[1] >= 1: count_digit[1] -= 1
#             elif count_digit[4] >= 1: count_digit[4] -= 1
#             elif count_digit[7] >= 1: count_digit[7] -= 1
#
#             # 去掉两个2 或者一个5一个2 或者两个5 或者一个8一个2 或者一个8一个5 或者两个8
#             elif count_digit[2] >= 2: count_digit[2] -= 2
#             elif count_digit[2]>=1 and count_digit[5]>=1: count_digit[2]-=1; count_digit[5]-=1
#             elif count_digit[5] >= 2: count_digit[5] -= 2
#             elif count_digit[2]>=1 and count_digit[8]>=1: count_digit[2]-=1; count_digit[8]-=1
#             elif count_digit[5]>=1 and count_digit[8]>=1: count_digit[5]-=1; count_digit[8]-=1
#             elif count_digit[8] >= 2: count_digit[8] -= 2
#
#         elif digits_sum % 3 == 2:
#             # 去掉一个2 或者一个5 或者一个8
#             if count_digit[2] >= 1: count_digit[2] -= 1
#             elif count_digit[5] >= 1: count_digit[4] -= 1
#             elif count_digit[8] >= 1: count_digit[8] -= 1
#
#             # 去掉两个1 或者一个1一个4 或者两个4 或者一个7一个1 或者一个7一个4 或者两个7
#             elif count_digit[1] >= 2: count_digit[1] -= 2
#             elif count_digit[1]>=1 and count_digit[4]>=1: count_digit[1]-=1; count_digit[4]-=1
#             elif count_digit[4] >= 2: count_digit[4] -= 2
#             elif count_digit[1]>=1 and count_digit[7]>=1: count_digit[1]-=1; count_digit[7]-=1
#             elif count_digit[4]>=1 and count_digit[7]>=1: count_digit[4]-=1; count_digit[7]-=1
#             elif count_digit[7] >= 2: count_digit[7] -= 2
#
#         # 至此，讲道理字典中的数之和能被3整除了
#         # 如果还不行，那就返回''
#         digits_sum = 0
#         for digit in count_digit.keys(): digits_sum += digit * count_digit[digit]
#         if digits_sum % 3 != 0: return ''
#
#         # 至此，讲道理字典中的数之和能被3整除了
#         for i in range(9, -1, -1):
#             res += str(i)*count_digit[i]
#
#         if not res: return ''
#         if res[0] == '0': return '0'
#         return res


pass
# 膜拜一下大佬的写法
from typing import List
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        res = ''
        count_digit = dict()
        for digit in range(10): count_digit[digit] = 0  # 初始化全部为0
        for digit in digits: count_digit[digit] += 1

        digits_sum = 0
        for digit in count_digit.keys():
            digits_sum += digit * count_digit[digit]

        if digits_sum % 3 == 1:
            if(not self.delete(1, count_digit)): self.delete(2, count_digit); self.delete(2, count_digit)
        elif digits_sum % 3 == 2:
            if(not self.delete(2, count_digit)): self.delete(1, count_digit); self.delete(1, count_digit)

        for i in range(9, -1, -1):
            res += str(i)*count_digit[i]

        if not res: return ''
        if res[0] == '0': return '0'
        return res


    def delete(self, num: int, digit_dict: dict) -> bool:
        for i in range(num, 10, 3):
            if digit_dict[i] >= 1: digit_dict[i]-=1; return True
        return False



solution = Solution()
digits = [9,8,6,8,6]
res = solution.largestMultipleOfThree(digits)
print(res)