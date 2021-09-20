
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        visited = set()
        n_rows, n_cols = len(grid), len(grid[0])

        def dfs(curr, prev, mark):
            nonlocal visited

            visited.add(curr)
            row, col = curr

            for next_row, next_col in [(row, col+1), (row+1, col),
                                       (row, col-1), (row-1, col)]:
                # the immediate prev position is not available
                if (next_row, next_col) == prev:
                    continue
                # boundary check
                if next_row < 0 or next_row >= n_rows or\
                   next_col < 0 or next_col >= n_cols:
                    continue
                # non homogene neighbor is not eligible
                if grid[next_row][next_col] != mark:
                    continue
                # detect the cycle !
                if (next_row, next_col) in visited:
                    return True
                else:
                    if dfs((next_row, next_col), curr, mark):
                        return True

            return False

        pseudo_prev = (-1, -1)
        for row in range(n_rows):
            for col in range(n_cols):
                if (row, col) not in visited:
                    if dfs((row, col), pseudo_prev, grid[row][col]):
                        return True
        return False

