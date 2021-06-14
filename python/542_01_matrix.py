
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        ROWS = len(mat)
        COLS = len(mat[0])

        def bfs(pos):
            visited = set([pos])
            queue = deque([(pos, 0)])

            while queue:
                (row, col), distance = queue.popleft()

                for ro, co in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row, new_col = row + ro, col + co
                    if 0 > new_row or new_row == ROWS or 0 > new_col or new_col == COLS:
                        continue

                    if (new_row, new_col) in visited:
                        continue

                    if mat[new_row][new_col] == 0:
                        return distance + 1
                    else: # == 1
                        visited.add((new_row, new_col))
                        queue.append(((new_row, new_col), distance+1))

            # should never have arrived here.
            return distance

        res = [[0]*COLS for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 1:
                    res[row][col] = bfs((row, col))

        return res


