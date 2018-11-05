"""
Given two words word1 and word2, find the minimum number of operations 
    required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

@author: Lisong Guo <lisong.guo@me.com>
@date:   Nov 05, 2018

"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        rows = len(word1) + 1
        cols = len(word2) + 1

        dp = [[0 for j in range(cols)] for i in range(rows)]

        for irow in range(rows):
            dp[irow][0] = irow
        for icol in range(cols):
            dp[0][icol] = icol

        for irow in range(0, rows-1):
            for icol in range(0, cols-1):
                if word1[irow] == word2[icol]:
                    dp[irow+1][icol+1] = dp[irow][icol]
                else:
                    d_insert = dp[irow+1][icol]
                    d_delete = dp[irow][icol+1]
                    d_replace = dp[irow][icol]

                    dp[irow+1][icol+1] = \
                        min(d_insert, d_delete, d_replace) + 1
        print(dp)
        
        return dp[rows-1][cols-1]


def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    actual_output = test_func(*test_input)
    print(case_name, test_input, ' target:', test_target,
          ' output:', actual_output)
    assert(test_target == actual_output)


if __name__ == "__main__":

    solution = Solution()

    word1 = "horse"
    word2 = "ros"
    test_case_1_input = (word1, word2)
    test_case_1_target = 3  # horse -> rorse -> rose -> ros
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.minDistance)


    word1 = "intention"
    word2 = "execution"
    test_case_2_input = (word1, word2)
    test_case_2_target = 5  # [inten]tion -> [execu]tion
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.minDistance)






