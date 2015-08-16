#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
"""
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        res = 0
        while num:
            res += num % 10
            res = res % 10 + res / 10
            num = num / 10
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.addDigits(38)
    print solution.addDigits(999)