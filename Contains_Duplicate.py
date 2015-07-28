#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of integers, find if the array contains any duplicates. Your function should return true
if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dictionary = {}
        for i in nums:
            if dictionary.has_key(i):
                return True
            dictionary[i] = 1
        return False

if __name__ == '__main__':
    a = []
    b = [1, 2, 3, 4, 5, 6]
    c = [1, 6, 0, 9, 1, 8, 7]
    solution = Solution()
    print solution.containsDuplicate(a)
    print solution.containsDuplicate(b)
    print solution.containsDuplicate(c)