#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/3
'''
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False
'''

import math
# 方法一：
# 贝祖定理
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0

# 方法二：
# 首先对题目进行建模。观察题目可知，在任意一个时刻，此问题的状态可以由两个数字决定：X 壶中的水量，以及 Y 壶中的水量。
#
# 在任意一个时刻，我们可以且仅可以采取以下几种操作：
#
# 把 X 壶的水灌进 Y 壶，直至灌满或倒空；
# 把 Y 壶的水灌进 X 壶，直至灌满或倒空；
# 把 X 壶灌满；
# 把 Y 壶灌满；
# 把 X 壶倒空；
# 把 Y 壶倒空。
# 因此，本题可以使用深度优先搜索来解决。搜索中的每一步以 remain_x, remain_y 作为状态，即表示 X 壶和 Y 壶中的水量。
# 在每一步搜索时，我们会依次尝试所有的操作，递归地搜索下去。
# 这可能会导致我们陷入无止境的递归，因此我们还需要使用一个哈希结合（HashSet）存储所有已经搜索过的 remain_x, remain_y 状态，
# 保证每个状态至多只被搜索一次。
#
# 在实际的代码编写中，由于深度优先搜索导致的递归远远超过了 Python 的默认递归层数
# （可以使用 sys 库更改递归层数，但不推荐这么做），因此下面的代码使用栈来模拟递归，避免了真正使用递归而导致的问题。
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        self.seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in self.seen:
                continue
            self.seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        self.seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or (remain_x+remain_y) == z:
                return True
            if (remain_x, remain_y) in self.seen:
                continue
            self.seen.add((remain_x, remain_y))

            # 把X壶灌满
            stack.append((x, remain_y))

            # 把Y壶灌满
            stack.append((remain_x, y))

            # 把X壶倒空
            stack.append((0, remain_y))

            # 把Y壶倒空
            stack.append((remain_x, 0))

            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空
            stack.append((remain_x-min(remain_x, y-remain_y), remain_y+min(remain_x, y-remain_y)))

            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空
            stack.append((remain_x+min(x-remain_x, remain_y), remain_y-min(x-remain_x, remain_y)))
        return False