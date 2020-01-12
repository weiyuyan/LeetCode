#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/12
'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 设置一个边缘节点head
        head = ListNode(-1)
        p = ListNode(-1)  # P是移动节点，等于l1 l2或者其他别的都可以
        head.next = p
        q = l1
        r = l2
        while(q and r):
            if q.val < r.val:
                p.next = q
                q = q.next
                p = p.next
            else:
                p.next = r
                r = r.next
                p = p.next
        if q == None:
            p.next = r
        else:
            p.next = q
        return p.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    solution = Solution()
    ll = solution.mergeTwoLists(l1, l2)
    while(ll != None):
        print(ll.val)
