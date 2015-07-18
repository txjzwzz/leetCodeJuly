#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
由于是要求O(1)，所以想法就只有利用原来的结构了，也就是修改原来的链表
把后面的掉方向（是把前面的调方向）
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        p1 = head
        p2 = head
        p3 = ListNode(0)
        while p2 != None and p2.next != None:
            prev = p1
            p1 = p1.next
            p2 = p2.next.next
            prev.next = p3.next
            p3.next = prev
        if p2 != None:
            p1 = p1.next
        p3 = p3.next
        while p1 != None:
            if p1.val != p3.val:
                return False
            p1 = p1.next
            p3 = p3.next
        return True

if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode('a')
    l2 = ListNode('b')
    l1.next = l2
    l3 = ListNode('c')
    l2.next = l3
    l6 = ListNode('c')
    l3.next = l6
    l4 = ListNode('b')
    l6.next = l4
    l5 = ListNode('a')
    l4.next = l5
    print solution.isPalindrome(l1)