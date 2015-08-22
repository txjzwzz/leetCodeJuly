#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        startIndex = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                startIndex += 1
                nums[startIndex] = nums[i]
        return startIndex+1