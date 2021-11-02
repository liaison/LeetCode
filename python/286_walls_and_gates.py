
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])

        gates = []
        gate_distance = {}

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    gates.append((row, col))
                elif rooms[row][col] == INF:
                    gate_distance[(row, col)] = INF

        def bfs(start):
            """
                update the min distance from each gate to each room
            """
            nonlocal gate_distance
            # start from a gate, do BFS to each room
            row, col = start
            queue = deque([(row, col, 0)])
            visited = set()
            while queue:
                row, col, steps = queue.popleft()

                for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row, new_col = row + row_offset, col + col_offset
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                        continue
                    if rooms[new_row][new_col] == INF and (new_row, new_col) not in visited:
                        coordinate = (new_row, new_col)
                        gate_distance[coordinate] = min(gate_distance[coordinate], steps + 1)
                        visited.add(coordinate)
                        queue.append((new_row, new_col, steps + 1))

        for gate in gates:
            bfs(gate)

        # return the min distance
        for (row, col), distance in gate_distance.items():
            rooms[row][col] = distance



class SolutionSingleBFS:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])

        gates = []
        gate_distance = {}

        queue = deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    # gate
                    queue.append((row, col, 0))
                    visited.add((row, col))
                elif rooms[row][col] == INF:
                    # room
                    gate_distance[(row, col)] = INF

        while queue:
            row, col, steps = queue.popleft()

            for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + r_offset, col + c_offset
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                if rooms[new_row][new_col] == INF and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
                    gate_distance[(new_row, new_col)] = steps + 1

        for (row, col), distance in gate_distance.items():
            rooms[row][col] = distance



