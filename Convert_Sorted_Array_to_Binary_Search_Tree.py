#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(nums, 0, len(nums)-1)

    def build_tree(self, nums, p, q):
        if p > q:
            return None
        mid = p + ((q-p) >> 1)
        node = TreeNode(nums[mid])
        node.left = self.build_tree(nums, p, mid-1)
        node.right = self.build_tree(nums, mid+1, q)
        return node