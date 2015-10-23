#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_val = [-2147483648]
        self.findMaxVal(root, max_val)
        return max_val[0]

    def findMaxVal(self, root, max_val):
        if not root:
            return 0
        left = max(0, self.findMaxVal(root.left, max_val))
        right = max(0, self.findMaxVal(root.right, max_val))
        max_val[0] = max(max_val[0], left + right + root.val)
        return max(left, right) + root.val