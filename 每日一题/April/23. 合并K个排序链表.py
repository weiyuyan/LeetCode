#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/26
'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 思路：多指针
        # return self.merge(lists, 0, len(lists)-1)
        res = self.merge(lists, 0, len(lists)-1)
        return res

    def merge(self, list: List[ListNode], l: int, r: int):
        if l==r: return list[l]
        if l>r: return
        mid = (l+r)>>1
        return self.mergeTwoLists(self.merge(list, l, mid), self.merge(list, mid+1, r))

    def mergeTwoLists(self, a: ListNode, b: ListNode):
        ahead = ListNode
        head = ahead
        while a and b:
            if a.val <= b.val:
                ahead.next = ListNode(a.val)
                a = a.next
                ahead = ahead.next
            else:
                ahead.next = ListNode(b.val)
                b = b.next
                ahead = ahead.next

        ahead.next = a if not b else b
        return head.next

from collections import deque
# 方法二：优先队列
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 思路：多指针
        ahead = ListNode(-1)
        res = ahead

        aqueue = deque()
        for i in lists:
            aqueue.append(i)
        while deque:
            a = aqueue.pop()
            if a.next:
                aqueue.append(a.next)

        return res.next


        res = self.merge(lists, 0, len(lists) - 1)
        return res

    def mergeTwoLists(self, a: ListNode, b: ListNode):
        ahead = ListNode
        head = ahead
        while a and b:
            if a.val <= b.val:
                ahead.next = ListNode(a.val)
                a = a.next
                ahead = ahead.next
            else:
                ahead.next = ListNode(b.val)
                b = b.next
                ahead = ahead.next

        ahead.next = a if not b else b
        return head.next

if __name__ == '__main__':
    solution = Solution()
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    c = ListNode(2)
    c.next = ListNode(6)
    res = solution.mergeKLists([a,b,c])
    while(res):
        print(res.val)
        res = res.next
