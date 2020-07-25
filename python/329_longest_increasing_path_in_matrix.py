class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if len(matrix) == 0:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        @lru_cache(maxsize=None)
        def dfs(row, col):
            ans = 0
            for ro, co in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + ro, col + co
                if 0 <= new_row and new_row < rows and \
                   0 <= new_col and new_col < cols and \
                   matrix[new_row][new_col] > matrix[row][col]:
                    ans = max(ans, dfs(new_row, new_col))
            return ans + 1
        
        max_paths = 0
        for row in range(rows):
            for col in range(cols):
                max_paths = max(max_paths, dfs(row, col))
        
        return max_paths