#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/29
'''
给定两个字符串A和B，现在要将A经过若干操作变为B，可进行的操作有：

删除–将字符串A中的某个字符删除。
插入–在字符串A的某个位置插入某个字符。
替换–将字符串A中的某个字符替换为另一个字符。
现在请你求出，将A变为B至少需要进行多少次操作。

输入格式
第一行包含整数n，表示字符串A的长度。

第二行包含一个长度为n的字符串A。

第三行包含整数m，表示字符串B的长度。

第四行包含一个长度为m的字符串B。

字符串中均只包含大写字母。

输出格式
输出一个整数，表示最少操作次数。

数据范围
1≤n,m≤1000
输入样例：
10
AGTCTGACGC
11
AGTAAGTAGGC
输出样例：
4
'''
# 状态表示：①集合：所有将a[1~i]变成b[1~j]的操作方式  ②属性：min：所有操作方式中的次数最小值
# 状态计算：
# 操作①：删a[i]：f[i-1][j]+1；
# 操作②：增a[i]：（这里增a[i]后与b[1~j]匹配，说明a[i]==b[j]）（同时，说明a[1~i]与b[1~j-1]匹配）；
# 操作③：改a[i]：如果a[i]==b[j]：pass，否则，把a[i]变成b[j]
# 注意：我们首先要让a[1~i]和b[1~j]匹配上，即f[i-1][j-1]
# if a[i] != b[j]:进行接下来的三个操作
#       f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1, f[i-1][j-1])
# else:f[i][j] = f[i-1][j-1]

class Solution:
    def minEditDistance(self, A: str, B: str):
        # 将A字符串经过若干次操作变成B字符串
        m = len(A)
        n = len(B)
        # 因为涉及到i-1操作和j-1操作，为了避免边界问题，dp数组统一后移一位
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # 初始化数组
        for i in range(m+1):
            dp[i][0] = i    # 这里表示：A长i，B长0，那么由A变到B需要i步骤（i个删除操作）
        for j in range(n+1):
            dp[0][j] = j    # 这里表示：A长0，B长j，那么由A变到B需要j步骤（j个增加操作）

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
                if A[i-1] == B[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    lenA = int(input())
    A = input()
    lenB = int(input())
    B = input()
    res = solution.minEditDistance(A, B)
    print(res)
