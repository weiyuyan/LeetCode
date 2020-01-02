#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2019/8/21
# Definition for singly-linked list.

import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = 0
        s2 = 0
        for i in range(0, -len(l1), -1):
            # 逆序遍历列表
            s1 *= 10
            s1 += l1[i-1]
        for i in range(0, -len(l2), -1):
            # 逆序遍历列表
            s2 *= 10
            s2 += l2[i-1]
        s3 = s1+s2
        l3 = []
        while s3:
            l3.append(s3 % 10)
            s3 = math.floor(s3 / 10)
        return l3


def main():
    l1 = [2,4,3]
    l2 = [5,6,4]
    # solution = Solution()
    # s3 = solution.addTwoNumbers(l1, l2)
    # print(s3)
    ll1 = ListNode(l1)
if __name__ == '__main__':
    main()

