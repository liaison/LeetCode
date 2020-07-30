class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        dim = len(A)
        
        def shift_and_count(x_shift, y_shift, M, R):
            """ M: matrix to be moved
                R: matrix for reference
                moving one matrix up and left is equivalent to 
                moving the other matrix down and right
            """
            count = 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        count += 1
            return count
        
        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))
        
        return max_overlaps