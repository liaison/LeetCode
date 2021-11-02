
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
            Run a BFS to see if the graph can be colored with two different codes,
                i.e. parent and child nodes should have different colors.
        """
        colors = {}
        nodes_num = len(graph)

        for node in range(nodes_num):
            if node in colors:
                continue

            colors[node] = 1
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                for child in graph[curr]:
                    if child not in colors:
                        colors[child] = - colors[curr]
                        queue.append(child)
                    elif colors[child] == colors[curr]:
                        return False

        return True
