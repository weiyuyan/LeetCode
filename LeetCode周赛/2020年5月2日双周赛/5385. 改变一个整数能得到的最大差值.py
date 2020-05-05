#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/5/2
'''
给你一个整数 num 。你可以对它进行如下步骤恰好 两次 ：

选择一个数字 x (0 <= x <= 9).
选择另一个数字 y (0 <= y <= 9) 。数字 y 可以等于 x 。
将 num 中所有出现 x 的数位都用 y 替换。
得到的新的整数 不能 有前导 0 ，得到的新整数也 不能 是 0 。
令两次对 num 的操作得到的结果分别为 a 和 b 。

请你返回 a 和 b 的 最大差值 。


示例 1：

输入：num = 555
输出：888
解释：第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 999 和 b = 111 ，最大差值为 888
示例 2：

输入：num = 9
输出：8
解释：第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 9 和 b = 1 ，最大差值为 8
示例 3：

输入：num = 123456
输出：820000
示例 4：

输入：num = 10000
输出：80000
示例 5：

输入：num = 9288
输出：8700

提示：
1 <= num <= 10^8

'''
from typing import List
class Solution:
    def maxDiff(self, num: int) -> int:
        list_num = []
        for j in str(num):
            list_num.append(j)

        self.max_list_num = list_num[:]
        self.min_list_num = list_num[:]
        self.get_max(self.max_list_num, 0)
        self.get_min(self.min_list_num)
        max_num = int(''.join(self.max_list_num))
        min_num = int(''.join(self.min_list_num))
        return max_num-min_num


    def get_max(self, num: List[str], pos: int):
        if pos >= len(num):
            return
        # 如果第一位不是9，把它变成9，否则，顺移到下一位
        if num[pos] != '9':
            tmp = num[pos]
            for i in range(pos, len(num)):
                if num[i] == tmp:
                    num[i] = '9'
        # 如果第一位是9，顺移到下一位
        else:
            self.get_max(num, pos+1)

    def get_min(self, num: List[str]):
        # 如果第一位不是1，把它变成1，否则，向后查找直到不是'1'，将它变成0
        if num[0] == '1':
            for i in range(len(num)):
                tmp = '0'
                if num[i] != '1' and num[i] != '0':
                    tmp = num[i]
                    break
            for j in range(len(num)):
                if num[j] == tmp:
                    num[j] = '0'
        else:
            tmp = num[0]
            for i in range(len(num)):
                if num[i] == tmp:
                    num[i] = '1'

if __name__ == '__main__':
    solution = Solution()
    num = 10000
    res = solution.maxDiff(num)
    print(res)