#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/27
'''
输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。

返回的结果用数组存储。

样例
输入：[2, 3, 5]
返回：[5, 3, 2]
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：栈
class Solution(object):
    def printListReversingly(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        if not head:
            return []
        p = head
        while(p):
            stack.append(p.val)
            p = p.next

        return [stack.pop() for _ in range(len(stack))]

if __name__ == '__main__':
    solution = Solution()
    Dummy = ListNode(-1)
    Dummy.next = ListNode(1)
    Dummy.next.next = ListNode(2)
    Dummy.next.next.next = ListNode(3)
    res = solution.printListReversingly(Dummy)
    print(res)