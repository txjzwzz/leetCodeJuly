#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这里其实利用了前序遍历，把二叉搜索树是否合法的问题转换为了在前序遍历中，后一个结点必须比前一个结点大的问题！
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = None
        return self.dfs(root, prev)

    def dfs(self, root, prev_root):
        if not root:
            return True
        if (not root.left or self.dfs(root.left, prev_root)) and (not prev_root or root.val > prev_root.val):
            prev_root = root
            return not root.right or self.dfs(root.right, prev_root)
        return False