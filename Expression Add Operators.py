#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not
unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, len(num)+1):
            if num[0] == "0" and i > 1:
                continue
            val = long(num[0:i])
            self.dfs(str(val), res, num, i, "#", target, val, val)

    def dfs(self, path, res, num, index, op, target, cur, pre_val):
        if index == len(num):
            if cur == target:
                res.append(path)
            return
        for i in range(index+1, len(num)+1):
            if num[index] == "0" and i - index > 1:
                continue
            val = long(num[index:i])
            self.dfs(path + "+" + val, res, num, i, "+", target, cur + val, val)
            self.dfs(path + "-" + val, res, num, i, "-", target, cur - val, val)
            if op == "-":
                self.dfs(path + "*" + val, res, num, i, "-", target, cur + pre_val - pre_val * val, pre_val * val)
            elif op == "+":
                self.dfs(path + "*" + val, res, num, i, "+", target, cur - pre_val + pre_val * val, pre_val * val)
            else:
                self.dfs(path + "*" + val, res, num, i, "*", target, cur * val, val)