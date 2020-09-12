class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key = lambda x: x[0])
        
        for curr in range(0, len(intervals)-1):
            curr_interval = intervals[curr]
            next_interval = intervals[curr+1]
            if curr_interval[1] > next_interval[0]:
                return False
        
        return True
