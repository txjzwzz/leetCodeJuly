#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        return self.binarySearch(nums, 0, len(nums)-1, target)


    def binarySearch(self, nums, i, j, target):
        if i > j:
            return -1
        mid = i + ((j-i)>>1)
        if nums[mid] > target:
            if mid > 0:
                if nums[mid-1] < target:
                    return mid
                else:
                    return self.binarySearch(nums, i, mid-1, target)
            else:
                return 0
        elif nums[mid] < target:
            if mid < len(nums)-1:
                if nums[mid+1] > target:
                    return mid+1
                else:
                    return self.binarySearch(nums, mid+1, j, target)
            else:
                return len(nums)
        else:
            return mid

if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,5,6]
    print solution.searchInsert(nums, 5)
    print solution.searchInsert(nums, 2)
    print solution.searchInsert(nums, 7)
    print solution.searchInsert(nums, 0)
    nums = [1]
    print solution.searchInsert(nums, 0)
    print solution.searchInsert(nums, 2)
    nums = [1, 3]
    print solution.searchInsert(nums, 2)
    print solution.searchInsert(nums, 4)
    print solution.searchInsert(nums, 0)