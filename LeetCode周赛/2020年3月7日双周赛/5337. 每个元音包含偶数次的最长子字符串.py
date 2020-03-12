#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，
在子字符串中都恰好出现了偶数次。

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。

提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。
'''


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        length = len(s)
        T = [0 for i in range(length + 1)]
        count = 0

        for i in range(length):
            if s[i] == 'a':
                count ^= 1
            elif s[i] == 'e':
                count ^= 2
            elif s[i] == 'i':
                count ^= 4
            elif s[i] == 'o':
                count ^= 8
            elif s[i] == 'u':
                count ^= 16
            T[i + 1] = count

        maxLength = 0
        tmp_dict = {}
        # 纪录首次出现的位置
        for i in range(len(T)):
            if T[i] not in tmp_dict:
                tmp_dict[T[i]] = i

        for j in range(len(T)-1, -1, -1):
            maxLength = max(maxLength, j-tmp_dict[T[j]])
        return maxLength

string = 'eleetminicoworoep'
res = Solution.findTheLongestSubstring(Solution, string)
print(res)
