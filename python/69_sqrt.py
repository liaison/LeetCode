

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
            Complexity O(1)
        """
        ans = 0
        bit = 1 << 16
        while (bit > 0):
            # add the current bit to the result
            ans |= bit
            if (ans * ans > x):
                # reverse the current bit from 1 to 0
                ans ^= bit
            bit >>= 1
        
        return ans


def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    actual_output = test_func(*test_input)
    print(case_name, test_input, ' target:', test_target,
          ' output:', actual_output)
    assert(test_target == actual_output)


import sys

if __name__ == "__main__":

    solution = Solution()

    test_case_1_input = (4, )
    test_case_1_target = 2
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.mySqrt)
    
    test_case_2_input = (8, )
    test_case_2_target = 2
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.mySqrt)
    
    test_case_3_input = (67, )
    test_case_3_target = 8
    verify('test case 3:',
           test_case_3_input, test_case_3_target, solution.mySqrt)
    
    test_case_4_input = (5, )
    test_case_4_target = 2
    verify('test case 4:',
           test_case_4_input, test_case_4_target, solution.mySqrt)
