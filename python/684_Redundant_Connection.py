class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def isReachable(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                else:
                    for neighbor in graph[source]:
                        if isReachable(neighbor, target):
                            return True
                return False

        graph = defaultdict(set)
        for u, v in edges:
            if u in graph and v in graph:
                # conduct a DFS search to see 
                #   if we could reach from u to v
                seen = set()
                if isReachable(u, v):
                    return (u, v)
            
            graph[u].add(v)
            graph[v].add(u)


class DisjointSetUnion(object):
    
    def __init__(self):
        # initially, each node is an independent component
        self.parent = [i for i in range(1001)]
        self.rank = [0] * 1001
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        # the two nodes share the same set
        if px == py:
            return False
        
        # otherwise, connect the two sets (components)
        if self.rank[px] < self.rank[py]:
            # add the node to the union with less rank (less members)
            self.parent[py] = px
        elif self.rank[px] > self.rank[py]:
            self.parent[px] = py
        else:
            # equal number of member
            self.parent[py] = px
            self.rank[px] += 1
        return True


class SolutionDSU:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DisjointSetUnion()
        
        for u, v in edges:
            if not dsu.union(u, v):
                return (u, v)
        