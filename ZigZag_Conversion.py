#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if not s or numRows == 1:
            return s
        resList = ["" for i in range(numRows)]
        count = 0
        direction = 0
        for i in s:
            resList[count] += i
            if direction == 0:
                if count == numRows-1:
                    direction = 1
                    count -= 1
                else:
                    count += 1
            else:
                if count == 0:
                    count += 1
                    direction = 0
                else:
                    count -= 1
        return "".join(resList[i] for i in range(numRows))

if __name__ == '__main__':
    solution = Solution()
    s = "PAYPALISHIRING"
    print solution.convert(s, 1)