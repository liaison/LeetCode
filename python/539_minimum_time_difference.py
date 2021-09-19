
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def to_minutes(time_str):
            hh = int(time_str[0:2])
            mm = int(time_str[3:])
            return hh * 60 + mm

        timestamps = []
        for time_str in timePoints:
            timestamps.append(to_minutes(time_str))

        timestamps.sort()
        min_gap = float('inf')
        for index in range(1, len(timestamps)):
            min_gap = min(min_gap, timestamps[index] - timestamps[index-1])

        tail_to_head = 24 * 60 - timestamps[-1] + timestamps[0]
        min_gap = min(min_gap, tail_to_head)

        return min_gap
