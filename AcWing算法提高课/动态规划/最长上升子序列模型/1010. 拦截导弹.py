#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/13
'''
某国为了防御敌国的导弹袭击，发展出一种导弹拦截系统。

但是这种导弹拦截系统有一个缺陷：虽然它的第一发炮弹能够到达任意的高度，但是以后每一发炮弹都不能高于前一发的高度。

某天，雷达捕捉到敌国的导弹来袭。

由于该系统还在试用阶段，所以只有一套系统，因此有可能不能拦截所有的导弹。

输入导弹依次飞来的高度（雷达给出的高度数据是不大于30000的正整数，导弹数不超过1000），计算这套系统最多能拦截多少导弹，如果要拦截所有导弹最少要配备多少套这种导弹拦截系统。

输入格式
共一行，输入导弹依次飞来的高度。

输出格式
第一行包含一个整数，表示最多能拦截的导弹数。

第二行包含一个整数，表示要拦截所有导弹最少要配备的系统数。

输入样例：
389 207 155 300 299 170 158 65
输出样例：
6
2
'''
# 首先，第一问是LIS问题
# 第二问，我们可以采用一种贪心策略
# 首先创建一个系统1（最起码得先有一个系统），然后遍历导弹
# 如果下一枚导弹大于目前所有系统的最后一个元素 missile[i] > system[j][-1] for j in len(system)
# 那么就新建一个系统，把该导弹填进去
# 如果下一枚导弹不全大于目前所有系统的最后一个元素
# 那么就挑一个 最小的且大于missile的     即 min(system[j][-1]) for j in len(system) and system[j][-1]>missile[i]

# 对于贪心的解法，一般我们是从直觉上先想一个解法，然后再去证实或者证伪它


# 贪心：
# 如何证明两个数相等？    A <= B 且 A >= B
# A表示贪心算法得到的序列个数    B表示最优解
# B <= A 这个首先无须证明
# 如何证明 A <= B？  调整法
# 首先假设最优解对应的方法和当前不同，找到第一个不同的数
#

from typing import List
class Solution:
    def defence_missiles(self, missiles: List[int]):
        res1 = 0
        dp = [1 for _ in range(len(missiles))]
        for i in range(len(dp)):
            for j in range(i):
                if missiles[i]<=missiles[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        res1 = max(dp)

        notebook = []   # notebook用来纪录每个system[k]的最低点，即system[k][-1]

        notebook.append(missiles[0])
        for i in range(1, len(missiles)):
            if missiles[i] > max(notebook):
                notebook.append(missiles[i])
            else:
                for k in range(len(notebook)):
                    if notebook[k]>missiles[i]:
                        notebook[k] = missiles[i]
                        break
        res2 = len(notebook)

        return [res1, res2]

if __name__ == '__main__':
    solution = Solution()
    # num = int(input())
    missiles = list(map(int, input().split()))
    res1, res2 = solution.defence_missiles(missiles)
    print(res1)
    print(res2)
