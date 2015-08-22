#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        b0, b1 = 0, 0
        for i in nums:
            b0 = (b0 ^ i) & (~b1)
            b1 = (b1 ^ i) & (~b0)
        return b0

if __name__ == '__main__':
    solution = Solution()
    print solution.singleNumber([1, 2, 3, 1, 2, 3, 1, 2, 4, 4, 5, 3, 4])
    print solution.singleNumber([1])
