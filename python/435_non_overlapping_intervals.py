
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])

        eliminate_count = 0

        curr_end = intervals[0][1]

        # Eliminate the intervals at early as possible greedily
        for (start, end) in intervals[1:]:
            if start < curr_end:
                # eliminate the current overlapped interval,
                #   since if we keep it, it would have a greater chance to overlap with the following intervals
                eliminate_count += 1
            else:
                curr_end = end

        return eliminate_count