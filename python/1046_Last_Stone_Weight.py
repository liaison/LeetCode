"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, 
    and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left. 
Return the weight of this stone (or 0 if there are no stones left.)

"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        # Since in Python, the heap is implemented as minimum heap,
        # in order to have the maximum heap, we applied a trick here,
        # i.e. we applied the negation on the original values.
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)
        
        while len(neg_stones) > 1:
            y = heapq.heappop(neg_stones)
            x = heapq.heappop(neg_stones)
            if x != y:
                #new_weight = -((-y) - (-x))
                new_weight = y - x
                
                heapq.heappush(neg_stones, new_weight)
        
        if neg_stones:
            return - neg_stones[0]
        else:
            return 0