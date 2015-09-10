#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        tmp_res, res = [], []
        self.get_permutations(0, nums, tmp_res, res)
        return res

    def get_permutations(self, i, nums, tmp_res, res):
        if i == len(nums):
            res.append(tmp_res[:])
            return
        tmp_res.append(nums[i])
        self.get_permutations(i+1, nums, tmp_res, res)
        tmp_res.pop()
        self.get_permutations(i+1, nums, tmp_res, res)

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print solution.subsets(nums)
    print solution.subsets([])