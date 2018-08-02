

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # length of the square
        N = len(matrix)
        if (N == 0):
            return False

        M = len(matrix[0])

        start, end =0, N * M

        while (start < end):
            mid = int((start+end)/2)
            pivot = matrix[int(mid/M)][mid%M]
            if (pivot == target):
                return True
            elif (pivot < target):
                start = mid + 1
            else:
                end = mid

        return False



def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    actual_output = test_func(*test_input)
    print(case_name, test_input, ' target:', test_target,
          ' output:', actual_output)
    assert(test_target == actual_output)


if __name__ == "__main__":

    solution = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    test_case_1_input = (matrix, 3)
    test_case_1_target = True
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.searchMatrix)

    test_case_2_input = (matrix, 4)
    test_case_2_target = False
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.searchMatrix)

    test_case_3_input = ([], 4)
    test_case_3_target = False
    verify('test case 3:',
           test_case_3_input, test_case_3_target, solution.searchMatrix)

    test_case_4_input = ([[1]], 1)
    test_case_4_target = True
    verify('test case 4:',
           test_case_4_input, test_case_4_target, solution.searchMatrix)




