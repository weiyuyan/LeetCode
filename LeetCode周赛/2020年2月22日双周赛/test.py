#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/24
#
# a, b, c = input().split(' ')
#
# a = float(a)
# b = float(b)
# c = float(c)
# a_list = [a, b, c]
# a_list.sort()
# c,b,a = a_list[0],a_list[1],a_list[2]
#
# if a>= b+c:
#     print('NAO FORMA TRIANGULO')
# if a*a == b*b+c*c: print('TRIANGULO RETANGULO')
# if a*a > b*b+c*c: print('TRIANGULO OBTUSANGULO')
# if a*a < b*b+c*c: print('TRIANGULO ACUTANGULO')
# if a==b and b==c: print('TRIANGULO EQUILATERO')
# if (a==b and a!=c) or (a!=b and b==c):print("TRIANGULO ISOSCELES")

r = input()
r = float(r)
PAI = 3.1415926
res = PAI*r*r
print('A='+'%.2f' %res)