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


class SolutionDFSwithStack:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(row, col):

            is_closed = True
            queue = [(row, col)]

            while queue:
                # queue that behaves as stack
                row, col = queue.pop()

                # mark the visited cell
                grid[row][col] = 1

                if row in [0, len(grid)-1] or col in [0, len(grid[0])-1]:
                    is_closed = False

                for row, col in [(row, col+1), (row+1, col), (row, col-1), (row-1, col)]:
                    if 0 > row or row == len(grid) or col < 0 or col == len(grid[0]):
                        continue

                    if grid[row][col] == 0:
                        queue.append((row, col))

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


class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]

    def find(self, index):
        if self.group[index] != index:
            self.group[index] = self.find(self.group[index])
        return self.group[index]

    def union(self, a, b):
        group_a = self.find(a)
        group_b = self.find(b)
        if group_a != group_b:
            # attach the group of the group_b to the group of group_a
            self.group[group_b] = group_a



class SolutionUnionFind:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        index = lambda row, col: (row * COLS + col)

        uf = UnionFind(ROWS * COLS)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    # only needs to check the neighbors on the right and down sides
                    for next_row, next_col in [(row, col+1), (row+1, col)]:
                        if next_row == ROWS or next_col == COLS:
                            continue
                        if grid[next_row][next_col] == 0:
                            uf.union(index(row, col), index(next_row, next_col))


        # indicate if the island group is closed or not
        island_mark = dict()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    group_id = uf.find(index(row, col))

                    if group_id not in island_mark:
                        island_mark[group_id] = True

                    if row in [0, ROWS-1] or col in [0, COLS-1]:
                        # one island on the border
                        island_mark[group_id] = False

        return len([is_closed for is_closed in island_mark.values() if is_closed])






