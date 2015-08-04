#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very
right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

class MaxQueue:
    def __init__(self):
        self.valQueue = []
        self.maxQueue = []

    def enQueue(self, val):
        self.valQueue.append(val)
        while self.maxQueue and val > self.maxQueue[len(self.maxQueue)-1]:
            self.maxQueue.pop()
        self.maxQueue.append(val)

    def deQueue(self):
        if not self.valQueue:
            return -1
        popVal = self.valQueue[0]
        if popVal == self.maxQueue[0]:
            self.maxQueue = self.maxQueue[1:]
        self.valQueue = self.valQueue[1:]

    def getCurrentMax(self):
        if not self.maxQueue:
            return -1
        return self.maxQueue[0]

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        maxQueue = MaxQueue()
        if not nums:
            return []
        for i in range(0, k):
            maxQueue.enQueue(nums[i])
        res = [maxQueue.getCurrentMax()]
        for i in range(k, len(nums)):
            maxQueue.deQueue()
            maxQueue.enQueue(nums[i])
            res.append(maxQueue.getCurrentMax())
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print solution.maxSlidingWindow(nums, k)