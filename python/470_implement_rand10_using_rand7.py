# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        
            Two-phase generation, decision-tree alike approach
                          
                 [1, 2, 3]            [5, 6, 7]
                     |                    |
                     |                    |
              [1, 2, 3, 4, 5]      [6, 7, 8, 9, 10]
              
        """
        while True:
            first_round = rand7()
            if first_round != 4:
                while True:
                    second_round = rand7()
                    if second_round <= 5:
                        return second_round + (first_round < 4) * 5