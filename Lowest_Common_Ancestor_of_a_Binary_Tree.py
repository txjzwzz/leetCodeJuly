#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two
nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
           ___6______
        /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p is None or q is None:
            return None
        path_p = [root]
        path_q = [root]
        self.dfs_child(root, p, path_p)
        self.dfs_child(root, q, path_q)
        index = 0
        while True:
            if index+1 < len(path_p) and index+1 < len(path_q) and path_p[index+1] == path_q[index+1]:
                index = index + 1
            else:
                break
        return path_p[index]


    # find path
    def dfs_child(self, root, p, path):
        if root == None:
            return False
        if root == p:
            return True
        path.append(root.left)
        if self.dfs_child(root.left, p, path) is True:
            return True
        else:
            path.pop()
            path.append(root.right)
            if self.dfs_child(root.right, p, path) is True:
                return True
            else:
                path.pop()
                return False


if __name__ == '__main__':
    s1 = TreeNode(6)
    s2 = TreeNode(2)
    s3 = TreeNode(8)
    s1.left = s2
    s1.right = s3
    s4 = TreeNode(0)
    s5 = TreeNode(4)
    s2.left = s4
    s2.right = s5
    s6 = TreeNode(7)
    s7 = TreeNode(9)
    s3.left = s6
    s3.right = s7
    s8 = TreeNode(3)
    s9 = TreeNode(5)
    s5.left = s8
    s5.right = s9
    solution = Solution()
    res = solution.lowestCommonAncestor(s1, s2, s3)
    print res.val
    res = solution.lowestCommonAncestor(s1, s2, s5)
    print res.val
    res = solution.lowestCommonAncestor(s1, s8, s7)
    print res.val
