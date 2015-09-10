#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
class Solution(object):
    # def sortColors(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     index_0 = -1
    #     index_2 = len(nums)
    #     for i in range(len(nums)):
    #         if nums[i] == 0:
    #             index_0 += 1
    #             nums[index_0], nums[i] = nums[i], nums[index_0]
    #     i = len(nums)-1
    #     while i > index_0:
    #         if nums[i] == 2:
    #             index_2 -= 1
    #             nums[i], nums[index_2] = nums[index_2], nums[i]
    #         i -= 1

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        point0 = -1
        point1 = 0
        point2 = len(nums)
        while point1 < point2:
            if nums[point1] == 0:
                point0 += 1
                nums[point0], nums[point1] = nums[point1], nums[point0]
                # important here!
                point1 += 1
            elif nums[point1] == 2:
                point2 -= 1
                nums[point1], nums[point2] = nums[point2], nums[point1]
            else:
                point1 += 1


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 0, 1, 2]
    solution.sortColors(nums)
    print nums
    nums = [0]
    solution.sortColors(nums)
    print nums
    nums = [2]
    solution.sortColors(nums)
    print nums
    nums = []
    solution.sortColors(nums)
    print nums