#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/2
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''
# 卧槽，超时了。。。
# n为35的时候输出了14930352
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         def climb(i, n):
#             if i > n: return 0
#             if i == n: return 1
#             return climb(i+1, n) + climb(i+2, n)
#
#         res = climb(0, n)
#         return res

# 这是花花的递推的写法，时间复杂度o(n)
# 执行用时 :24 ms, 在所有 Python3 提交中击败了97.36%的用户
# 内存消耗 :13 MB, 在所有 Python3 提交中击败了58.05%的用户
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f = [0, 1]
#         f[0] = 1
#         f[1] = 1
#         for i in range(2, n+1):
#             f.append(f[i-1] + f[i-2])
#         return f[-1]

# 动态规划写法：
# 动态规划，又叫“记忆化递归”，即可以写成递归的形式
# 我之前写的那个递归是非记忆化递归，很多情况下是会超时的
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f = [0 for _ in range(n+1)]
#         def num_of_solutions(n: int):
#             if n<=1: return 1
#             if f[n] > 0: return f[n]
#             f[n]=(num_of_solutions(n-1)+num_of_solutions(n-2))
#             return f[n]

        # return num_of_solutions(n)
# 计划递归，属实牛批

# 更强的一种方法，时间复杂度仍为o(n)，空间复杂度变为o(1)：改进了第二种递推方案
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        curr = 1
        for i in range(2, n+1):
            curr = one + two
            two = one
            one = curr

        return curr


if __name__ == '__main__':
    solution = Solution()
    res = solution.climbStairs(35)
    print(res)