#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/18
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 
提示：

各函数的调用总次数不超过 20000 次
 
注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_of_numbers = []
        self.list_of_mins = []

    def push(self, x: int) -> None:
        self.list_of_numbers.append(x)
        if len(self.list_of_mins) == 0: # 空的
            self.list_of_mins.append(x)
        else:
            self.list_of_mins.append(min(x, self.list_of_mins[-1]))

    def pop(self) -> None:
        if self.list_of_numbers:
            self.list_of_mins.pop()
            self.list_of_numbers.pop()
        else: print('stack is empty!')

    def top(self) -> int:
        return self.list_of_numbers[-1] if self.list_of_numbers else []

    def min(self) -> int:
        return self.list_of_mins[-1] if self.list_of_numbers else []

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
a = obj.min()
print(a)
# x = -2
# obj.push(x)
# x = 0
# obj.push(x)
# x = -3
# obj.push(x)
# param_3 = obj.top()
# param_4 = obj.min()
# print(param_3)
# print(param_4)
# a = obj.pop()
# print(a)
# print(obj.min())


