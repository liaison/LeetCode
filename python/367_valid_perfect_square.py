'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
    Input: 16
    Output: true

Example 2:

    Input: 14
    Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
            Binary search on the proper number
        '''
        low, high = 0, num
        
        # tricky to set the conditions:
        while low <= high:           # condition 1). low <= high
            pivot = (low + high) // 2
            product = pivot * pivot
            if product == num:
                return True
            elif product < num:
                low = pivot + 1      # condition 2). move the pivot
            else:
                high = pivot - 1     # condition 3). move the pivot
        
        return False
