

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda x:x[1])

        # minimal arrows
        arrow_count = 1

        # starting from the first ballon
        curr_end = points[0][1]

        for (start, end) in points:
            # Use one arrow to burst all ballons in an overlapped interval
            if curr_end < start:
                arrow_count += 1
                curr_end = end

        return arrow_count