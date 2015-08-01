#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you
should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
"""
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        if numCourses <= 0:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]
        needDict = {}
        for i in prerequisites:
            if len(i) == 2:
                if i[0] in needDict:
                    needDict[i[0]].append(i[1])
                else:
                    needDict[i[0]] = [i[1]]
        res = []
        # to find if element is in res
        resDict = {}
        while True:
            edit = False
            for key in needDict.keys():
                for val in needDict[key]:
                    if val not in needDict:
                        needDict[key].remove(val)
                        edit = True
                        if val not in resDict:
                            resDict[val] = 1
                            res.append(val)
                if len(needDict[key]) == 0:
                    needDict.pop(key)
            if not needDict:
                for i in range(numCourses):
                    if i not in resDict:
                        res.append(i)
                return res
            if not edit:
                return []

if __name__ == '__main__':
    solution = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print solution.findOrder(numCourses, prerequisites)
    prerequisites = [[1, 0], [0, 1]]
    print solution.findOrder(numCourses, prerequisites)
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print solution.findOrder(numCourses, prerequisites)