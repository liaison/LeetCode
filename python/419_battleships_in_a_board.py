class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        
        ship_count = 0
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '.':
                    continue
    
                # check if both the left and up neighbor are vacant,
                #   then this is the beginning of a new battleship.
                # otherwise we are just traversing part of the battleship.
                offsets = [(0, -1), (-1, 0)]
                vacant = True
                for (row_offset, col_offset) in offsets:
                    neighbor_row, neighbor_col = row + row_offset, col + col_offset
                    if neighbor_row >= 0 and neighbor_col >= 0 \
                        and board[neighbor_row][neighbor_col] == 'X':
                        vacant = False
                        break
                
                if vacant:
                    ship_count += 1
        
        return ship_count