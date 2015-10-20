#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前提应该是每个val都是unique？
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

    def buildTree1(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.search(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)

    def search(self, preorder, inorder, i_pre, j_pre, i_in, j_in):
        if i_pre > j_pre:
            return None
        root = TreeNode(preorder[i_pre])
        index = inorder.index(preorder[i_pre], i_in, j_in+1)
        length = index - i_in
        root.left = self.search(preorder, inorder, i_pre+1, i_pre+length, i_in, i_in+length-1)
        root.right = self.search(preorder, inorder, i_pre+length+1, j_pre, i_in+length+1, j_in)
        return root