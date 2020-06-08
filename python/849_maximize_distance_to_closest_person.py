class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        gaps = []

        # scan the seat arrange to find out all the gaps.
        # Note: when the head or tail is vacant,
        #   the size of gap should be considered as doubled,
        #   since there are no person before the head neither after the tail.
        last_person_index = -1
        for index, seat in enumerate(seats):
            if seat == 1:
                if index - last_person_index > 1:
                    if last_person_index == -1:
                        # special case when the head is vacant.
                        gaps.append(2*(index - 1 - last_person_index))
                    else:
                        gaps.append(index - last_person_index)
                last_person_index = index

        if last_person_index < len(seats)-1:
            # special case when the tail is vacant.
            gaps.append(2*(len(seats) - 1 - last_person_index))

        return int(max(gaps) / 2)


class Solution_MaxGapOnly:
    def maxDistToClosest(self, seats: List[int]) -> int:

        max_gap = 0
        last_person_index = -1
        for index, seat in enumerate(seats):
            if seat == 1:
                if index - last_person_index > 1:
                    if last_person_index == -1:
                        # special case when the head is vacant.
                        max_gap = max(max_gap, index - 1 - last_person_index)
                    else:
                        max_gap = max(max_gap, (index - last_person_index) // 2)
                # update the index
                last_person_index = index

        if last_person_index < len(seats)-1:
            # special case when the tail is vacant.
            max_gap = max(max_gap, len(seats) - 1 - last_person_index)

        return max_gap
