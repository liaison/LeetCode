class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
            Calculate the distance between any two vertex, 
            which can be considered as a brute-force solution.
            This solution did timeout.
        """
        
        distance_matrix = [[0] * n for i in range(n)]
        
        for (start, end) in edges:
            distance_matrix[start][end] = 1
            distance_matrix[end][start] = 1
        
        
        def distance_to_others(start):
            nonlocal distance_matrix
            
            visited = [False for i in range(n)]
            visited[start] = True
            
            steps = 1
            queue = deque([start])
            while queue:
                next_queue = deque([])
                while queue:
                    curr = queue.popleft()
                    for node_id, distance in enumerate(distance_matrix[curr]):
                        if distance == 1 and not visited[node_id]:
                            visited[node_id] = True
                            next_queue.append(node_id)
                            distance_matrix[start][node_id] = steps
                            distance_matrix[node_id][start] = steps 
                steps += 1
                queue = next_queue
        
        for root in range(n):
            counter = Counter(distance_matrix[root])
            if counter[0] > 1:
                distance_to_others(root)
        
        heights = [max(distance_matrix[i]) for i in range(n)]
        min_height = min(heights)
        
        return [i for i, h in enumerate(heights) if h == min_height]