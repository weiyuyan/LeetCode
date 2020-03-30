#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/29
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
3
'''
# 首先，一个长度为n的序列，一共可以有2^n个子序列
# 所以，如果用纯暴力做法的话，得有2^1000次计算，也就是大约10^300

# 状态表示（化零为整）①集合：f[i][j]：所有A[1~i]与B[1~j]的公共子序列的集合    ②属性：max（集合里所有公共子序列长度的最大值）
# 状态计算（化整为零）00表示f[i][j]里都不包含A[i]和B[j]，
#                   01表示不包含A[i]，包含B[j]，
#                   10表示包含A[i]，不包含B[j]，
#                   11表示都包含A[i]和B[j]

# 对于11状态，由于既包含a[i]又包含b[j]，所以必须满足a[i]==b[j]，此时f[i][j] = f[i-1][j-1]+1
# 对于00状态，由于既不包含a[i]又不包含b[j]，所以f[i][j] = f[i-1][j-1]
# 对于01状态，不包含a[i]，包含b[j]，这时我们可能会想到用f[i-1][j]，但是需要注意的是，f[i-1][j]除了有包含b[j]的一部分，也有
# 不包含b[j]的那一部分（换言之它还是被分成了4类），也就是说f[i-1][j]实际覆盖面积比f[i][j]中的01状态大，
# 然而，即时超覆盖了，但并不影响结果，数据本质上还在集合内流动，对于求count会影响，对于求min、max的情况不影响！
# 所以，对于01状态，f[i][j] = f[i-1][j]
# 对于10状态，f[i][j] = f[i][j-1]
# 此外，我们发现，00状态的f[i-1][j-1]一定包含在f[i-1][j]和f[i][j-1]中，所以我们只需要考虑10 01 11三个状态
# 我们下标从1开始，方便一些hhh

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

