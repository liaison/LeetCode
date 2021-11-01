class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque([])
        visited = [[False] * cols for _ in range(rows)]

        # treat all lands as a Unit
        # run BFS from all lands, the water that is reached at the end is the farest one
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col, 0))
                    visited[row][col] = True

        if len(queue) == rows * cols:
            # all lands, no water
            return -1

        steps = - 1
        while queue:
            row, col, steps = queue.popleft()

            for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + r_offset, col + c_offset
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue

                if not visited[new_row][new_col] and grid[new_row][new_col] == 0:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, steps + 1))

        return steps
