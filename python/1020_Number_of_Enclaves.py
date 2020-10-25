class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        
        rows, cols = len(A), len(A[0])
        
        borders = []
        total_land = 0
        
        def isBoundary(row, col):
            return (row == 0) or (row==rows-1) or (col==0) or (col==cols-1)
        
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == 1:
                    total_land += 1
                    if isBoundary(row, col):
                        borders.append((row, col))
                        A[row][col] = -1
        
        queue = deque(borders)
        total_land -= len(borders)

        # BFS traversal, starting from the borders
        #   reaching the inner land.
        while queue:
            row, col = queue.popleft()
            for ro, co in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + ro, col + co
                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    if A[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        A[new_row][new_col] = -1
                        total_land -= 1
        
        return total_land

    
