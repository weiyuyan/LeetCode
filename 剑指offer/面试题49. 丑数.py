#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/29
'''
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
'''
import time
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         num = 0
#         for i in range(1, 999999999999999999):
#             tmp = i
#             if i%7 == 0: continue
#             if i%11 == 0: continue
#             if i%13 == 0: continue
#             while(i%5==0):
#                 i /= 5
#             while (i % 3 == 0):
#                 i /= 3
#             while (i % 2 == 0):
#                 i /= 2
#             if i==1: num+=1
#             if num == n: return tmp
# 可以，但时间复杂度太高了

# 自己想的另一种方法
# 拉闸了操，行不通
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n>100:   # 大数，采取非常手段：
#             process = n//4
#             tmp_res = []
#             num = 0
#             for i in range(1, 99999999999999):
#                 tmp = i
#                 while tmp%5 == 0:
#                     tmp /= 5
#                 while tmp%3 == 0:
#                     tmp /= 3
#                 while tmp%2 == 0:
#                     tmp /= 2
#                 if tmp==1: tmp_res.append(i); num+=1
#                 if num==process: break
#
#             tmp_biggest = tmp_res[-1]*5
#             tmp_res_set = set(tmp_res)
#             rest_of_nums = len(tmp_res_set)*4 # 乘2乘3乘5，连本尊共四个
#             if rest_of_nums==n: return tmp_res[-1]*5
#             for i in range(tmp_biggest+1, 99999999999999):
#                 tmp = i
#                 while tmp % 5 == 0:
#                     tmp /= 5
#                 while tmp % 3 == 0:
#                     tmp /= 3
#                 while tmp % 2 == 0:
#                     tmp /= 2
#                 if tmp == 1: rest_of_nums += 1
#                 if rest_of_nums==n: return i
#
#         else:   # 小数，无足为奇
#             num = 0
#             for i in range(1, 99999999999999):
#                 tmp = i
#                 while tmp % 5 == 0:
#                     tmp /= 5
#                 while tmp % 3 == 0:
#                     tmp /= 3
#                 while tmp % 2 == 0:
#                     tmp /= 2
#                 if tmp == 1: num += 1
#                 if num == n: return i
pass
# 大神的写法：
# 三指针法
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        dp = [1]
        for i in range(1, n):
            dp.append(min(dp[p2]*2, dp[p3]*3, dp[p5]*5))
            if dp[i] == dp[p2]*2: p2+=1
            if dp[i] == dp[p3]*3: p3+=1
            if dp[i] == dp[p5]*5: p5+=1
        return dp[-1]


solution = Solution()
a = time.time()
res = solution.nthUglyNumber(1000003)
b = time.time()
print(res)
print(b-a)