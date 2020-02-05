#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/4
'''
子数列，又称子序列，在数学中，某个序列的子序列是从最初序列通过去除某些元素但不破坏余下元素的相对位置（在前或在后）而形成的新序列。

给你一个整数数组 arr 和一个整数 difference，请你找出 arr 中所有相邻元素之间的差等于给定 difference 的等差子序列，并返回其中最长的等差子序列的长度。



示例 1：

输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
示例 2：

输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
示例 3：

输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
 

提示：

1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4


'''

pass
# 思路错啦
# from typing import List
# class Solution:
#     def longestSubsequence(self, arr: List[int], difference: int) -> int:
#         res = 0
#         # 先排序吼吼吼
#         arr.sort()  # 由小到大排序
#         # 所以 difference 必须是正数
#         difference = difference if difference >= 0 else -difference
#         # 这段我写的我特么都佩服自己hhh
#         if len(arr) <= 1:
#             return len(arr)
#         tmp_max = 1
#         for i in range(1, len(arr)):
#             if arr[i] - arr[i-1] == difference:
#                 tmp_max += 1
#                 res = max(res, tmp_max)
#             else:
#                 tmp_max = 1
#         return res


from typing import List
# class Solution:
#     def longestSubsequence(self, arr: List[int], difference: int) -> int:
#         res = 1
#         arr = list(set(arr))
#         # 这段我写的我特么都佩服自己hhh
#         if len(arr) <= 1:
#             return len(arr)
#
#         # used = [False for _ in range(len(arr))]
#         used = {arr[num]: num+1 for num in range(len(arr))}
#         arr.sort()
#         difference = difference if difference >= 0 else -difference
#         for i in range(len(arr)):
#             cur = i
#             tmp_max = 1
#             if  used[arr[i]]:
#                 j = 1
#                 while(arr[i]+j*difference in arr and used[arr[i]+j*difference]>cur):
#                     cur = used[arr[i]+j*difference]
#                     tmp_max += 1
#                     used[arr[i] + j*difference] = False
#                     res = max(res, tmp_max)
#                     j+=1
#
#             else:
#                 continue
#         return res

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dict = {arr[0]: 1}
        res = 0
        for i in range(1, len(arr)):
            if arr[i]-difference in dict:
                dict[arr[i]] = dict[arr[i]-difference]+1
            else:
                dict[arr[i]] = 1
        res = max(dict, key=lambda x: dict[x])
        # 这一句不知道为什么不行
        res = max(dict.values())
        return res


solution = Solution()
res = solution.longestSubsequence([1,5,7,8,5,3,4,2,1], -2)
print(res)