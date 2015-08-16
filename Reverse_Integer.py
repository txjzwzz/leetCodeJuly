#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if not x:
            return x
        flag = False if x < 0 else True
        x = abs(x)
        res = []
        while x != 0:
            res.append(x % 10)
            x = x / 10
        returnNum = 0
        for i in res:
            returnNum = returnNum * 10 + i
        if (returnNum > 2147483647 and flag) or (returnNum < -2147483648 and not flag):
            return 0
        return returnNum if flag else -returnNum

if __name__ == '__main__':
    solution = Solution()
    print solution.reverse(123)
    print solution.reverse(-123)
    print solution.reverse(0)
    print solution.reverse(1)