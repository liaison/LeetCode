
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



class SolutionMergeK:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        k_cursors = [0 for _ in range(len(mat))]
        cursor_num = len(k_cursors)
        row_length = len(mat[0])
        curr_max, curr_cnt = 0, 0

        while True:
            for k in range(cursor_num):

                cursor = k_cursors[k]
                while cursor < row_length and mat[k][cursor] < curr_max:
                    cursor += 1

                # exceed one of the rows
                if cursor == row_length:
                    return -1

                k_cursors[k] = cursor
                if mat[k][cursor] > curr_max:
                    # reset the max value and its counter
                    curr_max = mat[k][cursor]
                    curr_cnt = 1
                else: # mat[k][cursor] == curr_max
                    curr_cnt += 1
                    if curr_cnt == cursor_num:
                        return curr_max
