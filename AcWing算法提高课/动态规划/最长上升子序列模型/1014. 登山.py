#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/12
'''
五一到了，ACM队组织大家去登山观光，队员们发现山上一个有N个景点，并且决定按照顺序来浏览这些景点，即每次所浏览景点的编号都要大于前一个浏览景点的编号。

同时队员们还有另一个登山习惯，就是不连续浏览海拔相同的两个景点，并且一旦开始下山，就不再向上走了。

队员们希望在满足上面条件的同时，尽可能多的浏览景点，你能帮他们找出最多可能浏览的景点数么？

输入格式
第一行包含整数N，表示景点数量。

第二行包含N个整数，表示每个景点的海拔。

输出格式
输出一个整数，表示最多能浏览的景点数。

数据范围
2≤N≤1000
输入样例：
8
186 186 150 200 160 130 197 220
输出样例：
4
'''

# 条件一：按照编号递增的顺序浏览 ==> 必须是子序列
# 条件二：相邻两个景点海拔不能相同
# 条件三：一旦开始下降，就不能上升了
#  大致是以下的上山下山路线
#
#            /\
#           /  \
#          /    \
#         /      \
# 目标：求出所有形状是上述子序列长度的最大值
# 我们可以看到，在上述情形中，峰值是唯一的
# 假设这些路线的峰值依次为a[1] a[2] a[3]...a[n]
# 且峰左和峰右是互不相干的，∴峰左的最大值+峰右的最大值

# dpl[i]表示从1到i所走的路径
# dpr[i]表示从n到i所走的路径
# 最后dp[i] = dpl[i] + dpr[i] - 1（峰值被多算了一次）

from typing import List
class Solution:
    def climb(self, mountains: List[int]):
        dpl = [1 for _ in range(len(mountains))]
        dpr = [1 for _ in range(len(mountains))]
        dp = [0 for _ in range(len(mountains))]

        for i in range(len(dpl)):
            for j in range(i):
                if mountains[i] > mountains[j]:
                    dpl[i] = max(dpl[i], dpl[j]+1)

        for i in range(len(dpr)-1, -1, -1):
            for j in range(i+1, len(dpr)):
                if mountains[i] > mountains[j]:
                    dpr[i] = max(dpr[i], dpr[j]+1)

        for k in range(len(dp)):
            dp[k] = dpl[k]+dpr[k]-1

        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    num = int(input())
    mountains = list(map(int, input().split()))
    res = solution.climb(mountains)
    print(res)