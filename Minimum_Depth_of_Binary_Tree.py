#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [2147483647]
        self.find_height(root, 0, res)
        return res[0]

    def find_height(self, root, height, res):
        if not root:
            return
        height += 1
        if height < res[0]:
            if not root.left and not root.right:
                res[0] = height
            else:
                self.find_height(root.left, height, res)
                self.find_height(root.right, height, res)