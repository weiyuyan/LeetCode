#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/24
'''
给定n个正整数ai，将每个数分解质因数，并按照质因数从小到大的顺序输出每个质因数的底数和指数。

输入格式
第一行包含整数n。

接下来n行，每行包含一个正整数ai。

输出格式
对于每个正整数ai,按照从小到大的顺序输出其分解质因数后，每个质因数的底数和指数，每个底数和指数占一行。

每个正整数的质因数全部输出完毕后，输出一个空行。

数据范围
1≤n≤100,
1≤ai≤2∗109
输入样例：
2
6
8
输出样例：
2 1
3 1

2 3

'''
# 思路：从小到大枚举所有的因数
# n中最多只包含一个大于sqrt(n)的质因子
# 时间复杂度：o(logn ~ sqrt(n))

import math
class Solution:
    def seperate_factor(self, num: int):
        res = []
        sqrt = math.sqrt(num)
        for i in range(2, int(sqrt)+1):
            s = 0
            while(num%i == 0):
                num //= i
                s += 1
            if s>0:
                res.append((i, s))
        if num > 1:
            res.append((num, 1))
        return res

solution = Solution()
num = 26
res = solution.seperate_factor(num)
print(res)