#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        return self.binary_search(nums, target, 0, len(nums)-1)

    def binary_search(self, nums, target, p, q):
        if p > q:
            return False
        mid = p + ((q-p) >> 1)
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            res = self.binary_search(nums, target,p, mid-1)
            if res == False and nums[q] <= nums[mid]:
                return self.binary_search(nums, target, mid+1, q)
            else:
                return res
        else:
            res = self.binary_search(nums, target, mid+1, q)
            if res == False and nums[p] >= nums[mid]:
                return self.binary_search(nums, target, p, mid-1)
            else:
                return res


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 0, 0, 0, 0, 1, 1, 2, 3]
    print solution.search(nums, 4)
    print solution.search(nums, 5)
    print solution.search(nums, 6)
    print solution.search(nums, 7)
    print solution.search(nums, 0)
    print solution.search(nums, 1)
    print solution.search(nums, 2)
    print solution.search(nums, 3)
    print solution.search(nums, 8)