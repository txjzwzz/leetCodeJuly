#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
"""
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        if n <= 0:
            return False
        processDict = {}
        currentVal = n
        while True:
            tmpVal = self.getNextVal(currentVal)
            if tmpVal == 1:
                return True
            if tmpVal in processDict:
                return False
            processDict[tmpVal] = 1
            currentVal = tmpVal

    def getNextVal(self, val):
        res = 0
        while val != 0:
            tmpVal = val % 10
            res = res + tmpVal * tmpVal
            val = int(val / 10)
        return res

if __name__ == '__main__':
    solution = Solution()
    n = 19
    print solution.isHappy(19)