#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        endIndex = len(nums)-2
        while endIndex >= 0 and nums[endIndex] >= nums[endIndex+1]:
            endIndex -= 1
        if endIndex < 0:
            nums.reverse()
            return
        tmp_min_index = len(nums)-1
        for i in range(tmp_min_index, endIndex, -1):
            if nums[i] > nums[endIndex]:
                tmp_min_index = i
                break
        nums[endIndex], nums[tmp_min_index] = nums[tmp_min_index], nums[endIndex]
        self.reverse(nums, endIndex+1, len(nums)-1)
        return

    def reverse(self, num, i, j):
        if i >= j:
            return
        for k in range(0, ((j-i)>>1)+1):
            num[i+k], num[j-k] = num[j-k], num[i+k]

if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    print nums
    nums = [4, 5, 2, 1]
    solution.nextPermutation(nums)
    print nums
    nums = [3, 5, 2, 1]
    solution.nextPermutation(nums)
    print nums
    nums = [1]
    solution.nextPermutation(nums)
    print nums
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print nums
    nums = [1, 3, 2]
    solution.nextPermutation(nums)
    print nums
    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    print nums
    nums = [5, 1, 1]
    solution.nextPermutation(nums)
    print nums


