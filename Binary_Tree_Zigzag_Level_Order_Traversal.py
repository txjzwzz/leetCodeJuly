#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level, queue = [], 0, [root]
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
            if level % 2 == 1:
                res[level].reverse()
            level += 1
            queue = tmp_queue[:]
        return res