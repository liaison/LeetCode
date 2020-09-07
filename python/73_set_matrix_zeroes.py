class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        column_header = matrix[0]
        col_size = len(column_header)
        
        # whether to reset the header later
        reset_header = False
        for header in column_header:
            if header == 0:
                reset_header = True
        
        # use the first row as the indicator to reset columns
        for row in range(1, len(matrix)):
            reset_row = False
            for col in range(col_size):
                if matrix[row][col] == 0:
                    column_header[col] = 0
                    reset_row = True
            
            if reset_row:
                matrix[row] = [0] * col_size
        
        # reset columns
        for col in range(col_size):
            if column_header[col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        # reset the column indicator if necessary
        if reset_header:
            matrix[0] = [0] * col_size
        
        