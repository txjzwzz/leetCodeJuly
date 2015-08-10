#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        eleDict = {}
        for i in range(len(nums)):
            if target - nums[i] in eleDict:
                return [min(eleDict[target-nums[i]], i+1), max(eleDict[target-nums[i]], i+1)]
            else:
                eleDict[nums[i]] = i+1
        return []

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print solution.twoSum(nums, target)