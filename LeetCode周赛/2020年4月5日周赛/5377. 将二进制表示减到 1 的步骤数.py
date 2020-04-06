#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/5
'''
给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数：

如果当前数字为偶数，则将其除以 2 。

如果当前数字为奇数，则将其加上 1 。

题目保证你总是可以按上述规则将测试用例变为 1 。

示例 1：

输入：s = "1101"
输出：6
解释："1101" 表示十进制数 13 。
Step 1) 13 是奇数，加 1 得到 14
Step 2) 14 是偶数，除 2 得到 7
Step 3) 7  是奇数，加 1 得到 8
Step 4) 8  是偶数，除 2 得到 4
Step 5) 4  是偶数，除 2 得到 2
Step 6) 2  是偶数，除 2 得到 1
示例 2：

输入：s = "10"
输出：1
解释："10" 表示十进制数 2 。
Step 1) 2 是偶数，除 2 得到 1
示例 3：

输入：s = "1"
输出：0

提示：

1 <= s.length <= 500
s 由字符 '0' 或 '1' 组成。
s[0] == '1'
'''
class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        if not s: return 0
        s_list = []
        for i in s:
            s_list.append(i)

        while len(s_list) != 1:
            # 是奇数
            if s_list[-1] == '1':

                # 进位操作
                for i in range(len(s_list)-1, -1, -1):
                    if s_list[i] == '0':
                        s_list[i] = '1'
                        break
                    elif s_list[i] == '1':
                        s_list[i] = '0'

                # 如果每一位都是1，需要在前面新增一位
                if s_list[0] == '0':
                    s_list.insert(0, '1')

                res += 1
            # 是偶数
            else:
                s_list.pop()
                res += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    s = "1101"
    res = solution.numSteps(s)
    print(res)
