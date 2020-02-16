#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/16
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序。

使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。

样例
输入：[1,2,3,4,5]

输出: [1,3,5,2,4]
'''

class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        """
        # 这次要用到双指针
        # p, q = 0, len(array)-1
        # while(p<q):
        #     if array[p] % 2 == 0:
        #         if array[q] % 2 == 0:
        #             q -= 1
        #         else:
        #             array[p], array[q] = array[q], array[p]
        #             p += 1
        #             q -= 1
        #     else:
        #         p += 1

        p, q = 0, len(array) - 1
        while (p < q):
            if self.judge(array[p]):
                if self.judge(array[q]):
                    q -= 1
                else:
                    array[p], array[q] = array[q], array[p]
                    p += 1
                    q -= 1
            else:
                p += 1

    # 可扩展的方法，这里提出了一个通用的框架
    def judge(self, x) -> bool:
        return True if x % 2 == 0 else False
        # return True if x % 3 == 0 else False


solution = Solution()
啊 = [1, 2, 3, 4, 5, 6, 7]
solution.reOrderArray(啊)
print(啊)
