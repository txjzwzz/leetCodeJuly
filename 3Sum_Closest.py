#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3:
            return -1
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-2):
            res = self.findClosest(nums, target-nums[i], i)
            if abs(target-(nums[i]+res)) < abs(target-ans):
                ans = nums[i] + res
        return ans

    def findClosest(self, nums, target, startIndex):
        secondIndex = startIndex + 1
        thirdIndex = len(nums) - 1
        res = nums[secondIndex] + nums[thirdIndex]
        while secondIndex < thirdIndex:
            if abs(target - (nums[secondIndex] + nums[thirdIndex])) < abs(target-res):
                res = nums[secondIndex] + nums[thirdIndex]
            if nums[secondIndex] + nums[thirdIndex] > target:
                thirdIndex -= 1
            elif nums[secondIndex] + nums[thirdIndex] < target:
                secondIndex += 1
            else:
                return target
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.threeSumClosest([-1,2,1,-4], 1)
    print solution.threeSumClosest([0, 2, 1, -3], 1)