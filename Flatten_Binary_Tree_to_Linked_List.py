#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.dfs(root)

    # return end node
    def dfs(self, root):
        if not root:
            return None
        end_node = root
        if root.left:
            end_node = self.dfs(root)
            tmp = root.right
            root.right = root.left
            end_node.right = tmp
        if root.right:
            return self.dfs(root.right)
        return end_node
