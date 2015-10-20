#-*- coding-utf-8 -*-
__author__ = 'zz'
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area
of largest rectangle in the histogram.
"""
class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = [0 for i in height]
        top, max_area, index = -1, 0, 0
        while index < len(height):
            if top < 0 or height[index] >= height[stack[top]]:
                top += 1
                stack[top] = index
                index += 1
            else:
                tmp = stack[top]
                top -= 1
                max_area =  max(max_area, height[tmp] * (index if top < 0 else index - stack[top] - 1))
        while top >= 0:
            tmp = stack[top]
            top -= 1
            max_area = max(max_area, height[tmp] * (len(height) if top < 0 else len(height) - stack[top] - 1))
        return max_area