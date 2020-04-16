#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/14
'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
通过次数22,782提交次数40,565
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         a_list = []
#         b_list = []
#         while (l1):
#             a_list.append(l1.val)
#             l1 = l1.next
#         while (l2):
#             b_list.append(l2.val)
#             l2 = l2.next
#
#         res = []
#         min_len = min(len(a_list), len(b_list))
#         tmp = 0  # 两数相加个位值
#         uper = 0  # 两数相加是否有进位（0 or 1）
#         for i in range(1, min_len + 1):
#             if a_list[-i] + b_list[-i] + uper >= 10:
#                 tmp = a_list[-i] + b_list[-i] + uper - 10
#                 uper = 1
#                 res.append(tmp)
#             else:
#                 tmp = a_list[-i] + b_list[-i] + uper
#                 uper = 0
#                 res.append(tmp)
#
#         if len(a_list) > len(b_list):
#             for j in range(min_len + 1, len(a_list) + 1):
#                 if a_list[-j] + uper >= 10:
#                     tmp = a_list[-j] + uper - 10
#                     uper = 1
#                 else:
#                     tmp = a_list[-j] + uper
#                     uper = 0
#                 res.append(tmp)
#
#         elif len(a_list) < len(b_list):
#             for j in range(min_len + 1, len(b_list) + 1):
#                 if b_list[-j] + uper >= 10:
#                     tmp = b_list[-j] + uper - 10
#                     uper = 1
#                 else:
#                     tmp = b_list[-j] + uper
#                     uper = 0
#                 res.append(tmp)
#
#
#         if uper == 1:
#             res.append(1)
#
#         real_res = ListNode(res[-1])
#         a = real_res
#         for k in range(len(res) - 2, -1, -1):
#             a.next = ListNode(res[k])
#             a = a.next
#         return real_res

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans


if __name__ == '__main__':
    solution = Solution()
    A1 = ListNode(7)
    B1 = ListNode(5)
    A1.next = ListNode(2)
    A1.next.next = ListNode(4)
    A1.next.next.next = ListNode(3)
    B1.next = ListNode(6)
    B1.next.next = ListNode(4)
    res = solution.addTwoNumbers(A1, B1)
    while res:
        print(res.val)
        res = res.next