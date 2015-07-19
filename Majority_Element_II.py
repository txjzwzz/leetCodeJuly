#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
思路仍然是Majority Element的思路，进行削减。但是要在之后进行一次搜索，看看是否满足出现次数的限制
有时候有些事情不是要一次全部搞定的
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        res = []
        a, b, countA, countB = 0, 0, 0, 0
        for i in nums:
            if i == a:
                countA += 1
            elif i == b:
                countB += 1
            elif countA == 0 :
                countA += 1
                a = i
            elif countB == 0:
                countB += 1
                b = i
            else:
                countA -= 1
                countB -= 1
        countA, countB = 0, 0
        for i in nums:
            if i == a:
                countA += 1
            elif i == b:
                countB += 1
        if countA > len(nums) / 3:
            res.append(a)
        if countB > len(nums) / 3:
            res.append(b)
        return res

if __name__ == '__main__':
    nums1 = [1]
    nums2 = [1, 2]
    nums3 = [1, 1, 2, 2, 3, 3]
    nums4 = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3]
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums6 = [1, 2, 3, 4, 3, 2, 1, 3, 2, 3, 2]
    solution = Solution()
    print solution.majorityElement(nums1)
    print solution.majorityElement(nums2)
    print solution.majorityElement(nums3)
    print solution.majorityElement(nums4)
    print solution.majorityElement(nums5)
    print solution.majorityElement(nums6)
