class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        # each value represents the maximal width of square 
        #   formed with the point as the bottom-rigth of the square.
        dp = [[0] * (cols+1) for i in range(rows+1)]

        max_width = 0
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if matrix[row-1][col-1] == '1':
                    dp[row][col] = \
                        1 + min([dp[row-1][col], dp[row][col-1], dp[row-1][col-1]])
                    max_width = max(max_width, dp[row][col])
        
        return max_width * max_width

    
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """ space-optimized DP solution,
            with sliding window.
        """
        # sliding window
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        dp = [0] * (cols+1)
        
        max_width = 0
        prev = 0
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                temp = dp[col]
                if matrix[row-1][col-1] == '1':
                    dp[col] = 1 + min([dp[col], dp[col-1], prev])
                    max_width = max(max_width, dp[col])
                else:
                    # reset the value for the next sliding window
                    dp[col] = 0
                # prepare for the next sliding window
                prev = temp
                
        
        return max_width * max_width
