#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one
 duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 1
        fast = len(nums)-1
        while slow < fast:
            mid, count1, count2 = slow + ((fast - slow) >> 1), 0, 0
            for num in nums:
                if num < mid:
                    count1 += 1
                elif num > mid:
                    count2 += 1
            if count1 >= mid:
                fast = mid-1
            elif count2 > len(nums)-1-mid:
                slow = mid+1
            else:
                return mid
        return slow