#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_length = 0
        for i in range(len(nums)):
            if i > max_length:
                return False
            max_length = max(max_length, i+nums[i])
        return True

if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    print solution.canJump(nums)
    nums = [3,2,1,0,4]
    print solution.canJump(nums)
    nums = []
    print solution.canJump(nums)
    nums = [0]
    print solution.canJump(nums)
    nums = [0, 1]
    print solution.canJump(nums)