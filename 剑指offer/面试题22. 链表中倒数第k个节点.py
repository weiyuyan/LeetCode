#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/17
'''
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        first_ptr = head
        second_ptr = head
        count = 0
        if k <= 0: return False
        if not first_ptr: return False
        while first_ptr:
            if count == k:
                second_ptr = second_ptr.next
                first_ptr = first_ptr.next
            else:
                first_ptr = first_ptr.next
                count += 1

        if count < k: return False

        return second_ptr

solution = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

b = None
res = solution.getKthFromEnd(a, 2)
print(res.val)
