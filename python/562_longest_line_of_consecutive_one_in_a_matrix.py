class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if len(M) == 0:
            return 0

        rows, cols = len(M), len(M[0])
        max_len = 0

        @lru_cache(maxsize=None)
        def dfs(row, col, direction):
            subpath = 0
            # directions: left, up, upleft, upright
            ro, co = direction
            new_row, new_col = row + ro, col + co
            if 0 <= new_row and new_row < rows and \
               0 <= new_col and new_col < cols and \
                M[new_row][new_col] == 1:
                subpath = dfs(new_row, new_col, direction)
            
            return (M[row][col] == 1) + subpath


        for row in range(rows):
            for col in range(cols):
                for direction in [(0, 1), (-1, 0), (-1, -1), (-1, 1)]:
                    max_len = max(max_len, dfs(row, col, direction))
        
        return max_len


class SolutionManualMemoization:
    def longestLine(self, M: List[List[int]]) -> int:
        
        if len(M) == 0:
            return 0
        
        rows, cols = len(M), len(M[0])
        max_len = 0
        
        path_counter = defaultdict(int)
        
        for row in range(rows):
            for col in range(cols):
                for direction in [row, col+.1, row-col+.2, row+col+.3]:
                    new_count = (path_counter[direction] + 1) * M[row][col]
                    path_counter[direction] = new_count
                    max_len = max(max_len, new_count)
        
        return max_len