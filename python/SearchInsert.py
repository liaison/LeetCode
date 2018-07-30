
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

@author: Lisong Guo <lisong.guo@me.com>
@date:   July 30, 2018

"""
class Solution:
    def _searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

          return the position to insert a new element into the sorted list.
          Note: the solution can be implemented in a recursive way.
        """
        size = len(nums)
        if (size == 0):
            # empty input list, early exit
            return 0

        mid_index = int(size/2)
        if (nums[mid_index] == target):
            return mid_index 
        elif (nums[mid_index] > target):
            return self.searchInsert(nums[0:mid_index], target)
        else:
            return mid_index + 1 + self.searchInsert(nums[mid_index+1:], target)


    def searchInsert(self, nums, target):
        return self.tail_recursive_searchInsert(0, nums, target)


    def tail_recursive_searchInsert(self, start, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

          return the position to insert a new element into the sorted list.
          Note: the solution can be implemented in a recursive way.
        """
        size = len(nums)
        if (size == 0):
            # empty input list, early exit
            return start

        mid_index = int(size/2)
        if (nums[mid_index] == target):
            return start + mid_index 
        elif (nums[mid_index] > target):
            return self.tail_recursive_searchInsert(
                            start, nums[0:mid_index], target)
        else:
            return self.tail_recursive_searchInsert(
                            start+mid_index+1, nums[mid_index+1:], target)


def verify(case_name, test_input, test_target):
    """
       utility function for unit testing
    """
    solution = Solution()
    print(case_name, test_input, ' target:', test_target)
    assert(test_target == solution.searchInsert(*test_input))


if __name__ == "__main__":

    solution = Solution()

    test_case_1_input = ([1,3,5,6], 5)
    test_case_1_target = 2
    verify('test case 1:', test_case_1_input, test_case_1_target)

    test_case_2_input = ([], 1)
    test_case_2_target = 0
    verify('test case 2 (empty list):', test_case_2_input, test_case_2_target)

    test_case_3_input = ([1,3,5,6], 2)
    test_case_3_target = 1
    verify("test case 3:", test_case_3_input, test_case_3_target)

    test_case_4_input = ([1,3,5,6], 7)
    test_case_4_target = 4
    verify("test case 4:", test_case_4_input, test_case_4_target)

    test_case_5_input = ([1,3,5,6], 0)
    test_case_5_target = 0
    verify("test case 5:", test_case_5_input, test_case_5_target)






