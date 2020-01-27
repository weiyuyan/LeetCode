#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/24
'''
单例模式,核心结构中只包含一个被称为单例类的特殊类,类的对象只能存在一个
三个要点: 某个类只有一个实例; 必须自行创建这个实例; 必须自行向整个系统提供这个实例
'''

'''
方法一：实现__new__方法,然后将类的一个实例绑定到类变量_instance上
如果cls._instance为None, 说明该类没有被实例化过, new一个该类的实例,并返回
如果cls._instance不是None, 直接返回_instance
'''
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class Myclass(Singleton):
    a = 1

one = Myclass()
two = Myclass()

print(id(one))
print(id(two))
print(one == two)
print(one is two)

two.a = 3
print(id(one))
print(id(two))