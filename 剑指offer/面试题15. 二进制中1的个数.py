#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/13
# 世界上有10种人：一种人知道二进制，另一种人不知道二进制。。。
'''
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，
有 2 位是 1。因此，如果输入 9，则该函数输出 2。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
 

注意：本题与主站 191 题相同：https://leetcode-cn.com/problems/number-of-1-bits/

'''
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         if n == 1:  return 1
#         if n == 0:  return 0
#         if n < 0:   return False
#         res = 0
#         while(n):
#             if n % 2 == 1:
#                 res += 1
#             n >>= 1
#         return res

pass

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        if n < 0:
            n = n & 0xffffffff

        # while n:
        #     n = n & (n - 1)
        #     count += 1

        while n:
            # n = n & (n - 1)
            if n % 2 == 1:
                count += 1
            n >>= 1
        return count

solution = Solution()
res = solution.hammingWeight(-8)
print(res)
# print(ord('a'))