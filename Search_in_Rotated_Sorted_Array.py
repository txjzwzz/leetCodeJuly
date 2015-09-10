#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.binary_search(nums, target, 0, len(nums)-1)

    def binary_search(self, nums, target, p, q):
        if p > q:
            return -1
        mid = p + ((q-p) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            res = self.binary_search(nums, target,p, mid-1)
            if res == -1 and nums[q] < nums[mid]:
                return self.binary_search(nums, target, mid+1, q)
            else:
                return res
        else:
            res = self.binary_search(nums, target, mid+1, q)
            if res == -1 and nums[p] > nums[mid]:
                return self.binary_search(nums, target, p, mid-1)
            else:
                return res

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print solution.search(nums, 4)
    print solution.search(nums, 5)
    print solution.search(nums, 6)
    print solution.search(nums, 7)
    print solution.search(nums, 0)
    print solution.search(nums, 1)
    print solution.search(nums, 2)
    print solution.search(nums, 3)