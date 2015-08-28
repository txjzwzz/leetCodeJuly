#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not(nums):
            return 0
        n_xor = 0
        for i in range(len(nums)+1):
            n_xor ^= i
        nums_xor = 0
        for i in nums:
            nums_xor ^= i
        return nums_xor ^ n_xor

if __name__ == '__main__':
    solution = Solution()
    print solution.missingNumber([0, 1, 3])
    print solution.missingNumber([1])
    print solution.missingNumber([0])