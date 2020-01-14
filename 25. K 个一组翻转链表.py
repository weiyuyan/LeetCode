#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/14
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 思路：用栈，把 k 个数压入栈中，然后弹出来的顺序就是翻转的！拉了拉了，操，没写出来！
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         # p是边缘节点，left是左侧标记节点，right是右侧标记节点
#         p = left = right =ListNode(-1)
#
#         # 首先检查一下是否有k以上个节点，并将边缘节点p指向第k个节点
#         for i in range(k):
#             if head is None:
#                 return head
#             else:
#                 head = head.next
#                 p.next = head
#         # 有k以上个节点
#
#
#         # 返回开头节点head和结尾节点end的列表形式[head, end]
#         def process_k_nodes(head: ListNode, k: int) -> list(ListNode):
#             tmp_pos = head
#             tmp_list = []
#             for i in range(k):
#                 tmp_list.append(tmp_pos)
#                 tmp_pos = tmp_pos.next
#                 # 如果不够k个
#                 if tmp_pos is None:
#                     return head
#
#             # 设结尾节点end
#             end = ListNode(-1)
#             end.next = tmp_list[-1].next
#
#             # 实现节点栈
#             tmp_pos = head
#             for i in range(k):
#                 tmp_pos.next = tmp_list.pop()
#                 tmp_pos = tmp_pos.next
#
#
#
#
#             pass

# 参考网友powcai
# 思路一：栈
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下链表连接起来
            p.next = tmp
            head = tmp

        return dummy.next

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

    head = solution.reverseKGroup(a, k=2)
    while(head):
        print(head.val)
        head = head.next
