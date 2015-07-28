#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that
the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    # 光进行排序和比较也不行，毕竟仅仅和相邻的比较是不够的！
    # 不用和过去的比，因为过去的已经和自己比过了！但是这么处理了还是超时
    # 复杂度为O(kn)会超时，只能想办法在k上面下手了
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums or k < 0 or t < 0:
            return False
        for i in range(len(nums)):
            endIndex = min(len(nums)-1, i + k) + 1
            for j in range(i+1, endIndex):
                if abs(nums[j] - nums[i]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums or k < 0 or t < 0:
            return False
        if k >= len(nums):
            k = len(nums) - 1
        if k > t:
            return self.TOper(nums, k, t)
        else:
            return self.KOper(nums, k, t)

    def TOper(self, nums, k, t):
        dictionary = {}
        for i in range(len(nums)):
            for j in range(nums[i] - t, nums[i] + t + 1):
                if dictionary.has_key(j) and abs(i - dictionary[j]) <= k:
                    return True
            dictionary[nums[i]] = i
        return False

    def KOper(self, nums, k, t):
        for i in range(len(nums)):
            endIndex = min(len(nums)-1, i + k) + 1
            for j in range(i+1, endIndex):
                if abs(nums[j] - nums[i]) <= t:
                    return True
        return False
    """
    # 新的思路：利用除以t减少t的搜索！
    # 但是这样做的话，dict后面的val就得是一个list了！
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums or k < 0 or t < 0:
            return False
        if t == 0:
            return self.containsNearbyDuplicate(nums, k)
        remains = [i % t for i in nums]
        div = [i / t for i in nums]
        dictionary = {}
        for i in range(len(nums)):
            if dictionary.has_key(div[i]):
                for j in dictionary[div[i]]:
                    if abs(j - i) <= k:
                        return True
                dictionary[div[i]].append(i)
            else:
                dictionary[div[i]] = [i]
            if dictionary.has_key(div[i]-1):
                for j in dictionary[div[i]-1]:
                    if remains[j] >= remains[i] and abs(j - i) <= k:
                        return True
            if dictionary.has_key(div[i]+1):
                for j in dictionary[div[i]+1]:
                    if remains[j] <= remains[i] and abs(j - i) <= k:
                        return True
        return False


    def containsNearbyDuplicate(self, nums, k):
        dictionary = {}
        for i in range(len(nums)):
            if dictionary.has_key(nums[i]) and abs(i - dictionary[nums[i]]) <= k:
                return True
            dictionary[nums[i]] = i
        return False


if __name__ == '__main__':
    a = []
    b = [1, 4, 7, 10, 13, 19]
    t = 2
    k = 3
    solution = Solution()
    print solution.containsNearbyAlmostDuplicate(a, k, t)
    print solution.containsNearbyAlmostDuplicate(b, k, t)
    t = 3
    print solution.containsNearbyAlmostDuplicate(b, k, t)
    d = [1,2]
    k = 0
    t = 1
    print solution.containsNearbyAlmostDuplicate(d, k, t)
    print solution.containsNearbyAlmostDuplicate([], 0, 0)
