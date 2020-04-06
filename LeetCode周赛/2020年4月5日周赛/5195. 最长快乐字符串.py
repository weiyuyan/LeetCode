#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/5
'''
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。

提示：

0 <= a, b, c <= 100
a + b + c > 0
'''

# class Solution:
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
#         # （a:num）(b: num)（c:num）
#         # 策略：每次把第一多的字符加两个，第二多的字符加一个
#         if a==1 and b==0 and c==0:
#             return 'a'
#         if a==0 and b==1 and c==0:
#             return 'b'
#         if a==0 and b==0 and c==1:
#             return 'c'
#
#         a_list = [['a', a], ['b', b], ['c', c]]
#         a_list.sort(reverse=True, key=lambda x: x[1])
#         res = ''
#         while (a_list[1][1]>=1 and a_list[0][1]>=2):
#             res += a_list[0][0]*2
#             a_list[0][1] -= 2
#
#             res += a_list[1][0]
#             a_list[1][1] -= 1
#
#             a_list.sort(reverse=True, key=lambda x: x[1])
#
#         if a_list[1][1] == 0:
#             if res[-1] == a_list[0][0]:
#                 return res
#             else:
#                 if a_list[0][1] >= 2:
#                     res += a_list[0][0]*2
#                     return res
#                 if a_list[0][1] == 1:
#                     res += a_list[0][0]
#                     return res
#                 if a_list[0][1] == 0:
#                     return res
#
#         if a_list[0][1] == 1:
#             # 此时a_list[1][1]肯定是1
#
#             if a_list[2][1] == 1:
#                 res += a_list[2][0]
#                 res += a_list[1][0]
#                 res += a_list[0][0]
#                 return res
#             else:
#                 res += a_list[1][0]
#                 res += a_list[0][0]
#                 return res

# 牛人解法：
# 任何时刻都选择当前存量最多的字符
# 当前两个字符相同时，将该字符排除在候选之外
# 初始存量优化：单一字符最大数量必须小于另外（两个字符+1）*2，如‘aabaabaacaa',b与c插入到a序列中，a的数量最多为8。
#
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a':min(a,2*(b+c+1)),'b':min(b,2*(a+c+1)),'c':min(c,2*(b+a+1))}
        n = sum(d.values())
        res = []
        for i in range(n):
            cand = set(['a','b','c'])
            if len(res)>1 and res[-1]==res[-2]:
                cand.remove(res[-1])
            tmp = max(cand,key=lambda x:d[x])
            res.append(tmp)
            d[tmp] -= 1
        return ''.join(res)

class Solution:
    def longestDirverString(self, a: int, b: int, c: int) -> str:
        d = {'a': min(a, 2*(b+c+1)), 'b': min(b, 2*(a+c+1)), 'c': min(c, 2*(a+b+1))}
        n = sum(d.values())
        res = []
        for i in range(n):
            candidate = set(['a', 'b', 'c'])
            if len(res)>1 and res[-1]==res[-2]:
                candidate.remove(res[-1])
            tmp = max(candidate, key=lambda x:d[x])
            res.append(tmp)
            d[tmp] -= 1

        return ''.join(res)

if __name__ == '__main__':
    solution = Solution()
    res = solution.longestDiverseString(4,4,3)
    print(res)
