#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.dfs(root, 1, res)
        return res[0]

    def dfs(self, root, level, res):
        if not root:
            return
        if not root.left and not root.right and level > res[0]:
            res[0] = level
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)