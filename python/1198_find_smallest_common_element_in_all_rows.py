
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        # using bisect algorithm to binary search for the element
        from bisect import bisect_left
        def index(a, x):
            i = bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return i
            else:
                return -1

        # Greedy algorithm to find the lowest element
        head_line = mat[0]
        for low in head_line:
            exist_in_all = True

            for array in mat[1:]:
                loc = index(array, low)
                if loc == -1:
                    exist_in_all = False
                    break

            if exist_in_all:
                return low

        return -1