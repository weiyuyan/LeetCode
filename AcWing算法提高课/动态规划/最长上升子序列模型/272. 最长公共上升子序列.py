#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/13
'''
熊大妈的奶牛在小沐沐的熏陶下开始研究信息题目。

小沐沐先让奶牛研究了最长上升子序列，再让他们研究了最长公共子序列，现在又让他们研究最长公共上升子序列了。

小沐沐说，对于两个数列A和B，如果它们都包含一段位置不一定连续的数，且数值是严格递增的，那么称这一段数是两个数列的公共上升子序列，而所有的公共上升子序列中最长的就是最长公共上升子序列了。

奶牛半懂不懂，小沐沐要你来告诉奶牛什么是最长公共上升子序列。

不过，只要告诉奶牛它的长度就可以了。

数列A和B的长度均不超过3000。

输入格式
第一行包含一个整数N，表示数列A，B的长度。

第二行包含N个整数，表示数列A。

第三行包含N个整数，表示数列B。

输出格式
输出一个整数，表示最长公共上升子序列的长度。

数据范围
1≤N≤3000,序列中的数字均不超过231−1
输入样例：
4
2 2 1 3
2 1 2 3
输出样例：
2
'''
# 首先，最大上升子序列，集合的划分方式是根据前面的元素是什么划分成了k类
# 最长公共子序列，集合的划分方式是分成了4类：
# 用00表示A[i]和B[j]都不包含，用01表示不包含A[i]，包含B[j]
# 用10表示包含A[i]不包含B[j]，用11表示包含A[i]和B[j]
# 最长公共上升子序列，我们这里把两种划分方式结合在一起

# 状态表示：dp[i][j]表示由A[1~i]、B[1~j]构成的，且以b[j]结尾的所有公共上升子序列 属性：max
# 状态计算：分为两部分：①所有包含A[i]的公共上升子序列  ②所有不包含A[i]的公共上升子序列
# 对于第一部分：根据倒数第二个数是什么，分为k类

# from typing import List
# class Solution:
#     def maxCommonUperString(self, A: List[int], B: List[int]):
#         dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
#         for i in range(1, len(A)):
#             for j in range(1, len(B)):
#                 dp[i][j] = dp[i-1][j]
#                 if A[i] == B[j]:
#                     dp[i][j] = max(dp[i][j], 1)
#                     for k in range(1, j):
#                         if B[k]<B[j]:
#                             dp[i][j] = max(dp[i][j], dp[i][k]+1)
#
#         res = 0
#         for i in range(len(dp)):
#             for j in range(len(dp[0])):
#                 res = max(res, dp[i][j])
#         return res

# 优化：（对代码做等价变形）
from typing import List
class Solution:
    def maxCommonUperString(self, A: List[int], B: List[int]):
        dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
        for i in range(1, len(A)):
            maxv = 1
            for j in range(1, len(B)):
                dp[i][j] = dp[i-1][j]
                if A[i] == B[j]:
                    dp[i][j] = max(dp[i][j], maxv)
                if B[j] < A[i]:
                    maxv = max(maxv, dp[i-1][j]+1)
        res = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    solution = Solution()
    num = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = solution.maxCommonUperString(A, B)
    print(res)