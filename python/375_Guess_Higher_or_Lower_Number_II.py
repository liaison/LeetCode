class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def cost(low, high):
            """ minmax algorithm: 
                 the minimal values among all possible (worst) scenarios
            """
            if low >= high:
                return 0
            
            min_cost = float('inf')
            for pivot in range(low, high):
                worst_scenario = pivot + max(cost(low, pivot-1), cost(pivot+1, high))
                min_cost = min(min_cost, worst_scenario)
            
            return min_cost
        
        return cost(0, n)


class SolutionOptimized:
    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def cost(low, high):
            if low >= high:
                return 0
            
            min_cost = float('inf')
            # only consider using the right half of the elments as pivots,
            #   as they are the worst scenarios.
            for pivot in range((low+high)//2, high):
                worst_scenario = pivot + max(cost(low, pivot-1), cost(pivot+1, high))
                min_cost = min(min_cost, worst_scenario)
            
            return min_cost
        
        return cost(1, n)