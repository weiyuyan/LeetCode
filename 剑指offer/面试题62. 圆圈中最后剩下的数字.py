#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/6
'''
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，
因此最后剩下的数字是3。

示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2

限制：

1 <= n <= 10^5
1 <= m <= 10^6
'''
# 这是著名的约瑟夫环问题
# 使用环形链表解决
# 时间复杂度较高（其实也不至于吧。。。）
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n <= 0: return False
        point = 0
        circle = [i for i in range(n)]
        res = []
        while(len(res) != n):
            point += m-1
            if point >= len(circle):
                point = point % len(circle)
            res.append(circle.pop(point))

        return res[-1]

# 利用数学公式的解法，神仙解法
# class Solution:
#     def lastRemaining(self, n: int, m: int) -> int:
#         ans = 0
#         for i in range(2,n+1):
#             ans = (ans+m) % i
#         return ans
#
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n<=0: return False
        ans = 0
        for i in range(2, n+1):
            ans = (ans+m) % i
        return ans

solution = Solution()
res = solution.lastRemaining(0, 3)
print(res)