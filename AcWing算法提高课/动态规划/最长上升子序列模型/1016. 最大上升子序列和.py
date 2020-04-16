#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/13
'''
一个数的序列 bi，当 b1<b2<…<bS 的时候，我们称这个序列是上升的。

对于给定的一个序列(a1,a2,…,aN)，我们可以得到一些上升的子序列(ai1,ai2,…,aiK)，这里1≤i1<i2<…<iK≤N。

比如，对于序列(1,7,3,5,9,4,8)，有它的一些上升子序列，如(1,7),(3,4,8)等等。

这些子序列中和最大为18，为子序列(1,3,5,9)的和。

你的任务，就是对于给定的序列，求出最大上升子序列和。

注意，最长的上升子序列的和不一定是最大的，比如序列(100,1,2,3)的最大上升子序列和为100，而最长上升子序列为(1,2,3)。

输入格式
输入的第一行是序列的长度N。

第二行给出序列中的N个整数，这些整数的取值范围都在0到10000(可能重复)。

输出格式
输出一个整数，表示最大上升子序列和。

数据范围
1≤N≤1000
输入样例：
7
1 7 3 5 9 4 8
输出样例：
18
'''
# 状态表示：集合：所有以a[i]结尾的上升子序列   属性：和的最大值
# 状态计算：按照倒数第二个数是哪个数来分类（分成i类，分别是：不存在、a1、a2、... 、ai-1）
# 用a[k]表示倒数第二个数
# dp[i] = max(dp[i], dp[k]+a[i])

from typing import List
class Solution:
    def sub_string(self, string: List[int]):
        dp = [string[i] for i in range(len(string))]
        for i in range(len(dp)):
            for j in range(i):
                if string[i]>string[j]:
                    dp[i] = max(dp[i], dp[j]+string[i])
        res = max(dp)
        return res

if __name__ == '__main__':
    solution = Solution()
    num = int(input())
    string = list(map(int, input().split()))
    res = solution.sub_string(string)
    print(res)