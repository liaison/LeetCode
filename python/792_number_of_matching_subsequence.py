

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        letter_indices = defaultdict(list)
        for index, letter in enumerate(s):
            letter_indices[letter].append(index)

        def isSubsequence(word):
            """
                Greedy matching which ensures to find a solution if there exists one.

                XYZ    -->    ****X****Y*****Z***
            """
            cursor = -1
            for letter in word:
                if letter not in letter_indices:
                    return False

                indices = letter_indices[letter]
                first_match = bisect.bisect_right(indices, cursor)

                if first_match == len(indices):
                    # no match
                    return False
                else:
            return True

        count = 0
        for word in words:
            if isSubsequence(word):
                count += 1
        return count

