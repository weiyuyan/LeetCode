#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/27
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。

请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

样例
输入数组：

[
  [1,2,8,9]，
  [2,4,9,12]，
  [4,7,10,13]，
  [6,8,11,15]
]

如果输入查找数值为7，则返回true，

如果输入查找数值为5，则返回false。
'''

# 方法一：每次只选择矩阵右上角的数字
class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not array:
            return False

        found = False
        rows = len(array)   # 行数
        columns = len(array[0])  # 列数
        row = 0
        column = columns - 1
        while(row<rows and column>=0):
            if array[row][column] == target:
                found = True
                break
            elif array[row][column] > target:
                column -= 1
            else:
                row += 1
        return found

if __name__ == '__main__':
    solution = Solution()
    res = solution.searchArray([[]], 40)
    print(res)