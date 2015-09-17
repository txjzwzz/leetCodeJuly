#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        tmp_head = ListNode(-1)
        tmp_head.next = head
        one_step = head
        two_step = head
        while two_step.next and two_step.next.next:
            tmp_head = tmp_head.next
            one_step = one_step.next
            two_step = two_step.next.next
        root = TreeNode(one_step.val)
        tmp_head.next = None
        if one_step != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(one_step.next)
        return root

    def sortedListToBST1(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.build_tree(nums, 0, len(nums)-1)

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