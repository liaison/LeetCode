
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
            Greedily search for the matches,
                give each letter a second chance to start the match from the beginning of source.
            The number of the startover chances is also the number of subsequences.
        """
        letter_indices = defaultdict(list)
        for index, letter in enumerate(source):
            letter_indices[letter].append(index)

        def find_subsequence(letter, cursor):
            indices = letter_indices[letter]
            first_match = bisect.bisect_right(indices, cursor)
            if first_match == len(indices):
                return (False, None)
            else:
                return (True, indices[first_match])


        cursor = -1
        startover_count = 1
        for letter in target:

            if letter not in letter_indices:
                return -1

            # give each letter a second chance to startover
            retry = False
            while True:
                found, next_cursor = find_subsequence(letter, cursor)
                if found:
                    cursor = next_cursor
                    break
                else:
                    if not retry:
                        retry = True
                        cursor = -1
                    else:
                        break

            if found:
                if retry:
                    startover_count += 1
            else:
                return -1

        return startover_count


