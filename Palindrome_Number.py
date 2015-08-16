#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        val = x
        if x < 0:
            return False
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
        return res == val

if __name__ == '__main__':
    solution = Solution()
    print solution.isPalindrome(1)