class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7

        # (efficiency, speed)
        metrics = zip(efficiency, speed)
        metrics = sorted(metrics, key=lambda t:t[0], reverse=True)

        speed_heap = []
        speed_sum, perf = 0, 0

        for curr_efficiency, curr_speed in metrics:

            if len(speed_heap) > k-1:
                speed_sum -= heapq.heappop(speed_heap)

            speed_sum += curr_speed
            heapq.heappush(speed_heap, curr_speed)
            perf = max(perf, speed_sum * curr_efficiency)

        return perf % modulo
