#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/18
class Solution:
    def minJump(self, jump) -> int:
        rec = []
        dp = [float('inf')] * len(jump)
        for i, x in enumerate(jump):
            rec.append(i + x)
            if (i + x) > len(jump):
                dp[i] = 1
        vis = [False] * len(jump)
        l_i = -1
        s = []
        vis[0] = True
        s.append(0)
        l_max = -1
        step = 0
        while len(s):
            t = []
            for item in s:
                ii = item + jump[item]
                if ii >= len(jump):
                    return step + 1
                if not vis[ii]:
                    t.append(ii)
                    vis[ii] = True
                for x in range(l_max + 1, item):
                    if not vis[x]:
                        t.append(x)
                        vis[x] = True
                l_max = max(l_max, item)
            s = t
            step += 1

if __name__ == '__main__':
    solution = Solution()
    jump = [1, 2, 3,1 ,2,1,5, 1,1,4,2,3,4]
    res = solution.minJump(jump)
    print(res)