#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.find_path(root, 0, [], sum, res)
        return res

    def find_path(self, root, tmp_sum, path, sum, res):
        if not root:
            return
        current_sum = tmp_sum + root.val
        path.append(root.val)
        if not root.left and not root.right and current_sum == sum:
            res.append(path[:])
        else:
            self.find_path(root.left, current_sum, path, sum, res)
            self.find_path(root.right, current_sum, path, sum, res)
        path.pop()