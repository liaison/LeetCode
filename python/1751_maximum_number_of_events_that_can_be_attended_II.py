class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort(key = lambda x: x[0])

        @functools.lru_cache(maxsize=None)
        def dfs(event_index, remain_k):
            if remain_k == 0 or event_index == len(events):
                return 0

            if remain_k == 1:
                return max([event[2] for event in events[event_index:]])

            not_included = dfs(event_index+1, remain_k)

            # linear search
            current_end = events[event_index][1]
            next_index = len(events)
            for index in range(event_index+1, len(events)):
                if events[index][0] > current_end:
                    next_index = index
                    break

            included = events[event_index][2] + dfs(next_index, remain_k - 1)

            return max(not_included, included)


        return dfs(0, k)


class SolutionWithBinarySearch:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort(key = lambda x: x[0])

        start_days = [event[0] for event in events]

        @functools.lru_cache(maxsize=None)
        def dfs(event_index, remain_k):
            if remain_k == 0 or event_index == len(events):
                return 0

            if remain_k == 1:
                return max([event[2] for event in events[event_index:]])

            not_included = dfs(event_index+1, remain_k)

            # binary search on the next available event
            current_end = events[event_index][1]
            next_index = bisect.bisect_right(start_days, current_end, lo = event_index+1)

            included = events[event_index][2] + dfs(next_index, remain_k - 1)

            return max(not_included, included)


        return dfs(0, k)