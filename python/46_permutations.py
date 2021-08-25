
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []

        def swap(array, a, b):
            if a != b:
                array[a], array[b] = array[b], array[a]

        def backtrack(start, array):
            nonlocal output
            """
                Generate permutation for the subarray[start:]

                when we reach the last subarray, the permutation is formed inside the array.
            """
            if start == len(array):
                output.append(list(array))
                return

            for next_index in range(start, len(array)):
                swap(array, next_index, start)

                # move on the subarray, i.e. array[start+1:]
                backtrack(start + 1, array)

                swap(array, next_index, start)

        backtrack(0, nums)
        return output


