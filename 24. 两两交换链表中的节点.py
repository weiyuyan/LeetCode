#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/13

'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 分析：我这里借用了一个数组来存储临时的链表并精进行转换，时间复杂度为o(n)，遍历了整个列表
# 空间复杂度o(1)，因为我只借用了大小为3的列表空间。
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         # 新建边缘节点r
#         r = ListNode(-1)
#         if(head and head.next):
#             r.next = head.next
#         else:
#             return head
#
#         # 新建标记节点p
#         p = ListNode(-1)
#         p.next = head
#         while(p.next and p.next.next and p.next.next.next):
#             tmp_list = [p.next, p.next.next, p.next.next.next]
#             p.next = tmp_list[1]
#             tmp_list[1].next = tmp_list[0]
#             tmp_list[0].next = tmp_list[2]
#             p = tmp_list[0]
#         if (p.next and p.next.next) and not p.next.next.next:
#             tmp_list = [p.next, p.next.next]
#             p.next = tmp_list[1]
#             tmp_list[1].next = tmp_list[0]
#             tmp_list[0].next = None
#         return r.next

# 递归的写法
# 这个傻逼递归的原理我还没懂！
class Solution():
    def swapPairs(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        p = head.next
        head.next = self.swapPairs(p.next)
        p.next = head
        return p

if __name__ == '__main__':
    solution = Solution()

    a = ListNode(6)
    a.next = ListNode(7)
    b = a.next
    b.next = ListNode(8)
    c = b.next
    c.next = ListNode(9)
    d = c.next
    d.next = ListNode(10)
    e = d.next

    head = solution.swapPairs(a)
    while(head):
        print(head.val)
        head = head.next


        