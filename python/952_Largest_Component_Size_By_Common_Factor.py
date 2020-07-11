class SolutionTLE:
    """ Solution leads to TLE (Time Limit Exceeded). """

    def largestComponentSize(self, A: List[int]) -> int:
        
        total_length = len(A)
        dsu = DisjointSetUnion(20000)
        # set the default value to 1, rather than 0.
        group_count = defaultdict(lambda:1)
        max_size = 0
        
        for start_index, start in enumerate(A):
            
            for end_index in range(start_index+1, total_length):
                
                if gcd(A[start_index], A[end_index]) == 1:
                    continue
        
                start_group = dsu.find(start_index)
                end_group = dsu.find(end_index)
                if start_group == end_group:
                    continue
                else:
                    merged_group = dsu.union(start_index, end_index)         
                    
                    group_count[merged_group] += group_count[end_group] if merged_group == start_group else group_count[start_group]
                    
                    max_size = max(max_size, group_count[merged_group])
                    
                    if max_size == total_length:
                        return total_length

        #print(group_count)
        
        return max_size
                
                
                
class DisjointSetUnion(object):
    
    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size+1)]
        self.rank = [0] * (size+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        # the two nodes share the same set
        if px == py:
            return px
        
        # otherwise, connect the two sets (components)
        if self.rank[px] < self.rank[py]:
            # add the node to the union with less rank (less members)
            self.parent[py] = px
            return px
        elif self.rank[px] > self.rank[py]:
            self.parent[px] = py
            return py
        else:
            # equal number of member
            self.parent[py] = px
            self.rank[px] += 1
            return px
                
                
                
                
                
                
                
                
                
                
                

