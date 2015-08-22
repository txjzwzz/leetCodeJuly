#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        endIndex = len(nums)
        startIndex = 0
        while startIndex < endIndex:
            if nums[startIndex] == val:
                endIndex -= 1
                nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
            else:
                startIndex += 1
        return endIndex

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    val = 5
    solution = Solution()
    print solution.removeElement(nums, val)
    print nums
    nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    val = 7
    print solution.removeElement(nums, val)
    print nums
    nums = [1, 1, 1]
    val = 1
    print solution.removeElement(nums, val)
    print nums
    nums = [1]
    val = 1
    print solution.removeElement(nums, val)
    print nums