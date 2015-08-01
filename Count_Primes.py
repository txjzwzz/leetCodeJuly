#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
from math import sqrt
class Solution:
    # @param {integer} n
    # @return {integer}
    """
    超时
    def countPrimes(self, n):
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, value):
        for i in range(2, int(sqrt(value))+1):
            if value % i == 0:
                return False
        return True
    """
    def countPrimes(self, n):
        if n <= 0:
            return 0
        matrix = [True for i in range(n)]
        if n >= 1:
            matrix[0] = False
        if n >= 2:
            matrix[1] = False
        for i in range(2, int(sqrt(n))+1):
            if matrix[i]:
                for j in range(i*2, n, i):
                    matrix[j] = False
        count = 0
        for i in range(0, n):
            if matrix[i]:
                count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    print solution.countPrimes(2)
    print solution.countPrimes(3)
    print solution.countPrimes(4)
    print solution.countPrimes(5)
    print solution.countPrimes(6)
    print solution.countPrimes(7)
    print solution.countPrimes(499979)