#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        if root is None:
            return 0
        indexList = [0]
        return self.dfs(root, indexList, k)

    # 使用indexList和方便修改当前是第几个点了
    def dfs(self, root, indexList, k):
        if root.left is not None:
            res = self.dfs(root.left, indexList, k)
            if res is not None:
                return res
        indexList[0] = indexList[0] + 1
        if indexList[0] == k:
            return root.val
        if root.right is not None:
            res = self.dfs(root.right, indexList, k)
            if res is not None:
                return res
        return None

if __name__ == '__main__':
    t1 = TreeNode(5)
    t2 = TreeNode(3)
    t3 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t4 = TreeNode(2)
    t5 = TreeNode(4)
    t2.left = t4
    t2.right = t5
    t6 = TreeNode(1)
    t4.left = t6
    t7 = TreeNode(6)
    t3.left = t7
    t8 = TreeNode(8)
    t3.right = t8
    t9 = TreeNode(9)
    t8.right = t9

    solution = Solution()
    print solution.kthSmallest(t1, 1)
    print solution.kthSmallest(t1, 2)
    print solution.kthSmallest(t1, 3)
    print solution.kthSmallest(t1, 4)
    print solution.kthSmallest(t1, 5)
    print solution.kthSmallest(t1, 6)
    print solution.kthSmallest(t1, 7)
    print solution.kthSmallest(t1, 8)
    print solution.kthSmallest(t1, 9)