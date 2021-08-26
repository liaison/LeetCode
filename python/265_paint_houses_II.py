
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
            Dynamic Programming
        """
        n_houses = len(costs)
        n_colors = len(costs[0])

        # dp[house_index][color_index]:
        #    minimal cost of painting the curent house with the color[color_index]
        #     together with all previous houses (0.1...house_index-1) painted as well.
        dp = [[0] * n_colors for _ in range(n_houses+1)]

        for house_index in range(1, n_houses+1):
            for curr_color in range(n_colors):
                min_cost = float('inf')
                for prev_color in range(n_colors):
                    # exclude the current color for the previous house
                    if curr_color == prev_color:
                        continue
                    new_cost = costs[house_index-1][curr_color] + dp[house_index-1][prev_color]
                    min_cost = min(min_cost, new_cost)

                # the minimal cost to paint the current house in 'curr_color'
                dp[house_index][curr_color] = min_cost

        # minimal cost to paint all houses (0.1....house_index)
        return min(dp[-1])


class SolutionDFS:
    def minCostII(self, costs: List[List[int]]) -> int:

        n_houses = len(costs)
        n_colors = len(costs[0])

        @functools.lru_cache(maxsize=None)
        def dfs(house_index, color_index):
            if house_index == 0:
                return 0

            min_cost = float('inf')
            for next_color in range(n_colors):
                if next_color == color_index:
                    continue
                new_cost = costs[house_index-1][color_index] + dfs(house_index-1, next_color)
                min_cost = min(min_cost, new_cost)

            return min_cost

        min_cost = float('inf')
        for color_index in range(n_colors):
            min_cost = min(min_cost, dfs(n_houses, color_index))

        return min_cost
