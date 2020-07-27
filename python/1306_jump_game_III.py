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


class SolutionDP:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        @lru_cache(maxsize=None)
        def dp(curr):
            
            if 0 > curr or curr >= len(arr):
                return False
            elif arr[curr] == 0:
                return True
            elif arr[curr] < 0:
                return False
            
            arr[curr] = -arr[curr]
            return dp(curr + arr[curr]) or dp(curr - arr[curr])
        
        return dp(start)
    

class SolutionBacktrack:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def backtrack(curr):
            
            if arr[curr] == 0:
                return True
            elif arr[curr] == -1:
                return False
            
            temp = arr[curr]
            for next_index in [curr + arr[curr], curr - arr[curr]]:
                arr[curr] = -1
                if 0 <= next_index and next_index < len(arr):
                    if backtrack(next_index):
                        return True
                arr[curr] = temp
            return False
                
        return backtrack(start)
