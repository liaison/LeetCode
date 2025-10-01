class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap_queue = []
        for row_index, array in enumerate(matrix):
            col_index = 0
            new_entry = (array[0], row_index, col_index)
            heap_queue.append(new_entry)

        heapq.heapify(heap_queue)

        while k > 0:
            min_element = heapq.heappop(heap_queue)
            value, row_index, col_index = min_element
            if col_index < len(matrix[row_index]) - 1:
                # push the next candidate number if we haven't reach the end of array
                new_entry = (matrix[row_index][col_index+1], row_index, col_index + 1)
                heapq.heappush(heap_queue, new_entry)

            k -= 1

        return min_element[0]

