#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/30
'''
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

 
Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
 

Note:

1 <= A.length <= 12
1 <= A[i].length <= 20

'''
from typing import List
# 洗碗了妈的不会
# class Solution:
#     def shortestSuperstring(self, A: List[str]) -> str:
#
#         # 先定义一个求2个字符串距离的函数
#         def _compute(a: str, b: str) -> int:
#             # 计算a, b字符串中a的结尾与b的开头有多少是一样的
#             for i in range(len(a)):
#                 if len(a) - i <= len(b) and a[i:] == b[:len(a) - i]:
#                     return len(a) - i
#             return 0
#         # res = _compute('a', 'abcdefgee')
#         # print(res)
#
#         # 求一个距离矩阵
#         dis_matrix = []
#         num_str = len(A)
#         for i in range(num_str):
#             dis_matrix.append([_compute(A[i], A[j]) for j in range(num_str)])
#             # for j in range(num_str):
#             #     dis_matrix[i].append(_compute(A[i], A[j]))
#
#         # 测试
#         for i in range(len(dis_matrix)):
#             for j in range(len(dis_matrix)):
#                 print(dis_matrix[i][j])
#             print()
#
#
#
#         self.best_length = float('-inf')
#         def _track_back(depth: int, path: List[int], cur_length: int, used: List[bool]) -> (List, int):
#             '''
#
#             :param depth: 这里纪录深度，如果等于len(A)停止
#             :param path: 这里纪录经过的路径
#             :param cur_length: 这里纪录总重复的char数
#             :param used: 这里是字符串使用记录表
#             :return: 返回该条路径path以及重复的char数
#             '''
#             # if cur_length > self.best_length:
#             #     self.best_length = cur_length
#
#             if depth == num_str:
#                 self.best_length = cur_length
#
#                 return
#             for i in range(num_str):
#                 if not used[i]:
#                     used[i] = True
#                     _track_back(depth+1, path.append(A[i]), res+=)
#
#
#
# solution = Solution()
# solution.shortestSuperstring(["alex","loves","leetcode"])
class Solution(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in range(1<<N)]
        parent = [[None] * N for _ in range(1<<N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(range(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)

solution = Solution()
res = solution.shortestSuperstring(["alex","loves","leetcode"])
print(res)

