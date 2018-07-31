

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
            Apply the revised binary search to prune the search space
        """
        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = int((low+high)/2)

            if (nums[mid] > nums[mid+1]):
                # search the descending slope
                high = mid
            else:
                # search the ascending slope
                low = mid + 1

        return low


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

    test_case_1_input = ([1,2,3,1], )
    test_case_1_target = 2
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.findPeakElement)

    test_case_2_input = ([1,2,1,3,5,6,4], )
    test_case_2_target = 5
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.findPeakElement)

    test_case_3_input = ([1], )
    test_case_3_target = 0
    verify('test case 3:',
           test_case_3_input, test_case_3_target, solution.findPeakElement)

    test_case_4_input = ([1, 2], )
    test_case_4_target = 1
    verify('test case 4:',
           test_case_4_input, test_case_4_target, solution.findPeakElement)







