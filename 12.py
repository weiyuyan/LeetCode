#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2019/9/28
'''
Title：整数转罗马数字
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

'''

from typing import List
class Solution:
    def intToRoman(self, num: int) -> str:
        nums =   [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        flag = 1
        result = []
        while(flag):
            for i in range(len(nums)):
                if num - nums[i] >= 0:
                    num = num - nums[i]
                    a = romans[i]
                    result.append(a)
                    break
                if nums[i] == 1:
                    flag = 0
        return ''.join(result)

class Solution2:
    def intToRoman(self, num: int) -> str:
        num_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        res = ""
        for key in sorted(num_dict.keys())[::-1]:
            # sorted()函数是从小到大排序，然后[::-1]是将结果倒序
            if num == 0:
                break
            tmp = num // key
            if tmp == 0:
                continue
            res += tmp * num_dict[key]
            num -= tmp * key
        return  res

if __name__ == '__main__':
    solution = Solution()
    result = solution.intToRoman(3009)
    print (result)

    solution2 = Solution2()
    result = solution2.intToRoman(3009)
    print (result)
