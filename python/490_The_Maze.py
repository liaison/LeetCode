class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        rows, cols = len(maze), len(maze[0])
        start, destination = tuple(start), tuple(destination)
        
        def next_move(curr, offset):
            next_pos = curr
            while True:
                row, col = next_pos[0] + offset[0], next_pos[1] + offset[1]
                if not (0 <= row < rows) or \
                   not (0 <= col < cols) or \
                   maze[row][col] == 1:   
                    break
                else:
                    next_pos = (row, col)
            return next_pos
    
        
        @lru_cache(maxsize=None)
        def backtrack(curr):
            if curr == destination:
                return True
            
            for offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_pos = next_move(curr, offset)
                if next_pos == curr or \
                    maze[next_pos[0]][next_pos[1]] == -1:
                    continue
                
                # mark the next move
                maze[next_pos[0]][next_pos[1]] = -1
                # try this move              
                ret = backtrack(next_pos)
                # unmark the move
                maze[next_pos[0]][next_pos[1]] = 0
        
                if ret:
                    return True
            return False
        
        return backtrack(start)
