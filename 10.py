#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2019/9/23

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素

        :param s: 可能为空，且只包含从 a-z 的小写字母。
        :param p: 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
        :return:
        '''
        for i in range(len(s)):
            if s[i] == p[i]:
                yield from self.isMatch(s[i+1:], p[i+1:])
            elif p[i] == '*':
                yield from self.isMatch(s[i+1:], p[i+1:])
            elif p[i] == '.':
                if p[i+1] == '*':
                    yield from self.isMatch(s[i+1], p[i:])
            else:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    True_False = solution.isMatch('aaa', 'aaa')
    print(True_False)