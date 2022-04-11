class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        min_sum_map = dict()
        max_row, max_col = len(matrix) - 1, len(matrix[0]) - 1

        def min_path(row, col):
            nonlocal min_sum_map

            if (row, col) in min_sum_map:
                return min_sum_map[(row, col)]

            if row == max_row:
                min_sum_map[(row, col)] = matrix[row][col]
                return min_sum_map[(row, col)]

            remain_path = float("inf")
            next_row = row + 1
            for next_col in [col-1, col, col+1]:
                if 0 <= next_col and next_col <= max_col:
                    curr_min = min_path(next_row, next_col)
                    remain_path = min(curr_min, remain_path)

            min_sum_map[(row, col)] = matrix[row][col] + remain_path
            return min_sum_map[(row, col)]

        result = float("inf")
        for col in range(0, max_col+1):
            result = min(result, min_path(0, col))

        return result