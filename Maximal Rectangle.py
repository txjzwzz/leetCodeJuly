#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        height = [0 for i in matrix[0]]
        for i in matrix:
            for index, val in enumerate(i):
                height[index] = height[index] + 1 if val == "1" else 0
            res = max(res, self.largestRectangleArea(height))
        return res

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