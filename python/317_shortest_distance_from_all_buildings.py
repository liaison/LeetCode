
class SolutionTLE:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        buildings = []
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    buildings.append((row, col))

        def bfs(start):
            row, col = start
            visited = set()
            queue = deque([(row, col, 0)])
            distance = {}
            while queue:
                curr_row, curr_col, steps = queue.popleft()

                for offset_row, offset_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    next_row, next_col = curr_row + offset_row, curr_col + offset_col
                    if next_row < 0 or next_row >= rows \
                        or next_col < 0 or next_col >= cols:
                        continue

                    if grid[next_row][next_col] == 0:
                        if (next_row, next_col) not in visited:
                            visited.add((next_row, next_col))
                            distance[(next_row, next_col)] = steps + 1
                            queue.append((next_row, next_col, steps + 1))
            return distance

        total_distance = {}
        for start in buildings:
            distances = bfs(start)

            for land, min_distance in distances.items():
                if land not in total_distance:
                    total_distance[land] = (0, 0)
                curr_count, curr_distance = total_distance[land]
                total_distance[land] = (curr_count + 1, curr_distance + min_distance)

        total_buildings = len(buildings)
        min_distance_sum = float('inf')
        for count, min_distance in total_distance.values():
            if count == total_buildings:
                min_distance_sum = min(min_distance_sum, min_distance)

        return min_distance_sum if min_distance_sum != float('inf') else -1



