#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/24
'''
给定一个正整数n，请你求出1~n中质数的个数。

输入格式
共一行，包含整数n。

输出格式
共一行，包含一个整数，表示1~n中质数的个数。

数据范围
1≤n≤10^6
输入样例：
8
输出样例：
4
'''
# 基本思想：从2~n，从前往后，把每一个数所有的倍数删掉，这样剩下的就是质数
# 为什么呢？对于任何一个数p，如果没有被删掉，说明从2~p-1没有任何一个数能把p删掉，所以p是一个质数
# 时间复杂度： n/2 + n/3 + n/4 +...+ n/n
# = n(1/2 + 1/3 + 1/4 +...+ 1/n)
# 1 + 1/2 + 1/3 + 1/4 +...+ 1/n这个是调和级数：当n趋于正无穷的时候，值为lnn+c

# 优化：我们并不需要把2~p-1中的所有数做一个判断，只要把当中的质数做一个判断就行了 (埃氏算法)

# 质数定理：在1~n中，有n/lnn个质数

# 优化后的真实的时间复杂度
# o(n loglogn)

class Solution:

    # 埃氏做法
    def get_prims(self, num):
        state = [False]*(num+1)
        res = 0
        for i in range(2, num+1):
            if not state[i]:
                res += 1
                print(i)
                for j in range(i, num+1, i):
                    state[j] = True
        return res

solution = Solution()
num = 80
res = solution.get_prims(num)
print(res)