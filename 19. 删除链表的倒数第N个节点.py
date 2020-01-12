#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/12
'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		# 增加一个特殊节点方便边界判断
		p = ListNode(-1)
		p.next,a,b = head,p,p
		# 第一个循环，b指针先往前走n步
		while n>0 and b:
			b,n = b.next,n-1
		# 假设整个链表长5，n是10，那么第一次遍历完后b就等用于空了
		# 于是后面的判断就不用做了，直接返回
		if not b:
			return head
		# 第二次，b指针走到链表最后，a指针也跟着走
		# 当遍历结束时，a指针就指向要删除的节点的前一个位置
		while b.next:
			a,b = a.next,b.next
		# 删除节点并返回
		a.next = a.next.next
		return p.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # 增加一个特殊节点，用于边界判断
        p = ListNode(-1)
        p.next = head
        a = p
        b = p
        while(b and n>0):
            b = b.next
            n = n-1
        if not b:
            return head
        while(b.next):
            b = b.next
            a = a.next
        a.next = a.next.next
        return p.next


if __name__ == '__main__':
    a = ListNode(6)
    a.next = ListNode(7)
    b = a.next
    b.next = ListNode(8)
    c = b.next
    c.next = ListNode(8)
    d = c.next
    d.next = ListNode(8)
    e = d.next

    # solution = Solution()
    # solution.removeNthFromEnd(a, 2)