#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
# 思路：a xor a = 0  0 xor a = a
# 对于一个list的数字，每一位上面的0 1总量是固定的，所以xor顺序是无关的!其实and和or也是这样
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res = res ^ i
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.singleNumber([1])
    print solution.singleNumber([1, 2, 3, 2, 1])
    print solution.singleNumber([1, 2, 3, 3, 4, 6, 5, 6, 2, 1, 4])