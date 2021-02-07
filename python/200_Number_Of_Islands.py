class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        def markIsland(row, col):
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


class UnionFind:

    def __init__(self, grid):
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.group_count = 0
        self.parent = [0] * (self.ROWS * self.COLS + 1)

        for row, row_values in enumerate(grid):
            for col, value in enumerate(row_values):
                if value == "1":
                    index = self.encode(row, col)
                    self.parent[index] = index
                    self.group_count += 1

    def encode(self, row, col):
        return self.COLS * row + col + 1

    def union(self, a, b):
        a_group = self.find(a)
        b_group = self.find(b)
        if a_group != b_group:
            self.parent[a_group] = b_group
            self.group_count -= 1

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def get_count(self):
        return self.group_count


class SolutionUnionFind:

    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        groups = UnionFind(grid)

        for row, row_values in enumerate(grid):
            for col, value in enumerate(row_values):
                if value == "1":
                    # only need to check the right and down directions
                    dirs = [(0, 1), (1, 0)]
                    for ro, co in dirs:
                        next_row, next_col = row + ro, col + co
                        if 0 <= next_row < ROWS and 0 <= next_col < COLS \
                            and grid[next_row][next_col] == "1":

                            groups.union(groups.encode(next_row, next_col),
                                         groups.encode(row, col))


        return groups.get_count()




