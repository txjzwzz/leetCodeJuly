#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
利用队列打印二项展开式的系数
"""
class Solution:
    def YangVI(self, n):
        Queue = [0 for i in range(n+1)]
        