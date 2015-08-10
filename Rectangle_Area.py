#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Assume that the total area is never beyond the maximum possible value of int.
"""
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if A > C or B > D or E > G or F > H:
            return 0
        area1 = (C-A) * (D-B)
        area2 = (G-E) * (H-F)
        xVal = min(C, G) - max(A, E)
        yVal = min(D, H) - max(B, F)
        if xVal <= 0 or yVal <= 0:
            return area1 + area2
        else:
            return area1 + area2 - xVal * yVal

if __name__ == '__main__':
    solution = Solution()
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    print solution.computeArea(A, B, C, D, E, F, G, H)
    print solution.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
