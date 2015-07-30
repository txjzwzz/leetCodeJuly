#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        res = []
        candidates = list(set(candidates))
        candidates.sort()
        for i in range(len(candidates)-1, -1, -1):
            tmpRes = self.calculate(candidates, target, i)
            if tmpRes:
                for tmp in tmpRes:
                    res.append(tmp)
        return res

    def calculate(self, candidates, target, index):
        if candidates[index] > target:
            return []
        res = []
        count = 1
        while count * candidates[index] <= target:
            tmpRes = []
            for i in range(count):
                tmpRes.append(candidates[index])
            if count * candidates[index] == target:
                res.append(tmpRes)
                return res
            for i in range(index-1, -1, -1):
                subRes = self.calculate(candidates, target-count*candidates[index], i)
                if subRes:
                    for tmp in subRes:
                        tmp += tmpRes
                        res.append(tmp)
            count += 1
        return res

if __name__ == '__main__':
    candidate = [2, 3, 6, 7]
    target1 = 7
    target2 = 8
    target3 = 9
    solution = Solution()
    print solution.combinationSum(candidate, target1)
    print solution.combinationSum(candidate, target2)
    print solution.combinationSum(candidate, target3)



