#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal
to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        tmp_head = ListNode(-1)
        tmp_head.next = head
        node_index = tmp_head
        prev = tmp_head
        while prev.next:
            if prev.next.val < x:
                if prev == node_index:
                    prev = prev.next
                    node_index = node_index.next
                else:
                    tmp = prev.next
                    prev.next = prev.next.next
                    tmp.next = node_index.next
                    node_index.next = tmp
                    node_index = node_index.next
            else:
                prev = prev.next
        return tmp_head.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    res = solution.partition(head, 3)
    while res:
        print res.val,
        res = res.next
    print