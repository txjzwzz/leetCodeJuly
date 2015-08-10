#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Invert a binary tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return None
        tmpNode = root.left
        root.left = root.right
        root.right = tmpNode
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == '__main__':
    solution = Solution()
