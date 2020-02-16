#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/15
'''
给定单向链表的一个节点指针，定义一个函数在O(1)时间删除该结点。

假设链表一定存在，并且该节点一定不是尾节点。

样例
输入：链表 1->4->6->8
      删掉节点：第2个节点即6（头节点为第0个节点）

输出：新链表 1->4->8
'''
# Definition for singly-linked list.

# 思路：是不是一定要得到被删除的节点的前一个节点？不是的，这样子时间复杂度为O(n)
# O(1)的方法：得到需要被删除的节点的下一个节点，将下一个节点的内容(val, next)覆盖到目标节点即可
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void
        """
        node.val = node.next.val
        node.next = node.next.next