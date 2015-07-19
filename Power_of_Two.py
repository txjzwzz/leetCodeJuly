#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n != 1:
            if n % 2 is not 0:
                return False
            n = n / 2
        return True

if __name__ == '__main__':
    solution = Solution()
    print solution.isPowerOfTwo(1)
    print solution.isPowerOfTwo(2)
    print solution.isPowerOfTwo(1024)
    print solution.isPowerOfTwo(1024* 1024)
    print solution.isPowerOfTwo(1023 * 1024)
    print solution.isPowerOfTwo(3)
    print solution.isPowerOfTwo(0)
    print solution.isPowerOfTwo(-1024)