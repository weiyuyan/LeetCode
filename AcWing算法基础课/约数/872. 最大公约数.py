#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/25
'''
给定n对正整数ai,bi，请你求出每对数的最大公约数。

输入格式
第一行包含整数n。

接下来n行，每行包含一个整数对ai,bi。

输出格式
输出共n行，每行输出一个整数对的最大公约数。

数据范围
1≤n≤105,
1≤ai,bi≤2∗109
输入样例：
2
3 6
4 6
输出样例：
3
2
'''
# 辗转相除法 # 欧几里得算法
# 最大公约数（a,b） = 最大公约数（b, a mod b）

class Solution:
    def gcd(self, a, b):
        if b:
            return self.gcd(b, a%b)
        else:
            return a

solution = Solution()
a = 4
b = 6
res = solution.gcd(a, b)
print(res)
