
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        start = None

        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '*':
                    start = (row, col)
                    break

        grid[start[0]][start[1]] = "X"
        queue = deque([(start, 0)])

        while queue:
            (row, col), distance = queue.popleft()

            for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_row, next_col = row + r_offset, col + c_offset
                if 0 > next_row or next_row == ROWS or 0 > next_col or next_col == COLS:
                    continue

                if grid[next_row][next_col] == "X":
                    continue
                elif grid[next_row][next_col] == "#": # find the food
                    return distance + 1
                else: # open space
                    # OPTIMIZATION: reduce the number of elements in queue
                    grid[next_row][next_col] = "X" # mark it as visited
                    queue.append(((next_row, next_col), distance+1))

        return -1