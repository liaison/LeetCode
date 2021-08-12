class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(row, col):
            # mark the visited cell
            grid[row][col] = 1
            is_closed = True

            if row in [0, len(grid)-1] or col in [0, len(grid[0])-1]:
                is_closed = False

            for row, col in [(row, col+1), (row+1, col), (row, col-1), (row-1, col)]:
                if 0 > row or row == len(grid) or col < 0 or col == len(grid[0]):
                    continue
                if grid[row][col] == 0:
                    # Should not merge the following two lines together
                    # otherwise, some dfs() invocation might be optimized away
                    next_is_closed = dfs(row, col)
                    is_closed = is_closed and next_is_closed

            return is_closed

        closed_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    # kick off the DFS visit
                    is_closed = dfs(row, col)
                    if is_closed:
                        closed_islands += 1


        return closed_islands