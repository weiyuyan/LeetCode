#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/2
'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None   # 链表为空
        if not head.next: return head # 链表只有一个元素
        p=head; q=p.next; r=q.next; p.next=None
        while r:
            q.next = p
            p = q
            q = r
            r = r.next
        # r==None
        q.next = p
        return q
