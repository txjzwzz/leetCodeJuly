#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which
the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        startIndex = 0
        endIndex = 0
        sumVal = nums[0]
        while endIndex+1 < len(nums) and sumVal < s:
            endIndex += 1
            sumVal += nums[endIndex]
        if sumVal < s:
            return 0
        while sumVal - nums[startIndex] >= s:
            sumVal = sumVal - nums[startIndex]
            startIndex += 1
        res = endIndex + 1 - startIndex
        while endIndex+1 < len(nums):
            endIndex += 1
            sumVal += nums[endIndex]
            while sumVal - nums[startIndex] >= s:
                sumVal = sumVal - nums[startIndex]
                startIndex += 1
            if endIndex + 1 - startIndex < res:
                res = endIndex + 1 - startIndex
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    print solution.minSubArrayLen(s, nums)
    s = 15
    print solution.minSubArrayLen(s, nums)
    s = 16
    print solution.minSubArrayLen(s, nums)
    s = 1
    print solution.minSubArrayLen(s, nums)
    s = 4
    nums = [1, 4, 4]
    print solution.minSubArrayLen(s, nums)
    s = 11
    nums = [1, 2, 3, 4, 5]
    print solution.minSubArrayLen(s, nums)