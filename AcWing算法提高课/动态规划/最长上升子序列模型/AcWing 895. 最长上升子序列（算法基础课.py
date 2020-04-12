#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/11
'''
给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数N。

第二行包含N个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤1000，
−109≤数列中的数≤109
输入样例：
7
3 1 2 1 8 5 6
输出样例：
4
'''
# 状态表示：①集合  所有以a[i]结尾的严格单调上升的子序列    ②属性：max
# 状态计算：根据前一个数是什么情况，一共分成i类：前一个数是a[i-1]，前一个数是a[i-2]...，前一个数是a[0]、前一个数是空

from typing import List
class Solution:
    def upString(self, string: List[int]):
        dp = [1 for _ in range(len(string)+1)]
        for i in range(1, len(dp)-1):
            for j in range(i):
                if string[j] < string[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    num = int(input())
    string = list(map(int, input().split()))
    res = solution.upString(string)
    print(res)