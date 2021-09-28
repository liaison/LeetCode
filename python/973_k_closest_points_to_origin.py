class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance_queue = []

        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            distance_queue.append((distance, [x, y]))

        heapq.heapify(distance_queue)
        output = []
        while k:
            distance, point = heapq.heappop(distance_queue)
            output.append(point)
            k -= 1

        return output