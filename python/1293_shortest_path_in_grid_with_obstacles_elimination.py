class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows, cols = len(grid), len(grid[0])
        target = (rows-1, cols-1)

        state = (0, 0, k)
        queue = deque([(0, state)])
        seen = set(state)

        while queue:

            level_length = len(queue)

            for _ in range(level_length):
                steps, (row, col, k) = queue.popleft()


                if (row, col) == target:
                    return steps

                for row, col in [(row, col+1), (row+1, col), (row, col-1), (row-1, col)]:
                    if 0 > row or row == rows or 0 > col or col == cols:
                        continue

                    new_state = (row, col, k - grid[row][col])

                    if k >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps+1, new_state))

            steps += 1

        # did not reach the target
        return -1