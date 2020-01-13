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

    # 我这个方法不好
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     # 设置一个边缘节点head
    #     head = ListNode(-1)
    #     p = ListNode(-1)  # P是移动节点，等于l1 l2或者其他别的都可以
    #     head.next = p
    #     q = l1
    #     r = l2
    #     while(q and r):
    #         if q.val < r.val:
    #             p.next = q
    #             q = q.next
    #             p = p.next
    #         else:
    #             p.next = r
    #             r = r.next
    #             p = p.next
    #     if q == None:
    #         p.next = r
    #     else:
    #         p.next = q
    #     return head.next.next

    # 利用递归
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

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
        ll = ll.next

'''
复杂度分析：
时间复杂度o(m+n) 因为每次调用递归都会去掉 l1 或者 l2 的头元素（直到至少有一个链表为空），函数 mergeTwoList 中只会遍历
每个元素一次。所以，时间复杂度与合并后的链表长度为线性关系。

空间复杂度o(m+n) 调用 mergeTwoLists 退出时 l1 和 l2 中每个元素都一定已经被遍历过了，所以 n+m 个栈帧会消耗 
O(n+m) 的空间。

'''