#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/11
'''
怪盗基德是一个充满传奇色彩的怪盗，专门以珠宝为目标的超级盗窃犯。

而他最为突出的地方，就是他每次都能逃脱中村警部的重重围堵，而这也很大程度上是多亏了他随身携带的便于操作的滑翔翼。

有一天，怪盗基德像往常一样偷走了一颗珍贵的钻石，不料却被柯南小朋友识破了伪装，而他的滑翔翼的动力装置也被柯南踢出的足球破坏了。

不得已，怪盗基德只能操作受损的滑翔翼逃脱。

假设城市中一共有N幢建筑排成一条线，每幢建筑的高度各不相同。

初始时，怪盗基德可以在任何一幢建筑的顶端。

他可以选择一个方向逃跑，但是不能中途改变方向（因为中森警部会在后面追击）。

因为滑翔翼动力装置受损，他只能往下滑行（即：只能从较高的建筑滑翔到较低的建筑）。

他希望尽可能多地经过不同建筑的顶部，这样可以减缓下降时的冲击力，减少受伤的可能性。

请问，他最多可以经过多少幢不同建筑的顶部(包含初始时的建筑)？

输入格式
输入数据第一行是一个整数K，代表有K组测试数据。

每组测试数据包含两行：第一行是一个整数N，代表有N幢建筑。第二行包含N个不同的整数，每一个对应一幢建筑的高度h，按照建筑的排列顺序给出。

输出格式
对于每一组测试数据，输出一行，包含一个整数，代表怪盗基德最多可以经过的建筑数量。

数据范围
1≤K≤100,
1≤N≤100,
0<h<10000
输入样例：
3
8
300 207 155 299 298 170 158 65
8
65 158 170 298 299 155 207 300
10
2 1 3 4 5 6 7 8 9 10
输出样例：
6
6
9
'''

# 当起点和方向确定了之后，问题就变成
# a[i]：求a[i]为起点的最长上升子序列
# 状态表示：dp[i]，表示以i为起点，从左向右方向 或 从右向左方向的走法集合   属性：max
# 状态计算：dp[i] = max(dp[i], dp[j]+1) for j in range(i) && a[i]>a[j]
# dp[i] = max(dp[i], dp[j]+1) for j in range(n, i, -1)  && a[i]>a[j]

from typing import List
class Solution:
    def Kiddo(self, buildings: List[int]):
        res = 0

        # 从左到右遍历
        dp = [1 for _ in range(len(buildings))]
        for i in range(len(dp)):
            for j in range(i):
                if buildings[i] > buildings[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    res = max(res, dp[i])

        # 从右到左遍历
        dp = [1 for _ in range(len(buildings))]
        for i in range(len(dp)-1, -1, -1):
            for j in range(len(dp)-1, i, -1):
                if buildings[i] > buildings[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    res = max(res, dp[i])

        return res

if __name__ == '__main__':
    res = []
    solution = Solution()
    group = int(input())
    for i in range(group):
        num = int(input())
        buildings = list(map(int, input().split()))
        res.append(solution.Kiddo(buildings))

    for j in res:
        print(j)
