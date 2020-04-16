#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/13
'''
给定两个长度分别为N和M的字符串A和B，求既是A的子序列又是B的子序列的字符串长度最长是多少。

输入格式
第一行包含两个整数N和M。

第二行包含一个长度为N的字符串，表示字符串A。

第三行包含一个长度为M的字符串，表示字符串B。

字符串均由小写字母构成。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤1000,

输入样例：
4 5
acbd
abedc
输出样例：
'''
# 状态表示：①集合：dp[i][j]表示所有A[1~i]与B[1~j]的公共子序列的集合  ②属性：max
# 状态计算：有4种状态：用00表示A[i]和B[j]都不包含，用01表示不包含A[i]，包含B[j]
#                    用10表示包含A[i]不包含B[j]，用11表示包含A[i]和B[j]
# 对于11情况：if A[i]==B[j]，dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
# 对于00情况：dp[i][j] = max(dp[i-1][j-1], dp[i][j])
# 对于01情况：注意虽然dp[i-1][j]存在包含B[j]和不包含B[j]的两种情况，但是我们要求的是max，不是要求count，所以无所谓
# 并且，容易看出dp[i-1][j]和dp[i][j-1]已经把dp[i-1][j-1]包括进去了，所以00情况也可以省去了

class Solution:
    def maxCommonString(self, A: str, B: str):
        len_A = len(A)
        len_B = len(B)

        dp = [[0 for _ in range(len_B+1)] for _ in range(len_A+1)]
        for i in range(1, len_A+1):
            for j in range(1, len_B+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    len_A, len_B = list(map(int, input().split()))
    A = input()
    B = input()
    res = solution.maxCommonString(A, B)
    print(res)