#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/16
'''
请你实现一个「数字乘积类」ProductOfNumbers，要求支持下述两种方法：

1. add(int num)

将数字 num 添加到当前数字列表的最后面。
2. getProduct(int k)

返回当前数字列表中，最后 k 个数字的乘积。
你可以假设当前列表中始终 至少 包含 k 个数字。
题目数据保证：任何时候，任一连续数字序列的乘积都在 32-bit 整数范围内，不会溢出。



示例：

输入：
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

输出：
[null,null,null,null,null,null,20,40,0,null,32]

解释：
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3); // 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // 返回  0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32


提示：

add 和 getProduct 两种操作加起来总共不会超过 40000 次。
0 <= num <= 100
1 <= k <= 40000
'''

pass
# 此方法超时了
# class ProductOfNumbers:
#
#     def __init__(self):
#         self.Numbers = []
#
#     def add(self, num: int) -> None:
#         self.Numbers.append(num)
#
#     def getProduct(self, k: int) -> int:
#         if set(self.Numbers) == {1}: return 1
#         res = 1
#         while (k and res):
#             if self.Numbers[-k] == 1:
#                 k -= 1
#             else:
#                 res *= self.Numbers[-k]
#                 k -= 1
#         return res

# Your ProductOfNumbers object will be instantiated and called as such:
pass

# 维护一个乘积前缀树
# 需要注意的是，当add 0发生时，需要特殊处理，不然在后续的product操作中会出现除0错误。
# 想法：维护一个存放'0'位置的列表
class ProductOfNumbers:

    def __init__(self):
        self.prefixTree = [1]    # 前缀树
        self.number_0 = [-1]     # 初始化，默认0的位置是-1


    def add(self, num: int) -> None:
        if num == 0:
            self.number_0.append(len(self.prefixTree))  # 纪录'0'所在的位置

        if self.prefixTree[-1] == 0:
            self.prefixTree.append(num)
        else:
            self.prefixTree.append(self.prefixTree[-1]*num)

    def getProduct(self, k: int) -> int:
        if len(self.prefixTree)-k <= max(self.number_0):    # 前k个区间内包含0
            return 0
        # 前k个区间不包含0
        # 如果倒数第k-1个是0，那么直接返回self.prefixTree[-1]
        if self.prefixTree[-k-1] == 0: return self.prefixTree[-1]
        # 否则，返回self.prefixTree[-1] // self.prefixTree[-k-1]
        else:
            return self.prefixTree[-1] // self.prefixTree[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(2)
param_2 = obj.getProduct(3)
param_2 = obj.getProduct(4)
obj.add(8)
param_2 = obj.getProduct(2)
print(param_2)