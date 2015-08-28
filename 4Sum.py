#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    """
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res = []
        ansHash = {}
        for i in range(len(nums)-1, -1, -1):
            tmpRes = self.threeSum(nums[:i], target-nums[i])
            if tmpRes:
                for tmp in tmpRes:
                    tmp.append(nums[i])
                    tmpVal = self.getVal(tmp)
                    if tmpVal not in ansHash:
                        ansHash[tmpVal] = 1
                        res.append(tmp)
        return res

    def threeSum(self, nums, target):
        if not nums:
            return []
        res = []
        ansHash = {}
        for i in range(len(nums)-1, -1, -1):
            tmpRes = self.twoSum(nums[:i], target-nums[i])
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
    """
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []
        res = []
        ans_hash = {}
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                tmpTarget = target - nums[i] - nums[j]
                tmpRes = self.twoSum(nums[j+1:], tmpTarget)
                if tmpRes:
                    for tmp in tmpRes:
                        tmp = [nums[i], nums[j]] + tmp
                        tmpVal = self.getVal(tmp)
                        if tmpVal not in ans_hash:
                            res.append(tmp)
                            ans_hash[tmpVal] = 1
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
    print solution.fourSum([1, 0, -1, 0, -2, 2], 0)