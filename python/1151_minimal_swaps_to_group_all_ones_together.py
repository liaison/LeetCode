class Solution:
    def minSwaps(self, data: List[int]) -> int:

        ones = 0
        for bit in data:
            if bit == 1:
                ones += 1

        if ones in [0, 1, len(data)]:
            return 0

        swaps = 0
        slide_window = deque(data[0:ones])
        for bit in slide_window:
            if bit == 0:
                swaps += 1

        min_swaps = swaps
        for bit in data[ones:]:

            slide_window.append(bit)
            if bit == 0:
                swaps += 1

            if slide_window.popleft() == 0:
                swaps -= 1

            min_swaps = min(min_swaps, swaps)

        return min_swaps
