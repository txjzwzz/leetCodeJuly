#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
对比str转为list相加再转为str的效率和str直接相加的效率
"""

def str_add1():
    ori = "abcdefghijklmn"
    for i in range(10000):
        ori += 'a'

def str_add2():
    ori = "abcdefghijklmn"
    ori_list = list(ori)
    for i in range(10000):
        ori_list.append('a')
    "".join(ori_list)

if __name__=='__main__':
    from timeit import Timer
    t1 = Timer("str_add1()", "from __main__ import str_add1")
    t2 = Timer("str_add2()", "from __main__ import str_add2")
    print t1.timeit(10000)
    print t2.timeit(10000)