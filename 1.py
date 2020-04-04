#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/1
import re
tels = ["18791069830", "18867185616", "10086"]
for tel in tels:
    ret = re.match("1\d{9}[0-3,5-6,8-9]", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是可用的手机号" % tel)
