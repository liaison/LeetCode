
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

@author: Lisong Guo <lisong.guo@me.com>
@date:   July 30, 2018

"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

          return the position to insert a new element into the sorted list.
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


if __name__ == "__main__":
     
    test_case_1_input = ([1,3,5,6], 5)
    test_case_1_target = 2

    solution = Solution()

    print("test case 1:", test_case_1_input)
    assert(test_case_1_target == solution.searchInsert(*test_case_1_input))


    test_case_2_input = ([], 1)
    test_case_2_target = 0
    print("test case 2:", test_case_2_input, ' target:', test_case_2_target)
    print(solution.searchInsert(*test_case_2_input))


    test_case_3_input = ([1,3,5,6], 2)
    test_case_3_target = 1
    print("test case 3:", test_case_3_input, ' target:', test_case_3_target)
    assert(test_case_3_target == solution.searchInsert(*test_case_3_input))


    test_case_4_input = ([1,3,5,6], 7)
    test_case_4_target = 4
    print("test case 4:", test_case_4_input, ' target:', test_case_4_target)
    assert(test_case_4_target == solution.searchInsert(*test_case_4_input))


    test_case_5_input = ([1,3,5,6], 0)
    test_case_5_target = 0
    print("test case 5:", test_case_5_input, ' target:', test_case_5_target)
    assert(test_case_5_target == solution.searchInsert(*test_case_5_input))






