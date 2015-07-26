#-*- coding=utf-8 -*-
"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the
last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    # 由于还是需要遍历一下底层的点，所以广度优先可行，就是可能需要大量的存储空间
    # 超时
    """
    def countNodes(self, root):
        if not root:
            return 0
        queue = [root]
        depth = 0
        while True:
            tmpQueue = []
            startIndex = 0
            while startIndex < len(queue):
                tmpNode = queue[startIndex]
                startIndex += 1
                if tmpNode.left:
                    tmpQueue.append(tmpNode.left)
                else:
                    return pow(2, depth+1) - 1 + len(tmpQueue)
                if tmpNode.right:
                    tmpQueue.append(tmpNode.right)
                else:
                    return pow(2, depth+1) - 1 + len(tmpQueue)
            queue = tmpQueue[:]
            depth += 1
    """
    def countNodes(self, root):
        return


if __name__ == '__main__':
    solution = Solution()
    root = None
    print solution.countNodes(root)
    root = TreeNode(10)
    print solution.countNodes(root)
    l1 = TreeNode(11)
    root.left = l1
    print solution.countNodes(root)
    r1 = TreeNode(12)
    root.right = r1
    print solution.countNodes(root)
    ll1 = TreeNode(13)
    l1.left = ll1
    print solution.countNodes(root)
    lr1 = TreeNode(14)
    l1.right = lr1
    print solution.countNodes(root)
    rl1 = TreeNode(15)
    r1.left = rl1
    print solution.countNodes(root)
    rr1 = TreeNode(16)
    r1.right = rr1
    print solution.countNodes(root)
    lll1 = TreeNode(17)
    ll1.left = lll1
    print solution.countNodes(root)