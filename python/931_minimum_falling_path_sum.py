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


class SolutionDPMemoryEfficient:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        max_row, max_col = len(matrix) - 1, len(matrix[0]) - 1

        prev_min_path = matrix[max_row]
        next_min_path = [float('inf')] * (max_col+1)

        for row_index in range(max_row-1, -1, -1):
            # get the min_path_sum from the current cell
            for col_index in range(0, max_col+1):
                for prev_col in [col_index-1, col_index, col_index+1]:
                    if 0 <= prev_col and prev_col <= max_col:
                        next_min_path[col_index] = min(next_min_path[col_index], prev_min_path[prev_col])
                next_min_path[col_index] += matrix[row_index][col_index]

            prev_min_path = next_min_path
            next_min_path = [float('inf')] * (max_col+1)

        return min(prev_min_path)