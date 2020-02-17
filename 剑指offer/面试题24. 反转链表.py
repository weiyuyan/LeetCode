#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/17
'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000

 

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        if not cur: return None    # 输入的是空指针    # 这里注意：空指针返回的应该是None
        pre = cur.next
        if not pre: return head     # 只有一个节点
        pre_pre = pre.next
        head.next = None # 第一个元素的后继置0

        while pre_pre:
            pre.next = cur
            cur = pre
            pre = pre_pre
            pre_pre = pre_pre.next
        pre.next = cur
        return pre

solution = Solution()
head = ListNode(-1)
p = head
nodes_list = []
for i in nodes_list:
    head.next = ListNode(i)
    head = head.next

reverse = solution.reverseList(None)
while reverse:
    print(reverse.val)
    reverse = reverse.next