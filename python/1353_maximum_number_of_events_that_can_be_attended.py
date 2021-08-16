class SolutionTLE:
    """
        Solution with Time Limit Exceeded
    """
    def maxEvents(self, events: List[List[int]]) -> int:
        queue = []
        heapq.heapify(queue)

        for event in events:
            start, end = event
            heapq.heappush(queue, (start, end))

        event_cnt = 0
        prev_event = 0
        while queue:
            start, end = heapq.heappop(queue)

            # by default, we do not attend the next event
            next_event = prev_event

            # start the next event as early as possible
            if start > prev_event:
                next_event = start
                event_cnt += 1
                prev_event = next_event

            elif prev_event < end:  # start <= prev_event
                next_event = prev_event + 1
                new_event = (next_event, end)
                heapq.heappush(queue, new_event)

            #else:
            # cannot squeeze the new event in

        return event_cnt



class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort(key = lambda e: e[0])  # sort events by start time

        event_cnt = 0
        event_index = 0
        curr_day = 0

        queue = []

        while event_index < len(events) or queue:

            if not queue:
                # attend as soon as possible
                curr_day = events[event_index][0]

            # given the current day, add all candidate events
            while event_index < len(events) and events[event_index][0] <= curr_day:
                # add the end days of all candidates
                heapq.heappush(queue, events[event_index][1])
                event_index += 1

            # pick the one that ends the earliest
            heapq.heappop(queue)
            event_cnt += 1

            # clean up the candidate queue
            while queue and queue[0] <= curr_day:
                heapq.heappop(queue)

            # move on the next day
            curr_day += 1

        return event_cnt

