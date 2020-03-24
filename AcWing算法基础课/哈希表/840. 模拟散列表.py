#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/18
'''
维护一个集合，支持如下几种操作：

“I x”，插入一个数x；
“Q x”，询问数x是否在集合中出现过；
现在要进行N次操作，对于每个询问操作输出对应的结果。

输入格式
第一行包含整数N，表示操作数量。

接下来N行，每行包含一个操作指令，操作指令为”I x”，”Q x”中的一种。

输出格式
对于每个询问指令“Q x”，输出一个询问结果，如果x在集合中出现过，则输出“Yes”，否则输出“No”。

每个结果占一行。

数据范围
1≤N≤10^5
−10^9≤x≤10^9
输入样例：
5
I 1
I 2
I 3
Q 2
Q 5
输出样例：
Yes
No
'''
# 哈希表：
# 存储结构：1、开放寻址法  2、拉链法（处理冲突的方法有这两种）
# 如果是开放寻址法，最好取一个质数，而且质数最好离2的整次幂最远
# 字符串哈希方式

# 寻找一个质数（比如取100000以上最小的一个质数）
import math
def find_prime(num):
    while(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                break
        if num % i != 0: return num
        num += 1

N = 100003
idx = 0
h = [0]*N
e = [0]*N
ne = [0]*N
def insert(x):
    global idx
    k = (x%N + N)%N #这里是为了保证余数为正数
    e[idx] = x
    ne[idx] = h[k]
    h[k] = idx
    idx += 1

def find(x):
    k = (x%N +N)%N
    i = h[k]
    while(i!=-1):


if __name__ == '__main__':
    res = find_prime(100000)
    print(res)