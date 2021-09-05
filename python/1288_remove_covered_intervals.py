
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        # Order intervals first by the starting in ascending order,
        # if two intervals have the same starting point, then order the ends in descending order.
        # Since we check the inclusion in the reserved ordre,
        #  i.e. for intervals[i], check if it is included by any of the previous intervals[0...i-1]
        intervals.sort(key = lambda x: (x[0], -x[1]))

        remaining_intervals = len(intervals)

        for curr in range(len(intervals)-1, 0, -1):
            is_covered = False

            _, curr_end = intervals[curr]

            for prev in range(curr-1, -1, -1):
                _, prev_end = intervals[prev]
                if prev_end >= curr_end:
                    is_covered = True
                    break

            if is_covered:
                remaining_intervals -= 1

        return remaining_intervals
