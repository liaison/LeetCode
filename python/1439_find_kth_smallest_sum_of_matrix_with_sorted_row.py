class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        queue = []
        col_index = 0
        n_rows, n_cols = len(mat), len(mat[0])

        col_array = [0] * n_rows

        queue_sum = sum([mat[row][0] for row in range(n_rows)])

        queue.append((queue_sum, col_array))
        heapq.heapify(queue)

        seen = set(tuple(col_array))

        while k:
            curr_sum, col_array = heapq.heappop(queue)
            k -= 1

            for row_index, col_index in enumerate(col_array):
                if col_index + 1 < n_cols:
                    new_sum = curr_sum - mat[row_index][col_index] + mat[row_index][col_index+1]
                    new_col_array = col_array.copy()
                    new_col_array[row_index] = col_index + 1

                    key = tuple(new_col_array)
                    if key in seen:
                        continue

                    seen.add(key)
                    heapq.heappush(queue, (new_sum, new_col_array))

        return curr_sum

