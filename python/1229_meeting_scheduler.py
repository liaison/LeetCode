class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort()
        slots2.sort()

        cursor_a, cursor_b = 0, 0
        len_a, len_b = len(slots1), len(slots2)

        while (cursor_a < len_a and cursor_b < len_b):

            start_a, end_a = slots1[cursor_a]
            start_b, end_b = slots2[cursor_b]

            meeting_start = max(start_a, start_b)
            meeting_end = min(end_a, end_b)

            if meeting_end - meeting_start >= duration:
                return [meeting_start, meeting_start + duration]

            # move on the next cursor.
            # key point is to move the slot that ends earlier, rather than the one start earlier
            if end_a < end_b:
                cursor_a = cursor_a + 1
            else:
                cursor_b = cursor_b + 1

        return []

