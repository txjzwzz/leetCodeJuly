#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        startIndex = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]-1:
                if i != startIndex:
                    res.append("{}->{}".format(nums[startIndex], nums[i]))
                else:
                    res.append("{}".format(nums[i]))
                startIndex = i + 1
        if startIndex != len(nums)-1:
            res.append("{}->{}".format(nums[startIndex], nums[len(nums)-1]))
        else:
            res.append("{}".format(nums[len(nums)-1]))
        return res

if __name__ == '__main__':
    solution = Solution()
    nums1 = [0, 1, 2, 4, 5, 7]
    nums2 = [1, 3, 5, 7, 9]
    nums3 = [1, 3, 5, 7, 8, 9, 10]
    print solution.summaryRanges(nums1)
    print solution.summaryRanges(nums2)
    print solution.summaryRanges(nums3)