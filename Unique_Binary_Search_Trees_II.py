#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1, n)

    def dfs(self, i, j):
        if i == j:
            return [TreeNode(i)]
        if i > j:
            return [None]
        ans = []
        for k in range(i, j+1):
            left_ans = self.dfs(i, k-1)
            right_ans = self.dfs(k+1, j)
            if left_ans and right_ans:
                for lnode in left_ans:
                    for rnode in right_ans:
                        head = TreeNode(k)
                        head.left = lnode
                        head.right = rnode
                        ans.append(head)
        return ans