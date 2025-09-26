from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        max_row, max_col = len(grid), len(grid[0])

        max_amount = 0
        def dfs(curr, visited, amount):
            nonlocal max_amount

            max_amount = max(max_amount, amount)

            row, col = curr
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for (row_offset, col_offset) in offsets:
                next_row = row + row_offset
                next_col = col + col_offset

                if next_row < 0 or next_row >= max_row or next_col < 0 or next_col >= max_col:
                    continue
                elif (next_row, next_col) in visited:
                    continue
                elif grid[next_row][next_col] > 0:
                    next_pos = (next_row, next_col)
                    visited.add(next_pos)
                    next_amount = amount + grid[next_row][next_col]
                    dfs(next_pos, visited, next_amount)
                    visited.remove(next_pos)

        for row in range(max_row):
            for col in range(max_col):
                amount = grid[row][col]
                if amount > 0:
                    curr = (row, col)
                    visited = set([curr])
                    dfs(curr, visited, amount)

        return max_amount



grid = [[0,6,0],[5,8,7],[0,9,0]]

expected = 24

solution = Solution()
assert solution.getMaximumGold(grid) == 24






