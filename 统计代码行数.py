#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/13
# -*- coding: utf-8 -*-
import os

# 需要统计的文件类型
exts = ['.py']
# 排除的文件夹
excludes = ["E:\PycharmProjects\test002\.idea"]


def get_line_count(file_name):
    line_count = 0
    with open('code_line_count.txt', 'a') as f:
        f.write('file_name : %s \n' % file_name)
    with open(file_name, 'r', encoding='utf8') as f:
        for file_line in f.readlines():
            file_line = file_line.strip()
            # if not len(file_line) or file_line.startswith('//'):
            #     continue
            line_count += 1
    with open('code_line_count.txt', 'a') as f:
        f.write('line count::%s\n' % line_count)
    return line_count


if __name__ == '__main__':
    with open('code_line_count.txt', 'w') as f:
        f.write('\n')
    count = 0
    file_count = 0
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            file_name = (root+'\\'+f)
            print(file_name)

            if os.path.dirname(file_name).split()[0] not in excludes:
                if os.path.splitext(f)[1]:
                    ext = f[f.rindex('.'):]
                    try:
                        if exts.index(ext) >= 0:
                            file_count += 1
                            c = get_line_count(file_name)
                            count += c
                            with open('code_line_count.txt', 'a') as f:
                                f.write('total count:%s\n' % count)
                    except:
                        pass

    with open('code_line_count.txt', 'a') as f:
        f.write('\n')
        f.write('--------------------------------------\n')
        f.write('total file count:%d\n' % file_count)
        f.write('total line count:%d\n' % count)

    import datetime
    with open('code_line_count_everyday.txt', 'a') as f:
        f.write('\n')
        f.write('--------------------------------------\n')
        now = datetime.datetime.now()
        now = str(now)
        f.write('date: ' + now +'\n')
        f.write('total file count:%d\n' % file_count)
        f.write('total line count:%d\n' % count)