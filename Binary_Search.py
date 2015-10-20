#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
二分搜索
"""

class Solution:
    def binarySearch(self, nums, num):
        return self.binary_search(nums, num, 0, len(nums)-1)

    def binary_search(self, nums, num, p, q):
        if p > q:
            return None
        mid = p + ((q - p) >> 1)
        if nums[mid] == num:
            return mid
        elif nums[mid] > num:
            return self.binary_search(nums, num, p, mid-1)
        else:
            return self.binary_search(nums, num, mid+1, q)

if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print solution.binarySearch(nums, 0)
    print solution.binarySearch(nums, 1)
    print solution.binarySearch(nums, 2)
    print solution.binarySearch(nums, 3)
    print solution.binarySearch(nums, 4)
    print solution.binarySearch(nums, 5)
    print solution.binarySearch(nums, 6)
    print solution.binarySearch(nums, 7)
    print solution.binarySearch(nums, 8)
    print solution.binarySearch(nums, 9)