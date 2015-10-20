#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.search(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def search(self, inorder, postorder, i_in, j_in, i_post, j_post):
        if i_in > j_in:
            return None
        root = TreeNode(postorder[j_post])
        index = inorder.index(postorder[j_post], i_in, j_in+1)
        length = index - i_in
        root.left = self.search(inorder, postorder, i_in, i_in+length-1, i_post, i_post+length-1)
        root.right = self.search(inorder, postorder, i_in+length+1, j_in, i_post+length, j_post-1)
        return root