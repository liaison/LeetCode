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