#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, node_left, node_right):
        if (not node_left and not node_right):
            return True
        if node_left and node_right and node_left.val == node_right.val:
            return self.dfs(node_left.left, node_right.right) and self.dfs(node_left.right, node_right.left)
        return False