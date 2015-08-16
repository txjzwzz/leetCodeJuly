#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, node, path, res):
        if not path:
            path += str(node.val)
        else:
            path += ("->" + str(node.val))
        if node.left:
            self.dfs(node.left, path, res)
        if node.right:
            self.dfs(node.right, path, res)
        if not node.left and not node.right:
            res.append(path)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print solution.binaryTreePaths(root)
    root1 = TreeNode(1)
    print solution.binaryTreePaths(root1)