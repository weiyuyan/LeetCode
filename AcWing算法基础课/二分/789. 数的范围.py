#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/13
'''
给定一个按照升序排列的长度为n的整数数组，以及 q 个查询。

对于每个查询，返回一个元素k的起始位置和终止位置（位置从0开始计数）。

如果数组中不存在该元素，则返回“-1 -1”。

输入格式
第一行包含整数n和q，表示数组长度和询问个数。

第二行包含n个整数（均在1~10000范围内），表示完整数组。

接下来q行，每行包含一个整数k，表示一个询问元素。

输出格式
共q行，每行包含两个整数，表示所求元素的起始位置和终止位置。

如果数组中不存在该元素，则返回“-1 -1”。

数据范围
1≤n≤100000
1≤q≤10000
1≤k≤10000
输入样例：
6 3
1 2 2 3 3 4
3
4
5
输出样例：
3 4
5 5
-1 -1
'''

# 首先，二分是一定有解的
# 下面给出两个二分算法，一个是求从左往右第一个等于x的，一个是求从右往左第一个等于x的
n = 10000
q = [0]*n
def check(n):
    pass
def bsearch_1(l ,r):
    while(l<r):
        mid = (l+r)//2
        if check(mid):
            r = mid
        else:
            l = mid+1
    return l

def bsearch_2(l, r):
    while(l<r):
        mid = (l+r+1)//2
        if check(mid):
            l = mid
        else:
            r = mid-1
    return l

# 这道题
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/12
from typing import List
class Solution:
    def number_range(self, alist: List[int], num: int):
        l = 0; r = len(alist)-1
        while(l<r):
            mid = (l+r)//2
            if alist[mid]<num:
                l = mid+1
            else:
                r = mid
        if alist[l] != num:
            print('-1 -1')
            return

        print(l, end=' ')

        l = 0; r = len(alist) - 1
        while(l<r):
            mid = (l+r+1)//2
            if alist[mid]<=num:
                l = mid
            else:
                r = mid-1
        print(l)
        return

if __name__ == '__main__':
    solution = Solution()
    len_nums, n = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    num_list = []
    for i in range(n):
        num_list.append(int(input()))

    for num in num_list:
        solution.number_range(nums, num)
