#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/16
'''
给定一个模式串S，以及一个模板串P，所有字符串中只包含大小写英文字母以及阿拉伯数字。

模板串P在模式串S中多次作为子串出现。

求出模板串P在模式串S中所有出现的位置的起始下标。

输入格式
第一行输入整数N，表示字符串P的长度。

第二行输入字符串P。

第三行输入整数M，表示字符串S的长度。

第四行输入字符串S。

输出格式
共一行，输出所有出现位置的起始下标（下标从0开始计数），整数之间用空格隔开。

数据范围
1≤N≤10^4
1≤M≤10^5
输入样例：
3
aba
5
ababa
输出样例：
0 2
'''
# 核心：求next[]数组
# 对于模板串p[]，求一个next数组，next[i] = j，使得
# p[i, j] = p[i-j+1, j]，而且长度最长
# ______________________i
# ___________j
#            ___________j

# N = 10010
# M = 100010
# P = [0]*N
# S = [0]*M
# next = []
#
# if __name__ == '__main__':
#     n = input()
#     p = list(input().split())
#     m = input()
#     s = list(input().split())

from array import array
from sys import stdin

'''
 #include <iostream>

using namespace std;

const int M = 1e4 + 10, N = 1e5 + 10;

int m, n;
char p[M], s[N];
int ne[M];
//

int main() {
    cin >> m >> p + 1 >> n >> s + 1;

    //求ne数组
    for(int i = 2, j = 0; i <= m; i++) {
        while(j && p[i] != p[j + 1]) j = ne[j];
        if(p[i] == p[j + 1]) j++;
        ne[i] = j;
    }

    //kmp匹配
    for(int i = 1, j = 0; i <= n; i++) {
        while(j && s[i] != p[j + 1]) j = ne[j];
        if(s[i] == p[j + 1]) j++;
        if(j == m) {
            j = ne[j]; //当匹配成功时继续往下匹配
            printf("%d ", i - m);
        }
    }

    return 0;
}

'''
def get_dfa(word):
    n = len(word)
    # dfa = array('i', [-1]) * n
    dfa = [-1]*n
    i = 0
    j = -1
    while i < n - 1:
        if j == -1 or word[i] == word[j]:
            i += 1
            j += 1
            dfa[i] = j
        else:
            j = dfa[j]
    return dfa

def kmp(pattern, text, n, m):
    dfa = get_dfa(pattern)
    i = j = 0
    while i < m:
        if j == -1 or pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            j = dfa[j]
        if j == n:
            print(i-n, end=' ')
            j = dfa[j-1] + 1

def main():
    n = int(stdin.readline())
    pattern = stdin.readline().rstrip()
    m = int(stdin.readline())
    text = stdin.readline().rstrip()
    kmp(pattern, text, n, m)
    print()


if __name__ == "__main__":
    main()
