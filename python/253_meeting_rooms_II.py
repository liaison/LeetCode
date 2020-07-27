
class SolutionHeap(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """        
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        
        meeting_rooms = []
        heapq.heappush(meeting_rooms, intervals[0][1])
        
        for meeting in intervals[1:]:
            start, end = meeting
            
            # using heap to keep a sliding window of meeting rooms
            if meeting_rooms[0] <= start:
                heapq.heappop(meeting_rooms)
            
            heapq.heappush(meeting_rooms, end)
            
        
        return len(meeting_rooms)