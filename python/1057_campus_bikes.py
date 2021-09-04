class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        def manhattan_distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        distance_worker_bike = []

        worker_bike_match = [-1] * len(workers)
        bike_occupied = [False] * len(bikes)

        for worker_index, worker in enumerate(workers):
            for bike_index, bike in enumerate(bikes):
                distance_worker_bike.append((manhattan_distance(worker, bike), worker_index, bike_index))

        # order all possible matches in the order of (distance, worker_index, bike_index)
        distance_worker_bike.sort()

        match_count = 0
        for distance, worker_index, bike_index in distance_worker_bike:
            # greedily find all the matches
            if worker_bike_match[worker_index] == -1 and not bike_occupied[bike_index]:
                match_count += 1
                worker_bike_match[worker_index] = bike_index
                bike_occupied[bike_index] = True

            if match_count == len(workers):
                break

        return worker_bike_match