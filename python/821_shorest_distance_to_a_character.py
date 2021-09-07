class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        target_indices = []
        for index, letter in enumerate(s):
            if c == letter:
                target_indices.append(index)

        result = []
        for index, letter in enumerate(s):
            if letter == c:
                result.append(0)
            else:
                to_insert = bisect.bisect_left(target_indices, index)
                if to_insert == 0:
                    distance = abs(index - target_indices[0])
                    result.append(distance)
                elif to_insert == len(target_indices):
                    distance = abs(index - target_indices[-1])
                    result.append(distance)
                else:
                    left_distance = abs(index - target_indices[to_insert-1])
                    right_distance = abs(index - target_indices[to_insert])
                    result.append(min(left_distance, right_distance))

        return result

