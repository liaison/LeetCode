class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def markIsland(row, col):    
            #queue = deque([(row, col)])
            queue = [(row, col)]
         
            # DFS traversal, not BFS, due to the use of stack
            while queue:
                row, col = queue.pop()
                # mark the visited land
                grid[row][col] = -1
                
                dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for ro, co in dirs:
                    next_row, next_col = row + ro, col + co
                    if 0 <= next_row < ROWS and 0 <= next_col < COLS \
                        and grid[next_row][next_col] == "1":
                        queue.append((next_row, next_col))
        
        island_count = 0
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if value == "1":
                    markIsland(row_index, col_index)
                    island_count += 1
        
        return island_count