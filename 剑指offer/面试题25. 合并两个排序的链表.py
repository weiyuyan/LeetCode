#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/17

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 首先建一个头结点
        head = ListNode(-1)
        p = head
        while(l1 and l2):
            if l1.val >= l2.val:
                p.next = l2
                p = p.next
                l2 = l2.next
            else:
                p.next = l1
                p = p.next
                l1 = l1.next
        if l1:
            p.next = l1
        elif l2:
            p.next = l2
        return head.next