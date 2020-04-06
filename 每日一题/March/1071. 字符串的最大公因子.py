#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/12
'''
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""
 

提示：

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母
'''
class Solution:
    # 枚举法
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if str1[:i]==str2[:i] and str1[:i]*(len(str1)//i)==str1 and str2[:i]*(len(str2)//i)==str2:
            # 或者
            # if str1[:i]*(len(str1)//i)==str1 and str2[:i]*(len(str2)//i)==str2:
                return str1[:i]
        return ''

    # 枚举法（优化）
    # 先求两个长度的最大公约数，然后再搞
    def gcdOfStrings_(self, str1: str, str2: str) -> str:
        import math
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[:candidate_len]
        if candidate*(len(str1)//candidate_len)==str1 and candidate*(len(str2)//candidate_len)==str2:
            return candidate
        return ''

solution = Solution()
str1 = 'LEET'
str2 = 'CODE'
res = solution.gcdOfStrings_(str1, str2)
print(res)
