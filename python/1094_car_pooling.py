
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:


        capacity_changes = []

        for psg, start, end in trips:
            # capacity decrease at pickup and increase at dropoff
            # for overlapping intervals, we should drop-off first then pickup.
            #  as a result, the second element should also play a role in ordering
            # Note: we must priroitize the dropoff before pickup
            capacity_changes.append((start, psg))
            capacity_changes.append((end, -psg))

        heapq.heapify(capacity_changes)

        used_capacity = 0
        while capacity_changes:
            timestamp, capacity_delta = heapq.heappop(capacity_changes)
            used_capacity += capacity_delta

            if used_capacity > capacity:
                return False

        return True
