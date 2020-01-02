#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2019/9/23

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        for i in range(len(str_int)//2):
            if str_int[i] != str_int[-i-1]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    True_or_false = solution.isPalindrome(-12345654321)
    print(True_or_false)