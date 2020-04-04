#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/4
'''
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
示例 3：

输入：[1]
输出：false
解释：没有满足要求的分组。
示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
示例 5：

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]

提示：

1 <= deck.length <= 10000
0 <= deck[i] < 10000
'''
from typing import List
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 可以求最大公约数hh
        a_dict = {}
        for i in deck:
            if i in a_dict:
                a_dict[i] += 1
            else:
                a_dict[i] = 1
        a_list = []
        for key in a_dict:
            a_list.append(a_dict[key])

        minimum = min(a_list)
        if minimum == 1:
            return False
        yueshu = set()
        # 求minimum的所有约数
        for j in range(2, int(math.sqrt(minimum))+1):
            if minimum%j == 0:
                yueshu.add(j)
                yueshu.add(minimum//j)
        yueshu.add(minimum)

        while yueshu:
            a = yueshu.pop()
            for i in range(len(a_list)):
                if a_list[i]%a != 0:
                    break
            if a_list[i] % a == 0:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    a = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
    res = solution.hasGroupsSizeX(a)
    print(res)