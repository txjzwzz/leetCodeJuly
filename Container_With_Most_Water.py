#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0
        startIndex = 0
        endIndex = len(height)-1
        res = 0
        while startIndex < endIndex:
            res = max(res, min(height[startIndex], height[endIndex]) * (endIndex - startIndex))
            if height[startIndex] < height[endIndex]:
                startIndex += 1
            elif height[startIndex] > height[endIndex]:
                endIndex -= 1
            else:
                startIndex += 1
                endIndex -= 1
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.maxArea([1, 1])
    print solution.maxArea([1, 1, 1])
    print solution.maxArea([1, 2, 3, 1])