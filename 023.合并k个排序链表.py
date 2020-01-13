#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/13

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

# 暴力法：
'''
遍历所有链表，将所有节点的值放到一个数组中。
将这个数组排序，然后遍历所有元素得到正确顺序的值。
用遍历得到的值，创建一个新的有序链表。
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        point = head = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        nodes.sort()
        for i in nodes:
            point.next = ListNode(i)
            point = point.next
        return head.next

if __name__ == '__main__':
    solution = Solution()

    a = ListNode(6)
    a.next = ListNode(7)
    b = a.next
    b.next = ListNode(8)
    c = b.next
    c.next = ListNode(8)
    d = c.next
    d.next = ListNode(8)
    e = d.next

    node_lists = [a]
    new_nodes = solution.mergeKLists(node_lists)
    while(new_nodes):
        print(new_nodes.val)
        new_nodes = new_nodes.next