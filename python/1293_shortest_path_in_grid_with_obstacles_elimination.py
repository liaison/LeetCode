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


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows, cols = len(grid), len(grid[0])
        target = (rows-1, cols-1)

        manhattan_distance = lambda row, col: (rows - row + cols - col - 2)

        if manhattan_distance(0, 0) <= k:
            return rows - 1 + cols - 1

        # (row, col, remaining_elimination)
        state = (0, 0, k)

        # (estimation, steps, state)
        queue = [(manhattan_distance(0, 0), 0, state)]
        seen = set(state)

        while queue:
            estimation, steps, (row, col, remain_eliminations) = heapq.heappop(queue)

            # we can reach the target in the shortest path (manhattan distance),
            #   even if the remaining steps are all obstacles
            if estimation - steps <= remain_eliminations:
                return estimation

            # explore the four directions in the next step
            for new_row, new_col in [(row, col+1), (row+1, col), (row, col-1), (row-1, col)]:
                # out of the boundary of grid
                if 0 > new_row or new_row == rows or 0 > new_col or new_col == cols:
                    continue

                new_eliminations = remain_eliminations - grid[new_row][new_col]
                new_state = (new_row, new_col, new_eliminations)

                # if the next direction is worth exploring
                if new_eliminations >= 0 and new_state not in seen:
                    seen.add(new_state)
                    new_estimation = manhattan_distance(new_row, new_col) + steps + 1
                    queue.append((new_estimation, steps+1, new_state))

        # did not reach the target
        return -1
