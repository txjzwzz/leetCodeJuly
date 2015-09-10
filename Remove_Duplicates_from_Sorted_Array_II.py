#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter
what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start_index, duplicate = 0, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                duplicate = 1
            else:
                duplicate += 1
            if duplicate <= 2:
                start_index += 1
                nums[start_index] = nums[i]
        return start_index+1

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,2,2,3]
    print solution.removeDuplicates(nums)
    print nums
    nums = [1]
    print solution.removeDuplicates(nums)
    print nums
    nums = []
    print solution.removeDuplicates(nums)
    print nums