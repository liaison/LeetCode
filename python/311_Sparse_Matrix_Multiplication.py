class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        # convert the second matrix to column-based vectors
        col_vecs = [[] for i in range(len(B[0]))]
        for row in B:
            for col_index, col in enumerate(row):
                col_vecs[col_index].append(col)
        
        result = [[] for i in range(len(A))]
        for row_index, row_vec in enumerate(A):
            for col_index, col_vec in enumerate(col_vecs):
                dotsum = sum([a*b for (a, b) in zip(row_vec, col_vec)])
                result[row_index].append(dotsum)
        
        return result
