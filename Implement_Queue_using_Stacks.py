#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        if self.queue is []:
            return
        tmpQueue = []
        while self.queue:
            tmpQueue.append(self.queue.pop())
        tmpQueue.pop()
        while tmpQueue:
            self.queue.append(tmpQueue.pop())

    # @return an integer
    def peek(self):
        if self.queue is []:
            return None
        tmpQueue = []
        while self.queue:
            tmpQueue.append(self.queue.pop())
        res = tmpQueue[len(tmpQueue)-1]
        while tmpQueue:
            self.queue.append(tmpQueue.pop())
        return res

    # @return an boolean
    def empty(self):
        return True if not self.queue else False

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    print q.peek()
    q.push(2)
    print q.peek()
    q.push(3)
    print q.peek()
    q.pop()
    print q.peek()
    q.pop()
    print q.peek()
