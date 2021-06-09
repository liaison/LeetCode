class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start].append(end)
            graph[end].append(start)

        visited = [False for _ in range(n)]

        def explore(node, visited):
            if visited[node]:
                return

            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    explore(neighbor, visited)

        component_cnt = 0

        for node in range(n):
            if not visited[node]:
                explore(node, visited)
                component_cnt += 1

        return component_cnt

