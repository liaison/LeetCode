"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prevNum = ['1', 'E']
        return ''.join(self.nextNumber(n, prevNum))

    def nextNumber(self, n, prevNum):
        if n == 1:
            return prevNum[:-1]
        
        nextNum = []
        prevDigit = prevNum[0]
        digitCnt = 1
        for digit in prevNum[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                nextNum.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1
        
        nextNum.append('E')
        
        return self.nextNumber(n-1, nextNum)


class SolutionRec(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prevNum = ['1', 'E']
        return ''.join(self.nextNumber(n, prevNum))


    def count(self, prevDigit, count, num, result):
        if len(num) == 0:
            return result
    
        if prevDigit == num[0]:
            return self.count(prevDigit, count+1, num[1:], result)
        else:
            result.extend([str(count), prevDigit])
            return self.count(num[0], 1, num[1:], result)


    def nextNumber(self, n, prevNum):
        if n == 1:
            return prevNum[:-1]
        
        result = []
        nextNum = self.count(prevNum[0], 1, prevNum[1:], result)
        
        nextNum.append('E')
        
        return self.nextNumber(n-1, nextNum)

        
        
