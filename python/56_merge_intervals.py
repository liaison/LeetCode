
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


class SolutionTwoPointers:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        ret = []
        prev_interval = intervals[0]
        for next_interval in intervals[1:]:
            next_start, next_end = next_interval
            prev_start, prev_end = prev_interval

            if prev_end < next_start:
                ret.append(prev_interval)
                prev_interval = next_interval
            else: # prev_end >= next_start
                # overlapping
                new_interval = [prev_start, max(prev_end, next_end)]
                prev_interval = new_interval

        ret.append(prev_interval)

        return ret


