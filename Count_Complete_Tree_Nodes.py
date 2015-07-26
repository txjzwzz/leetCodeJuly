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
    # 现在换个思路，因为这里有一个性质没有使用到，就是底层的结点，一旦一个结点底层是满的，那么，
    # 其左边的一定是满的，所以可以用类似二分查找的方式！目的是找到左右分叉的点！
    # 当然，左右分叉的点可能不存在！
    # 过程就是对比左子结点和右子结点的最右的底层结点的高度
    def countNodes(self, root):
        path = []
        self.markPath(root, path)
        depth = 0
        count = 0
        while path:
            count = count + path.pop() * pow(2, depth)
            depth += 1
        res = pow(2, depth) - 1 + count
        return res

    def markPath(self, root, path):
        if not root:
            return
        if self.count_right_height(root.left) > self.count_right_height(root.right):
            path.append(1)
            self.markPath(root.right, path)
        else:
            path.append(0)
            self.markPath(root.left, path)

    def count_right_height(self, root):
        if not root:
            return 0
        count = 1
        while root.right:
            count += 1
            root = root.right
        return count


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