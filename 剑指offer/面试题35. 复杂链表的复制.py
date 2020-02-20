#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/20
'''
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
 

注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head: return None

        # 方法一：构建一个哈希表用空间来换时间，在哈希表里存放每个节点N和其对应的复制节点N'的配对信息，即<N, N'>
        node_dict = {}
        p = head
        # 构建映射表
        while head:
            node_dict[head] = Node(head.val)
            head = head.next
        head = p
        while head:
            node_dict[head].next = node_dict[head.next] if head.next else None
            node_dict[head].random = node_dict[head.random] if head.random else None
            head = head.next

        mirror_head = node_dict[p]
        return mirror_head

solution = Solution()
A = Node(1)
B = Node(2)
C = Node(3)
A.next = B
B.next = C
solution.copyRandomList(A)