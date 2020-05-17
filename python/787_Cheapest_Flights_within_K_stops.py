class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        graph = defaultdict(list)
        for flight in flights:
            flight_src, flight_dst, flight_price = flight
            graph[flight_src].append((flight_dst, flight_price))
        
        minPriceMap = dict()
        minPriceMap[src] = 0
        minPriceMap[dst] = float('inf')
        
        queue = deque([src])
        stops = 0
        while queue and stops < K + 1:
            
            level_length = len(queue)
            for _ in range(level_length):
                curr_src = queue.popleft()
                
               # update the min price            
                for curr_dst, curr_price in graph[curr_src]:
                    
                    # update the min price
                    if stops == K and curr_dst != dst:
                        continue
                
                    another_price = minPriceMap[curr_src] + curr_price
                    if curr_dst not in minPriceMap or another_price < minPriceMap[curr_dst]:
                        minPriceMap[curr_dst] = another_price
                        queue.append(curr_dst)
            
            stops += 1
    
        # return the min price if there is any
        return -1 if minPriceMap[dst] == float('inf') else minPriceMap[dst]
