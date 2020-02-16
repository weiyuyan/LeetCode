#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/15
'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留。

样例1
输入：1->2->3->3->4->4->5

输出：1->2->5
样例2
输入：1->1->1->2->3

输出：2->3
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while(head):
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

solution = Solution()
a = ListNode(1)
tmp = a

node_list = [1, 2, 2, 3, 4, 5, 5, 6]
for nodeval in node_list:
    node = ListNode(nodeval)
    a.next = node
    a = a.next

a = tmp
while(a):
    print(a.val)
    a = a.next

a = tmp
solution.deleteDuplication(a)

a = tmp
while(a):
    print(a.val)
    a = a.next