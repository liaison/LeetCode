class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        pair_sum, array_index_1, array_index_2 = nums1[0] + nums2[0], 0, 0
        heap_queue = [(pair_sum, array_index_1, array_index_2)]

        array_len_1, array_len_2 = len(nums1), len(nums2)
        heapq.heapify(heap_queue)

        pairs = []
        visited = set((array_index_1, array_index_2))
        while k > 0:
            pair_sum, array_index_1, array_index_2 = heapq.heappop(heap_queue)

            if array_index_1 < array_len_1 - 1 and (array_index_1 + 1, array_index_2) not in visited:
                new_entry = (
                    nums1[array_index_1 + 1] + nums2[array_index_2],
                    array_index_1 + 1,
                    array_index_2
                )
                visited.add((array_index_1 + 1, array_index_2))
                heapq.heappush(heap_queue, new_entry)

            if array_index_2 < array_len_2 - 1 and (array_index_1, array_index_2 + 1) not in visited:
                new_entry = (
                    nums1[array_index_1] + nums2[array_index_2 + 1],
                    array_index_1,
                    array_index_2 + 1
                )
                visited.add((array_index_1, array_index_2 + 1))
                heapq.heappush(heap_queue, new_entry)

            pairs.append((nums1[array_index_1], nums2[array_index_2]))

            k -= 1

        return pairs
