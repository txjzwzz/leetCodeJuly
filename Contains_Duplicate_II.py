#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dictionary = {}
        for i in range(len(nums)):
            if dictionary.has_key(nums[i]) and abs(i - dictionary[nums[i]]) <= k:
                return True
            dictionary[nums[i]] = i
        return False

if __name__ == '__main__':
    a = []
    b = [1, 2, 3]
    k = 3
    c=  [1, 2, 3, 1]
    d = [1, 2, 3, 4, 1, 2, 3, 4]
    solution = Solution()
    print solution.containsNearbyDuplicate(a, k)
    print solution.containsNearbyDuplicate(b, k)
    print solution.containsNearbyDuplicate(c, k)
    print solution.containsNearbyDuplicate(d, k)