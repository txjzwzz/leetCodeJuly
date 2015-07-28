#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
"""
class Solution:
    # @param {character[][]} grid
    # @return {integer}
    # 思想：从左上角开始沿着右下方进行统计
    # 一行行统计，只有自己的左边和上方都没有的1才算上一个
    # 但是有可能这个被之后的1和上面连起来了！也可能被下面的1和后面连起来了！
    # 所以这种做法不严谨！还是得用bfs
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        count = 0
        for i in range(len(grid[0])):
            if grid[0][i] == '1':
                if i == 0 or (i > 0 and grid[0][i-1] == '0'):
                    count += 1
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    if j == 0:
                        if grid[i-1][j] == '0':
                            count += 1
                    else:
                        if grid[i-1][j] == '0' and grid[i][j-1] == '0':
                            count += 1
                        if grid[i-1][j] == '1':
                            flag = False
                            index = j - 1
                            while index >= 0 and  grid[i][index] == '1':
                                if grid[i-1][index] == '0':
                                    flag = True
                                else:
                                    flag = False
                                    break
                                index -= 1
                            if flag:
                                count -= 1
        return count
        """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        markGrid = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if markGrid[i][j] == 1 or grid[i][j] == '0':
                    continue
                elif grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, grid, markGrid)
        return count

    def bfs(self, i, j, grid, markGrid):
        markGrid[i][j] = 1
        queue = []
        queue.append((i, j))
        while queue:
            tmpQueue = []
            while queue:
                (eleX, eleY) = queue.pop()
                if eleX > 0 and grid[eleX-1][eleY] == '1' and markGrid[eleX-1][eleY] == 0:
                    tmpQueue.append((eleX-1, eleY))
                    markGrid[eleX-1][eleY] = 1
                if eleY > 0 and grid[eleX][eleY-1] == '1' and markGrid[eleX][eleY-1] == 0:
                    tmpQueue.append((eleX, eleY-1))
                    markGrid[eleX][eleY-1] = 1
                if eleX < len(grid)-1 and grid[eleX+1][eleY] == '1' and markGrid[eleX+1][eleY] == 0:
                    tmpQueue.append((eleX+1, eleY))
                    markGrid[eleX+1][eleY] = 1
                if eleY < len(grid[0])-1 and grid[eleX][eleY+1] == '1' and markGrid[eleX][eleY+1] == 0:
                    tmpQueue.append((eleX, eleY+1))
                    markGrid[eleX][eleY+1] = 1
            queue = tmpQueue[:]


if __name__ == '__main__':
    a = ['11110', '11010', '11000', '00000']
    b = ['11000', '11000', '00100', '00011']
    c = ['11111', '10001', '10001', '00000']
    d = ['11111', '10001', '10001', '11111']
    e = ['010', '101', '010']
    f = ["111", "010", "111"]
    g = ["10111", "10101", "11101"]
    solution = Solution()
    print solution.numIslands(a)
    print solution.numIslands(b)
    print solution.numIslands(c)
    print solution.numIslands(d)
    print solution.numIslands(e)
    print solution.numIslands(f)
    print solution.numIslands(g)
