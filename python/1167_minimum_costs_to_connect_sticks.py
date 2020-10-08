class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heapq.heapify(sticks)
        
        # Greedily merge two sticks together
        #  since the sticks merged earlier would accumulate the costs over the time
        costs = 0 
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            new_stick = x + y
            heapq.heappush(sticks, new_stick)
            costs += new_stick
        
        return costs
