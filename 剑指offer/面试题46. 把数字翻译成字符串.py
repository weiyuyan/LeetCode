#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/26
'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25
翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：

0 <= num < 231
'''
# class Solution:
#     def translateNum(self, num: int) -> int:
#         # 先将其转换成字符串
#         char_num = str(num)
#         self.res = 0
#         self.back_track(char_num)
#         return self.res
#
#     def back_track(self, cur: str):
#         #递归结束条件
#         if len(cur) <= 1:
#             self.res += 1
#             return
#         self.back_track(cur[1:])
#         if int(cur[0]+cur[1]) < 26 and cur[0]!='0':
#             self.back_track(cur[2:])
pass

# 解法二，利用python的记忆化递归装饰器
# P.S.解法二貌似有点问题，这个装饰器好像有bug
'''
import functools
class Solution:
    def translateNum(self, num: int) -> int:
        # 先将其转换成字符串
        char_num = str(num)
        self.res = 0
        self.back_track(char_num)
        return self.res

    @functools.lru_cache(None)
    def back_track(self, cur: str):
        #递归结束条件
        if len(cur) <= 1:
            self.res += 1
            return
        self.back_track(cur[1:])
        if int(cur[0]+cur[1]) < 26 and cur[0]!='0':
            self.back_track(cur[2:])
'''
pass

# 解法三：动态规划
class Solution:
    def translateNum(self, num: int) -> int:
        pass
        self.str_num = str(num)
        self.dp_num = len(self.str_num)
        self.dp = [1 for _ in range(self.dp_num+1)]
        for i in range(2, self.dp_num+1):
            if self.str_num[i]
    def dp(self, i):
solution = Solution()
res = solution.translateNum(220)
print(res)