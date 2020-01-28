#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/26
'''
给你一个字符串 s，它仅由字母 'a' 和 'b' 组成。每一次删除操作都可以从 s 中删除一个回文 子序列。

返回删除给定字符串中所有字符（字符串为空）的最小删除次数。

「子序列」定义：如果一个字符串可以通过删除原字符串某些字符而不改变原字符顺序得到，那么这个字符串就是原字符串的一个子序列。

「回文」定义：如果一个字符串向后和向前读是一致的，那么这个字符串就是一个回文。



示例 1：

输入：s = "ababa"
输出：1
解释：字符串本身就是回文序列，只需要删除一次。
示例 2：

输入：s = "abb"
输出：2
解释："abb" -> "bb" -> "".
先删除回文子序列 "a"，然后再删除 "bb"。
示例 3：

输入：s = "baabb"
输出：2
解释："baabb" -> "b" -> "".
先删除回文子序列 "baab"，然后再删除 "b"。
示例 4：

输入：s = ""
输出：0


提示：

0 <= s.length <= 1000
s 仅包含字母 'a'  和 'b'
'''


# class Solution:
#     def removePalindromeSub(self, s: str) -> int:
#         # 先求最长回文子串
#         def mancher(s: str) -> str:
#             if len(s) < 2:
#                 return 0, 1
#             # 将一个可能是偶数长/奇数长的字符串，首位以及每个字符间添加#
#             test = '#' + '#'.join(s) + '#'
#             # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
#             max_len = 0
#             for i in range(len(test)):
#                 left = i - 1
#                 right = i + 1
#                 step = 0
#                 while left >= 0 and right < len(test) and test[left] == test[right]:
#                     # print("spread",test[left],test[right])
#                     left -= 1
#                     right += 1
#                     step += 1
#                     # print(step)
#
#                 if step > max_len:
#                     max_len = step
#                     start = (i - max_len) // 2
#             return start, max_len
#         res = 0
#         while(s):
#             start, num = mancher(s)
#             new_string = list(s)
#             for i in range(num):
#                 new_string.pop(start)
#             s = ''.join(new_string)
#             res += 1
#         return res


# 我他喵佛了！！子序列和子串还不一样！！！先删所有a，剩下只有b，当然是回文
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            for i in range(len(s)-1):
                if s[i] != s[i+1]:
                    return 2
            return 1
# 我尼玛。。。

if __name__ == '__main__':
    s = "bbaabaaa"
    solution = Solution()
    res = solution.removePalindromeSub(s)
    print(res)




