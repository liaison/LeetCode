class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        min_value, max_value = float('inf'), float('-inf')
        max_distance = float('-inf')

        for array in arrays:
            curr_min, curr_max = array[0], array[-1]

            max_distance = max(
                max_distance,
                max_value - curr_min,
                curr_max - min_value
            )

            min_value = min(min_value, curr_min)
            max_value = max(max_value, curr_max)

        return max_distance
