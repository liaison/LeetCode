class Solution:
    def customSortString(self, order: str, s: str) -> str:

        # using order to define the priority/order of each letter
        letter_priority = {}
        for index, letter in enumerate(order):
            letter_priority[letter] = index

        # apply the priority for each letter
        # Note: by default, for letter with unknown priority, we put them in the front
        heap = []
        heapq.heapify(heap)
        for letter in s:
            priority = -1
            if letter in letter_priority:
                priority = letter_priority[letter]
            heapq.heappush(heap, (priority, letter))

        output = []
        while heap:
            priority, letter = heapq.heappop(heap)
            output.append(letter)

        return "".join(output)