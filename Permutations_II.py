#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = [nums[:]]
        while True:
            endIndex = len(nums)-1
            while endIndex > 0 and nums[endIndex] <= nums[endIndex-1]:
                endIndex -= 1
            if endIndex == 0:
                return res
            tmp_min_index = len(nums)-1
            for i in range(len(nums)-1, endIndex-1, -1):
                if nums[i] > nums[endIndex-1]:
                    tmp_min_index = i
                    break
            nums[endIndex-1], nums[tmp_min_index] = nums[tmp_min_index], nums[endIndex-1]
            self.reverse(nums, endIndex, len(nums)-1)
            res.append(nums[:])

    def reverse(self, nums, i, j):
        if i >= j:
            return
        for k in range(0, ((j-i)>>1)+1):
            nums[i+k], nums[j-k] = nums[j-k], nums[i+k]