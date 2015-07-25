#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
You may assume that the given expression is always valid.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        valList = []
        opList = []
        for i in s:
            if i == '+':
                opList.append(i)
            elif i == '-':
                opList.append(i)
            elif opList == '*':
