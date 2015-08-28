#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        step = [0 for i in range(length)]
        max_length = 0
        for i in range(len(nums)):
            if i + nums[i] <= max_length:
                continue
            if i + nums[i] >= length-1:
                return step[i] + 1 if i != length-1 else step[i]
            for j in range(max_length+1, i+nums[i]+1):
                step[j] = step[i] + 1
            max_length = i + nums[i]
        return step[length-1]

if __name__ == '__main__':
    solution = Solution()
    A = [2,3,1,1,4]
    print solution.jump(A)
    A = [1,1,1,1,1,1,1]
    print solution.jump(A)
    A = []
    print solution.jump(A)
    A = [1]
    print solution.jump(A)
    A = [2,1]
    print solution.jump(A)