
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        array = [0] * length

        # update the boundaries with delta values
        for start, end, delta in updates:
            array[start] += delta
            if end < length - 1:
                array[end + 1] -= delta

        # calculate the cumulative sum / prefix_sum
        prefix_sum = 0
        for index in range(length):
            array[index] += prefix_sum
            prefix_sum = array[index]

        return array
