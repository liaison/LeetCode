
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        """
            Dynamic programming in the bottom-up approach
        """
        N = len(days)

        # dp[i] the minimum cost if the travel is of the postfix: days[i:]
        dp = [0] * (N+1)

        # should be the 1-day pass, if the input is designed properly
        # i.e. one day should be the least expensive of all.
        # the minimal cost of ticket if the travel plan consists of one day
        dp[N-1] = min(costs)

        for index in range(N-2, -1, -1):
            curr_day = days[index]
            min_cost = float('inf')

            # Try different plans from the current day till the end
            for ci, duration in enumerate([1, 7, 30]):
                next_day_index = index
                while next_day_index < N and days[next_day_index] < curr_day + duration :
                    next_day_index += 1

                min_cost = min(min_cost, costs[ci] + dp[next_day_index])
            # fill the best plan for the postfix plan, days[index:]
            dp[index] = min_cost

        return dp[0]
