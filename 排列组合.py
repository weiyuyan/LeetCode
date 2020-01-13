#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/13

from typing import List

result = []
def generate(s: str, n: int) -> List:
    if n == 0:
        result.append(s)
    else:
        generate(s+'(', n-1)
        generate(s+')', n-1)

if __name__ == '__main__':
    generate('', 6)
    print(result)