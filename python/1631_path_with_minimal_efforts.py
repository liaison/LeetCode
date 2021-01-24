class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows, cols = len(heights), len(heights[0])
        
        def canReach(curr, visited, min_effort):
            if curr == (rows-1, cols-1):
                return True
            
            # right, down, left, up, 
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            row, col = curr
            for (ro, co) in directions:
                next_row, next_col = row + ro, col + co    
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if not visited[next_row][next_col]:
                        effort = abs(heights[next_row][next_col] - heights[row][col])
            
                        if effort > min_effort:
                            continue

                        visited[next_row][next_col] = True
                        if canReach((next_row, next_col), visited, min_effort):
                            return True
                
            return False
        

        low, high = 0, 10000000
        mid = 0
        
        while low < high:
            mid = (low + high) // 2
            
            curr = (0, 0)
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
            if canReach(curr, visited, mid):
                high = mid
            else:
                low = mid + 1
            
        return low
    
    


class Solution:
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
            Time Limit Exceeded
        """
        rows, cols = len(heights), len(heights[0])
        
        min_effort = float("inf")
        
        def backtrack(curr, visited, prev_effort):
            nonlocal min_effort
                        
            if curr == (rows-1, cols-1):
                min_effort = min(prev_effort, min_effort)
                return True
            
            # right, down, left, up, 
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            row, col = curr
            next_steps = []
            for (ro, co) in directions:
                next_row, next_col = row + ro, col + co    
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if (next_row, next_col) not in visited:
                        effort = abs(heights[next_row][next_col] - heights[row][col])
                        next_steps.append((next_row, next_col, effort))
            
            #next_steps.sort(key = lambda x: x[2])
            
            for (row, col, effort) in next_steps:
                visited.add((row, col))
                next_effort = max(prev_effort, effort)
                backtrack((row, col), visited, next_effort)
                visited.remove((row, col))
            
        curr = (0, 0)
        visited = set()
        visited.add((0,0))
        
        backtrack(curr, visited, 0)
        
        return min_effort
    
    
        

                    