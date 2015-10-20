#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res

    # level start from 0
    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) <= level:
            res.append([root.val])
        else:
            res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)

    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, queue, level = [], [root], 0
        while queue:
            tmp_queue = []
            for i in queue:
                if len(res) <= level:
                    res.append([i.val])
                else:
                    res[level].append(i.val)
                if i.left:
                    tmp_queue.append(i.left)
                if i.right:
                    tmp_queue.append(i.right)
            queue = tmp_queue[:]
            level += 1
        return res