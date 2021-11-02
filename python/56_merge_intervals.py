
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])

        merged = []
        for interval in intervals:
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                # add a new interval
                merged.append(interval)
            else:
                # update the previous interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

