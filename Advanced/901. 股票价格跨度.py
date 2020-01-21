#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/21
'''
编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。

今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。

 

示例：

输入：["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
输出：[null,1,1,1,2,1,4,6]
解释：
首先，初始化 S = StockSpanner()，然后：
S.next(100) 被调用并返回 1，
S.next(80) 被调用并返回 1，
S.next(60) 被调用并返回 1，
S.next(70) 被调用并返回 2，
S.next(60) 被调用并返回 1，
S.next(75) 被调用并返回 4，
S.next(85) 被调用并返回 6。

注意 (例如) S.next(75) 返回 4，因为截至今天的最后 4 个价格
(包括今天的价格 75) 小于或等于今天的价格。

提示：

调用 StockSpanner.next(int price) 时，将有 1 <= price <= 10^5。
每个测试用例最多可以调用  10000 次 StockSpanner.next。
在所有测试用例中，最多调用 150000 次 StockSpanner.next。
此问题的总时间限制减少了 50%。

'''

# 这里用Monotonic Stack方法（单调栈）
# 就是大鱼吃小鱼的思想
class StockSpanner:

    def __init__(self):
        self.s = list()
    def next(self, price: int) -> int:
        span = 1
        while self.s and price >= self.s[-1][0]:
            span += self.s[-1][1]
            self.s.pop()
        self.s.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
print(param_1)
param_1 = obj.next(80)
print(param_1)
param_1 = obj.next(60)
print(param_1)
param_1 = obj.next(70)
print(param_1)
param_1 = obj.next(60)
print(param_1)
param_1 = obj.next(75)
print(param_1)
param_1 = obj.next(85)
print(param_1)
param_1 = obj.next(80)
print(param_1)



