class DisjointSet:

    def __init__(self, N):
        # the id starts from 1, instead of 0
        self.parent = [i for i in range(N+1)]

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            # attach the group of pb to pa
            self.parent[pb] = pa
        return pa


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        # at least we need N-1 edges to connect N vetex
        if len(connections) < N-1:
            return -1

        connections.sort(key = lambda x: x[2])
        ds = DisjointSet(N)

        components = N
        total_cost = 0
        for (city1, city2, cost) in connections:
            if components == 1:
                break

            group1, group2 = ds.find(city1), ds.find(city2)
            if group1 != group2:
                ds.union(group1, group2)
                components -= 1
                total_cost += cost

        return -1 if components != 1 else total_cost

