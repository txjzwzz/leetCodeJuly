#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
堆
"""

class Heap:

    def __init__(self):
        self.heap_size = 0

    # (i+1)*2=j+1
    def left(self, i):
        return 2 * (i+1) - 1
    # (i+1)*2+1=j+1
    def right(self, i):
        return 2 * (i+1)

    def parent(self, i):
        return ((i+1)>>1)-1

    def max_heapfy(self, A, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i
        largest = r if r <= self.heap_size and A[r] > A[largest] else largest
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapfy(A, largest)

    def build_max_heap(self, A):
        self.heap_size = len(A)-1
        for i in range((len(A)-1) >> 1, -1, -1):
            self.max_heapfy(A, i)

    def heap_sort(self, A):
        self.build_max_heap(A)
        for i in range(len(A)-1, 0, -1):
            A[0], A[i] = A[i], A[0]
            self.heap_size -= 1
            self.max_heapfy(A, 0)

if __name__ == '__main__':
    solution = Heap()
    import random
    A = [random.randint(0, 100) for i in range(10)]
    solution.heap_sort(A)
    print A