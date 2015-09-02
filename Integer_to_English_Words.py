#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
class Solution(object):


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        top_19 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        def word(num):
            if num < 20: #maybe zero
                return top_19[num-1:num]
            if num < 100:
                return [tens[num/10-1]] + word(num%10)
            if num < 1000:
                return [top_19[num/100-1]] + ['Hundred'] + word(num%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                print p, w
                if num < 1000 ** (p+1):
                    return word(num/(1000**p)) + [w] + word(num%(1000**p))
        return ' '.join(word(num)) or 'Zero'

if __name__ == '__main__':
    solution = Solution()
    print solution.numberToWords(100)
