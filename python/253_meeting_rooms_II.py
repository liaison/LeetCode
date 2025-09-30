
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


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        meeting_rooms = []

        intervals.sort(key = lambda x: x[0])

        start, end = intervals[0]
        # meeting_rooms keep the ending time of each meeting
        meeting_rooms.append(end)

        heapq.heapify(meeting_rooms)
        for start, end in intervals[1:]:

            earliest_end = meeting_rooms[0]

            if start >= earliest_end:
                # one room becomes available
                heapq.heappop(meeting_rooms)

            heapq.heappush(meeting_rooms, end)

        return len(meeting_rooms)


import heapq

class Solution:
    def minMeetingRoomsConcise(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        meeting_ends = []

        for interval in intervals:
            start, end = interval

            if len(meeting_ends) == 0:
                heapq.heappush(meeting_ends, end)
                continue

            current_meeting_end = meeting_ends[0]

            if current_meeting_end <= start:
                # vacant this meeting, reuse the meeting room
                heapq.heappop(meeting_ends)

            heapq.heappush(meeting_ends, end)

        return len(meeting_ends)






