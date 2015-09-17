#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = [True]
        self.balanced_height(root, res)
        return res[0]

    def balanced_height(self, root, res):
        if not root or not res[0]:
            return 0
        height_left = self.balanced_height(root.left, res)+1
        height_right = self.balanced_height(root.right, res)+1
        if abs(height_left-height_right) > 1:
            res[0] = False
        return max(height_left, height_right)