#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits)-1
        while index >= 0 and digits[index] == 9:
            digits[index] = 0
            index -= 1
        if index < 0:
            res = [1]
            res.extend(digits)
            return res
        digits[index] += 1
        return digits

if __name__ == '__main__':
    digits = [9, 9, 9]
    solution = Solution()
    print solution.plusOne(digits)
    print solution.plusOne([1])
    print solution.plusOne([1,2,3])
    print solution.plusOne([9])