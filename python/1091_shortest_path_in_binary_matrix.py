class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        N = len(grid)

        def bfs():

            queue = [(0, 0)]
            distance = 0
            is_found = False

            while queue:
                next_queue = []
                distance += 1

                while queue:
                    row, col = queue.pop()

                    for ro, co in [(1, 1), (1, 0), (0, 1), (-1, 0),
                                   (0, -1), (1, -1), (-1, -1), (-1, 1)]:
                        new_row, new_col = row + ro, col + co
                        if new_row < 0 or new_row >= N or \
                            new_col < 0 or new_col >= N:
                            continue

                        if row == N-1 and col == N-1:
                            return distance

                        if grid[new_row][new_col] == 0:
                            grid[new_row][new_col] = 1
                            next_queue.append((new_row, new_col))
                queue = next_queue

            return -1

        if grid[0][0] != 0:
            return -1

        if N == 1:
            return 1

        grid[0][0] = 1
        distance = bfs()
        return distance
