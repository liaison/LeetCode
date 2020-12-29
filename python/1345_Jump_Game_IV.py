class Solution:
    def minJumps(self, arr) -> int:
        
        # value: [indices]
        graph = defaultdict(set)
        
        for index, value in enumerate(arr):
            graph[value].add(index)
        
        queue = deque([0])
        visited = [False for i in range(len(arr))]
        target = len(arr) - 1
        steps = 0
                
        while queue:
            level_size = len(queue)
                                    
            for i in range(level_size):
                curr = queue.popleft()
                
                if curr == target:
                    return steps
                visited[curr] = True
                
                for neighbor in graph[arr[curr]]:
                    if not visited[neighbor]:
                        queue.append(neighbor)

                graph[arr[curr]].clear()
                        
                for neighbor in [curr-1, curr+1]:
                    if 0 <= neighbor <= target and not visited[neighbor]:
                        queue.append(neighbor)
            
            steps += 1
        
        return steps
    
