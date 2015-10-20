#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
class Solution(object):
    # def trap(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     if not height:
    #         return 0
    #     lMax = [0 for i in height]
    #     rMax = [0 for i in height]
    #     lMax[0] = height[0]
    #     rMax[-1] = height[-1]
    #     for index in range(1, len(height)):
    #         lMax[index] = max(lMax[index-1], height[index])
    #         rMax[len(height)-1-index] = max(rMax[len(height)-index], height[len(height)-1-index])
    #     res = 0
    #     for index in range(1, len(height)-1):
    #         res += min(lMax[index], rMax[index]) - height[index]
    #     return res
    def trap(self, height):
        l, r, level, res = 0, len(height)-1, 0, 0
        while l < r:
            if height[l] < height[r]:
                lower = height[l]
                l += 1
            else:
                lower = height[r]
                r -= 1
            level = max(level, lower)
            res += level - lower
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])