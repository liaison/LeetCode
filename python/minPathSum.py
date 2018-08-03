"""

Given a m x n grid filled with non-negative numbers, find a path from top left 
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

    Input:
    [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
 
@author: Lisong Guo <lisong.guo@me.com
@date:   Aug 03, 2018

"""

class Solution:
    def _minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import sys

        n_row = len(grid)
        if (n_row == 0):
            return 0

        n_col = len(grid[0])
        size = n_row * n_col
        dp = [sys.maxsize] * (n_row + 1) * (n_col + 1)
        dp[size-1] = grid[n_row-1][n_col-1]
        
        i = size-2
        while(i >= 0):
            i_row = i // n_col
            i_col = i % n_col
            min_path = min(dp[i + n_col], dp[i + 1])
            dp[i] = grid[i_row][i_col] + min_path
            i -= 1

        return dp[0]


    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_row = len(grid)
        n_col = len(grid[0])
        # extend the dp matrix with pseudo boundary to eliminate the switch cases
        dp = [[sys.maxsize for _ in range(n_col + 1)] for _ in range(n_row + 1)]
        dp[n_row-1][n_col] = 0

        for i_row in range(n_row-1, -1, -1):
            for i_col in range(n_col-1, -1, -1):
                min_path = min(dp[i_row+1][i_col], dp[i_row][i_col+1])
                dp[i_row][i_col] = grid[i_row][i_col] + min_path
        
        return dp[0][0]


def print_matrix(m):
    for i in range(len(m)):
        print(m[i])


def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    actual_output = test_func(*test_input)
    print(case_name, test_input, ' target:', test_target,
          ' output:', actual_output)
    assert(test_target == actual_output)


import sys

if __name__ == "__main__":

    solution = Solution()

    test_case_1_input = ([
        [1,3,1],
        [1,5,1],
        [4,2,1]], )
    test_case_1_target = 7
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.minPathSum)

    test_case_2_input = ([
        [1,3,1]], )
    test_case_2_target = 5
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.minPathSum)

    test_case_3_input = ([[1]], )
    test_case_3_target = 1
    verify('test case 3:',
           test_case_3_input, test_case_3_target, solution.minPathSum)
