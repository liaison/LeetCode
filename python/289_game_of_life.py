class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def live_neighbors(row, col):
            count = 0
            for ro, co in [(-1, 0), (0, -1), (1, 0), (0, 1),
                           (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                new_row, new_col = row + ro, col + co
                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    if board[new_row][new_col] > 0:
                        count += 1
            return count
        
        for row in range(rows):
            for col in range(cols):            
                count = live_neighbors(row, col)
                
                if board[row][col] == 1:
                    # live cell
                    if count < 2 or count > 3:
                        # mark this cell to become dead later
                        board[row][col] = 2
                    # else the cell live on
                else:
                    # dead cell
                    if count == 3:
                         # mark this cell to become live later
                        board[row][col] = -1
        
        # restore the states properly
        for row in range(rows):
            for col in range(cols):            
                if board[row][col] == 2:
                    board[row][col] = 0
                elif board[row][col] == -1:
                    board[row][col] = 1
