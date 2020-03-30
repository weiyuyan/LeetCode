#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/25
'''
给定n个正整数ai，对于每个整数ai,请你按照从小到大的顺序输出它的所有约数。

输入格式
第一行包含整数n。

接下来n行，每行包含一个整数ai。

输出格式
输出共n行，其中第 i 行输出第 i 个整数ai的所有约数。

数据范围
1≤n≤100,
2≤ai≤2∗10^9
输入样例：
2
6
8
输出样例：
1 2 3 6
1 2 4 8
'''
import math
class Solution:
    def get_divisor(self, num):
        sqrt_num = math.sqrt(num)
        res = []
        for i in range(1, int(sqrt_num)+1):
            if num%i == 0:
                res.append(i)
            if num//i != i:
                res.append(num//i)
        res.sort()
        return res

solution = Solution()
num = 10
res = solution.get_divisor(num)
print(res)