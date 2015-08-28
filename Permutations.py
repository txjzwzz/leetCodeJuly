#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""
class Solution(object):
    def permute(self, nums):
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
            for k in range(0, ((len(nums)-1-endIndex)>>1)+1):
                nums[endIndex+k], nums[len(nums)-1-k] = nums[len(nums)-1-k], nums[endIndex+k]
            res.append(nums[:])

    def reverse(self, nums, i, j):
        if i >= j:
            return
        for k in range(0, ((j-i)>>1)+1):
            nums[i+k], nums[j-k] = nums[j-k], nums[i+k]




if __name__ == '__main__':
    solution = Solution()
    print solution.permute([1, 3, 2])
    print solution.permute([1, 3, 2, 4])
    print solution.permute([1, 3, 1])
    print solution.permute([1, 1])
    print solution.permute([1, 2, 2, 2])
