class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count = 0

        slide_window = defaultdict(int)
        for index, letter in enumerate(s):
            if index < k:
                slide_window[letter] += 1
            else:
                slide_window[letter] += 1
                popped = s[index-k]
                slide_window[popped] -= 1
                if slide_window[popped] == 0:
                    del slide_window[popped]

            # check the characters once the sliding window is fully filled.
            if index >= k-1 and len(slide_window) == k:
                count += 1

        return count