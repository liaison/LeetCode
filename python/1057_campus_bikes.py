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



class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        worker_bike_match = [-1] * len(workers)
        bike_occupied = [False] * len(bikes)

        distance_per_worker = []
        for worker_index, worker in enumerate(workers):
            distance_list = []
            for bike_index, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distance_list.append((distance, worker_index, bike_index))
            # sort the distances for each worker
            distance_list.sort(reverse=True)
            distance_per_worker.append(distance_list)

        match_count = 0

        # init all the shortest distances per worker
        queue = [worker_distance.pop() for worker_distance in distance_per_worker]
        heapq.heapify(queue)

        # multi-headed merge sort
        # (distance, worker_index, bike_index)
        # Keep the worker_index as the pointer to the distance matrix, to pick up the next element if necessary
        while match_count < len(workers):
            # At any moment, the heap contains only the workers that have not yet been assigned a bike
            distance, worker_index, bike_index = heapq.heappop(queue)

            if not bike_occupied[bike_index]:
                match_count += 1
                worker_bike_match[worker_index] = bike_index
                bike_occupied[bike_index] = True
            else:
                # propose another bike to the worker
                heapq.heappush(queue, distance_per_worker[worker_index].pop())

        return worker_bike_match



class SolutionBFS:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def manhattan_distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        queue = [(0, 0, 0)]
        visited = set()

        # Run Dijkstra's algorithm
        while queue:
            cost_so_far, worker_index, bike_mask = heapq.heappop(queue)

            if worker_index == len(workers):
                return cost_so_far

            if bike_mask in visited:
                continue

            for bike_index in range(len(bikes)):
                if bike_mask & (1 << bike_index) == 0:
                    new_mask = bike_mask | (1 << bike_index)

                    new_cost = cost_so_far + manhattan_distance(
                        workers[worker_index], bikes[bike_index])

                    heapq.heappush(queue, (new_cost, worker_index+1, new_mask))

            visited.add(bike_mask)

        return None