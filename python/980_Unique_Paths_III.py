"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.


Hint: a standard backtracking problem, similar with 8-queens problem

"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rowNum = len(grid)
        colNum = len(grid[0])
        
        # Find the starting point, and the number of empty cells.
        emptyCount = 0
        startPos = (0, 0)
        for row in range(0, rowNum):
            for col in range(0, colNum):
                cell = grid[row][col] 
                if  cell == 0:
                    emptyCount = emptyCount + 1
                elif cell == 1:
                    startPos = (row, col)
        
        def nextPosition(row, col, dirIndex):
            """ calculate the next valid move """
            nonlocal rowNum, colNum
            # up, right, down, left
            DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            newRow = row + DIRECTIONS[dirIndex][0]
            newCol = col + DIRECTIONS[dirIndex][1]
            if newRow < 0 or newRow >= rowNum:
                return (-1, -1)
            elif newCol < 0 or newCol >= colNum:
                return (-1, -1)
            else:
                return (newRow, newCol)
        
        # A standard backtracking algorithm, to explore all paths.
        visited = set()
        pathCount = 0
        def backtracking(pos):
            nonlocal pathCount
            
            oldRow, oldCol = pos
            for dirIndex in range(0, 4):
                nextPos = nextPosition(oldRow, oldCol, dirIndex)
                if nextPos[0] == -1 or nextPos in visited:
                    continue
        
                row, col = nextPos
                cell = grid[row][col]
                if cell == 2:
                    # reach the destination
                    if len(visited) == emptyCount + 1:
                        pathCount = pathCount + 1
                    # reach the destination, 
                    # exit to avoid the unnecessary exploration
                    continue
                elif cell == -1:
                    continue # obstacle
           
                # possible path, explore further, and mark the option
                visited.add(nextPos)
            
                backtracking(nextPos)
                    
                # unmark the option, try next direction
                visited.remove(nextPos)
        
        visited.add(startPos)
        backtracking(startPos)
        
        return pathCount

