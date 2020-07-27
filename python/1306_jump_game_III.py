class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = deque([start])
        
        while queue:
            # BFS search
            curr = queue.pop()
            
            if arr[curr] == 0:
                return True
            elif arr[curr] == -1:
                continue
            
            for next_index in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= next_index and next_index < len(arr):
                    queue.append(next_index)
        
            arr[curr] = -1
            
        return False