
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


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """
            Backtracking with memoization
        """
        def manhattan_distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        @functools.lru_cache(maxsize=None)
        def min_distance_sum(worker_index, bike_mask):
            """
                All input parameters need to be "hashtable",
                  in order to apply the memoization
            """
            if worker_index == len(workers):
                return 0

            # convert the bitmask to list for backtracking later
            #  since the string is immutable in Python
            bit_mask = [bit for bit in bike_mask]

            ret = float("inf")
            for bike_index, bit in enumerate(bike_mask):
                if bit == "0":
                    new_match = manhattan_distance(workers[worker_index], bikes[bike_index])
                    # mark the bike as occupied
                    bit_mask[bike_index] = "1"
                    ret = min(ret,
                              new_match + min_distance_sum(worker_index+1, "".join(bit_mask)))
                    # backtrack, unmark the bike
                    bit_mask[bike_index] = "0"

            return ret

        bike_mask = ["0" for i in range(len(bikes))]
        return min_distance_sum(0, "".join(bike_mask))
