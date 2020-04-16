#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/12
'''
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。     

合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK， 
则他们的身高满足T1<…<Ti>Ti+1>…>TK(1≤i≤K)。     

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

输入格式
输入的第一行是一个整数N，表示同学的总数。

第二行有n个整数，用空格分隔，第i个整数Ti是第i位同学的身高(厘米)。

输出格式
输出包括一行，这一行只包含一个整数，就是最少需要几位同学出列。

数据范围
2≤N≤100,
130≤Ti≤230
输入样例：
8
186 186 150 200 160 130 197 220
输出样例：
4
'''
# 本题和1014、登山 是对偶问题，所以这里把变量换一下，结果改一下直接贴上去了
from typing import List
class Solution:
    def chorus(self, student: List[int]):
        dpl = [1 for _ in range(len(student))]
        dpr = [1 for _ in range(len(student))]
        dp = [0 for _ in range(len(student))]

        for i in range(len(dpl)):
            for j in range(i):
                if student[i] > student[j]:
                    dpl[i] = max(dpl[i], dpl[j]+1)

        for i in range(len(dpr)-1, -1, -1):
            for j in range(i+1, len(dpr)):
                if student[i] > student[j]:
                    dpr[i] = max(dpr[i], dpr[j]+1)

        for k in range(len(dp)):
            dp[k] = dpl[k]+dpr[k]-1

        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    num = int(input())
    student = list(map(int, input().split()))
    res = solution.chorus(student)
    print(len(student)-res)