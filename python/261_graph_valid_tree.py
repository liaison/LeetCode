
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited_count = 0

        def has_cycle(prev_node, curr_node, visited):
            nonlocal visited_count
            visited_count += 1

            visited[curr_node] = True
            for next_node in graph[curr_node]:
                if next_node == prev_node:
                    continue
                if visited[next_node]:
                    return True
                if has_cycle(curr_node, next_node, visited):
                    return True
            return False

        graph = defaultdict(list)
        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start].append(end)
            graph[end].append(start)

        visited = [False for _ in range(n)]

        start_node = 0
        return (not has_cycle(-1, 0, visited)) and visited_count == n



