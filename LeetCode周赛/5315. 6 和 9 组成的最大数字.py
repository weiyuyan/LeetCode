#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/19
'''
 显示英文描述
用户通过次数785
用户尝试次数798
通过次数797
提交次数996
题目难度Easy
给你一个仅由数字 6 和 9 组成的正整数 num。

你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。

请返回你可以得到的最大数字。



示例 1：

输入：num = 9669
输出：9969
解释：
改变第一位数字可以得到 6669 。
改变第二位数字可以得到 9969 。
改变第三位数字可以得到 9699 。
改变第四位数字可以得到 9666 。
其中最大的数字是 9969 。
示例 2：

输入：num = 9996
输出：9999
解释：将最后一位从 6 变到 9，其结果 9999 是最大的数。
示例 3：

输入：num = 9999
输出：9999
解释：无需改变就已经是最大的数字了。

'''
# 题目没看清，凑！
# class Solution:
#     def maximum69Number (self, num: int) -> int:
#         num_list = []
#         while(num):
#             new_num, mod = divmod(num, 10)
#             num_list.append(mod)
#             num = new_num
#
#         num_list.sort(reverse=True)
#         result = 0
#         for i in num_list:
#             result *= 10
#             result += i
#         return result


class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = []
        while (num):
            new_num, mod = divmod(num, 10)
            num_list.append(mod)
            num = new_num
        for i in range(1, len(num_list)+1):
            if num_list[-i] == 6:
                num_list[-i] = 9
                break
        result = 0
        for j in range(1, len(num_list)+1):
            result *= 10
            result += num_list[-j]
        return result


if __name__ == '__main__':
    solution = Solution()
    res = solution.maximum69Number(6699)
    print(res)

