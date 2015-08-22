#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = [len(nums), -1]
        self.binarySearch(nums, target, 0, len(nums)-1, index)
        return index if index[1] != -1 else [-1, -1]

    def binarySearch(self, nums, target, i, j, index):
        if i > j:
            return
        mid = i + ((j-i) >> 1)
        if nums[mid] < target:
            self.binarySearch(nums, target, mid+1, j, index)
        elif nums[mid] > target:
            self.binarySearch(nums, target, i, mid-1, index)
        else:
            index[0] = min(index[0], mid)
            index[1] = max(index[1], mid)
            if mid-1>=0 and nums[mid-1] == target:
                self.binarySearch(nums, target, i, mid-1, index)
            if mid+1 <= len(nums)-1 and nums[mid+1] == target:
                self.binarySearch(nums, target, mid+1, j, index)

if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    print solution.searchRange(nums, 8)
    print solution.searchRange(nums, 7)
    print solution.searchRange(nums, 6)
    nums = []
    print solution.searchRange(nums, 0)
    nums = [5]
    print solution.searchRange(nums, 0)
    print solution.searchRange(nums, 5)
    nums = [2, 2]
    print solution.searchRange(nums, 2)