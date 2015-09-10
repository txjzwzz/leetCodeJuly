#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        totalset = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            count = 0
            while count+i < len(nums) and nums[count+i] == nums[i]:
                count += 1
            previousN = len(totalset)
            for k in range(0, previousN):
                instance = totalset[k][:]
                for j in range(0, count):
                    instance.append(nums[i])
                    totalset.append(instance[:])
            i += count
        return totalset

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2]
    print solution.subsetsWithDup(nums)