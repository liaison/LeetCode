

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
          Rotate the matrix layer by layer like onion, in clock-wise direction.
          e.g The outter most layer consists of the elements on the four edges.
        """
        edge_len = len(matrix)

        for x in range(0, int(edge_len/2)):
            for y in range(x, edge_len-x-1):
                #store the current cell. This is the top edge as well.
                temp = matrix[x][y]
                # move the left edge to the top
                matrix[x][y] = matrix[edge_len-1-y][x]
                # move the bottom edge to the left
                matrix[edge_len-1-y][x] = matrix[edge_len-1-x][edge_len-1-y]
                # move the right edge to the bottom
                matrix[edge_len-1-x][edge_len-1-y] = matrix[y][edge_len-1-x]
                # and finally move the top edge to the right
                matrix[y][edge_len-1-x] = temp


def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    # the return values is carried within the modified input
    print(case_name, test_input)
    
    test_func(test_input)

    print(' target:', test_target,
          ' output:', test_input)
    assert(test_target == test_input)


if __name__ == "__main__":

    solution = Solution()

    test_case_1_input = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    test_case_1_target = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]

    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.rotate)










