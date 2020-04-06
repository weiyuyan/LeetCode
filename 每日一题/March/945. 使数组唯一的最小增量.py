#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/4
'''
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

返回使 A 中的每个值都是唯一的最少操作次数。

示例 1:

输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
示例 2:

输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
提示：

0 <= A.length <= 40000
0 <= A[i] < 40000
通过次数26,178提交次数54,949
'''
from typing import List
class Solution:
    # 自己写的
    # def minIncrementForUnique(self, A: List[int]) -> int:
    #     res = 0
    #     if not A: return 0
    #     A.sort()
    #     minimum = A[0]
    #
    #     statistic_dict = {}
    #     for num in range(minimum, 80000):
    #         statistic_dict[num] = 0
    #     for num in A:
    #         statistic_dict[num] += 1
    #
    #
    #     zero_space = []
    #     many_space = []
    #     for key in statistic_dict.keys():
    #         if statistic_dict[key] == 0:
    #             zero_space.append(key)
    #         if statistic_dict[key] > 1:
    #             for _ in range(statistic_dict[key]-1):
    #                 many_space.append(key)
    #
    #     while many_space:
    #         a = many_space.pop(0)
    #         b = zero_space.pop(0)
    #         while b<=a:
    #             b = zero_space.pop(0)
    #         res += b-a
    #
    #     return res

    # 方法二：排序后：只需要把后面的数变成比前一个数大一即可
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                res += A[i-1] - A[i] + 1
                A[i] = A[i-1]+1
        return res


if __name__ == '__main__':
    solution = Solution()
    arr = [1]
    res = solution.minIncrementForUnique(arr)
    print(res)


