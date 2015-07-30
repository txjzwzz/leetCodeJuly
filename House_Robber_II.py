#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Note: This is an extension of House Robber.
After robbing those houses on that street, the thief has found himself a new place for his thievery so that
he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the
first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for
those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        matrix = [0 for i in nums]
        # 用第一个
        matrix[0] = nums[0]
        if len(nums) > 1:
            matrix[1] = nums[0]
        for i in range(2, len(nums)-1):
            matrix[i] = max(matrix[i-1], matrix[i-2] + nums[i])
        tmpMax1 = matrix[len(nums)-1]
        # 不用第一个
        matrix[0] = 0
        if len(nums) > 1:
            matrix[1] = nums[1]
        for i in range(2, len(nums)):
            matrix[i] = max(matrix[i-1], matrix[i-2] + nums[i])
        return max(tmpMax1, matrix[len(nums)-1])

if __name__ == '__main__':

    nums = [1, 2]
    solution = Solution()
    print solution.rob(nums)
    nums = [1, 2, 3]
    print solution.rob(nums)
    nums = [1, 2, 3, 4]
    print solution.rob(nums)
    nums = [1, 2, 3, 4, 5]
    print solution.rob(nums)
    nums = [0]
    print solution.rob(nums)
    nums = [2, 1, 1, 1]
    print solution.rob(nums)