
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """
            Naive Backtracking algorithm
            Time Limit Exceeded
        """
        min_distance_sum = float('inf')

        def swap(one, other):
            if one != other:
                bikes[one], bikes[other] = bikes[other], bikes[one]

        def manhattan_distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        def calculate_distance_sum():
            distance_sum = 0
            for index in range(len(workers)):
                distance_sum += manhattan_distance(workers[index], bikes[index])
            return distance_sum

        def backtrack(bike_index):
            nonlocal min_distance_sum

            if bike_index == len(workers):
                new_distance_sum = calculate_distance_sum()
                min_distance_sum = min(min_distance_sum, new_distance_sum)
                return

            # permutation to generate matches between workers and bikes
            for next_index in range(bike_index, len(bikes)):
                swap(bike_index, next_index)
                backtrack(bike_index + 1)
                swap(bike_index, next_index)


        backtrack(0)
        return min_distance_sum