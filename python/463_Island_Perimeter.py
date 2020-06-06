
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def shoreCount(row, col):
            count = 0
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for rowOffset, colOffset in directions:
                newRow, newCol = row+rowOffset, col+colOffset
                if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS:
                    count += 1
                elif grid[newRow][newCol] == 0:
                    count += 1
            return count
        
        perimeter = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    perimeter += shoreCount(row, col)
        
        return perimeter
