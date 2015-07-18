#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of n integers where n > 1, nums, return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].
Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6].

思路：其实res[i]就是所有小于其的数的积乘以大于其的数的乘积
所以用两个队列，一个队列的less[i]存从1到i的乘积，more[i]存从i到n的乘积
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        less = [0 for i in range(len(nums))]
        more = [0 for i in range(len(nums))]
        tmp = 1
        for i in range(len(nums)):
            less[i] = tmp * nums[i]
            tmp = less[i]
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            more[i] = tmp * nums[i]
            tmp = more[i]
        res = [0 for i in range(len(nums))]
        res[0] = more[1]
        res[len(nums)-1] = less[len(nums)-2]
        for i in range(1, len(nums)-1):
            res[i] = less[i-1] * more[i+1]
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2]
    print solution.productExceptSelf(nums)
    nums = [1, 2, 3, 4]
    print solution.productExceptSelf(nums)
