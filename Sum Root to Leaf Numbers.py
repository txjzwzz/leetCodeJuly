#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = [0]
        self.dfs(root, 0, sum)
        return sum[0]

    def dfs(self, root, cur_val, sum):
        if not root:
            return
        cur_val = cur_val * 10 + root.val
        if not root.left and not root.right:
            sum[0] += cur_val
        if root.left:
            self.dfs(root.left, cur_val, sum)
        if root.right:
            self.dfs(root.right, cur_val, sum)