class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        # convert the second matrix to column-based vectors
        col_vecs = [[] for i in range(len(mat2[0]))]
        for row in mat2:
            for col_index, col in enumerate(row):
                col_vecs[col_index].append(col)

        result = [[] for i in range(len(mat1))]
        for row_index, row_vec in enumerate(mat1):
            for col_index, col_vec in enumerate(col_vecs):
                dot_product = sum([a*b for (a, b) in zip(row_vec, col_vec)])
                result[row_index].append(dot_product)

        return result
