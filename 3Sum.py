#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if not nums:
            return []
        nums.sort()
        res = []
        ansHash = {}
        for i in range(len(nums)-1, -1, -1):
            tmpRes = self.twoSum(nums[:i], 0-nums[i])
            if tmpRes:
                for tmp in tmpRes:
                    tmp.append(nums[i])
                    tmpVal = self.getVal(tmp)
                    if tmpVal not in ansHash:
                        ansHash[tmpVal] = 1
                        res.append(tmp)
        return res


    def twoSum(self, nums, target):
        res = []
        eleDict = {}
        for i in nums:
            if target - i in eleDict:
                res.append([target-i, i])
            else:
                eleDict[i] = 1
        return res

    def getVal(self, resList):
        tmpList = [str(i) for i in resList]
        return ''.join(tmpList)

if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print solution.threeSum(nums)
    nums = [-1, -1, -1, -1, -1, 2, 2, 2]
    print solution.threeSum(nums)
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print solution.threeSum(nums)