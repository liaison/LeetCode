
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



class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]

    def find(self, node):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def union(self, n1, n2):
        """
            return false: if n1 and n2 already belong to the same group
        """
        g1 = self.find(n1)
        g2 = self.find(n2)
        if g1 != g2:
            self.group[g1] = self.group[g2]
            return True
        else:
            return False


class SolutionUnionFind:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        uf = UnionFind(n)

        for edge in edges:
            start, end = edge[0], edge[1]
            if not uf.union(start, end):
                return False

        return True





