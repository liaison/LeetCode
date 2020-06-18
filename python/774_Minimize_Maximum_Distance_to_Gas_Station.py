class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        
        interval_queue = []
        for i in range(len(stations)-1):
            #-(length), length, num_of_ga_station
            interval = stations[i+1] - stations[i]
            interval_queue.append((-interval, interval, 1))
        
        # heapify the interval queue
        heapq.heapify(interval_queue)
        
        # add gas stations GREEDILY, one by one.
        #   at each step, add it to the maximal interval
        for _ in range(K):
            weight, interval, num_gas = heapq.heappop(interval_queue)
            num_gas += 1
            weight = - interval / num_gas
            heapq.heappush(interval_queue, (weight, interval, num_gas))
        
        return -interval_queue[0][0]