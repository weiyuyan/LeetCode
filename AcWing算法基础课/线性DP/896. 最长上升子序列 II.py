#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/28
'''
给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数N。

第二行包含N个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤100000，
−109≤数列中的数≤109
输入样例：
7
3 1 2 1 8 5 6
输出样例：
4
'''
# 首先，用之前的做法写是可以的，不过会超时
from typing import List
class Solution:
    def max_substring(self, string: List[int]):
        n = len(string)
        dp = [float('-inf') for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = 1
            for j in range(1, i):
                if string[i-1] > string[j-1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        # n = len(string)
        # dp = [float('-inf') for _ in range(n+1)]
        # for i in range(1, n+1):
        #     dp[i] = 1
        #     for j in range(1, i):
        #         if string[i-1] > string[j-1]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

# 优化：
# 在dp[i], 对于符合条件的同样长度的dp[i]子序列，如：1→3→5→8 和 1→2→4→6，由于最后一个元素6小于8，所以第二组由于第一组
# 因为长度相同的情况下，末位元素越小，适配性越强
# 受此启发，对于dp[i]，我们不需要把全部情况都存储进去，只要存储前面每种长度的最长上升子序列的末位的值的最小值
# 容易证明，dp[i]中的序列一定是单调递增的（存的是不同长度的单调递增子序列中的结尾的最小值）
# 状态计算，对于每一个a[i]，我们要把它接到dp[i]数组中“最大的、小于a[i]的数后面”
# 如何找到小于a[i]的最大的数？由于是单调递增的，所以可以用二分查找

class Solution:
    def max_substring(self, string: List[int]):
        n = len(string)
        dp = [string[0]]+[float('inf') for _ in range(n+1)]  # dp存放了每种长度下最长上升子序列末位值的最小值，经严格证明，已经是单调递增的
        # dp[0] = string[0]
        for i in range(1, n):
            target = string[i]
            pos = self.bi_search(dp, target, 0, n)

            # 特殊情况，只针对开头时候寻找到的位置的元素仍大于target
            if dp[pos] > target and dp[pos]!=float('inf'):
                dp[pos] = target
            elif dp[pos] < target:
                dp[pos+1] = min(dp[pos+1], target)

        res = 0
        before = float('-inf')
        for j in dp:
            if j>before and j!=float('inf'):
                res += 1
                before = j
            else:
                break
        return res


    def bi_search(self, dp: List[int], target: int, begin: int, end: int):
        # 二分查找，返回小于target的最大的位置

        mid = (begin + end) >> 1
        while(begin<end):
            if target >= dp[mid]:
                return self.bi_search(dp, target, mid+1, end)
            else:
                return self.bi_search(dp, target, begin, mid)
        return (mid-1) if mid else 0    # 如果mid是0返回0，否则返回mid-1


if __name__ == '__main__':
    n = int(input())
    string = list(map(int, input().split()))
    solution = Solution()
    res = solution.max_substring(string)
    print(res)
