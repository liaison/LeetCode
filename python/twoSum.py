
"""
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and 
you may not use the same element twice.

@author: Lisong Guo <lisong.guo@me.com>
@date:   July 31, 2018

"""
class Solution:
    def _twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

            Setup two pointers from both ends, approach the middle point.
            Complexity O(n)
        """
        low = 0
        high = len(numbers) - 1

        while (low < high):
            two_sum = numbers[low] + numbers[high]
            if (two_sum == target):
                break
            elif (two_sum > target):
                high -= 1
            else:
                low += 1

        return [low+1, high+1]


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


    def twoSum(self, numbers, target):
        
        sub_target = target - numbers[0]

        # use the binary search to reduce the upper bound
        low = 0
        high = self.searchInsert(numbers, sub_target)
       
        if (high == len(numbers)):
            high -= 1

        if (numbers[high] == sub_target):
            return [low+1, high+1]
        
        while (low < high):
            two_sum = numbers[low] + numbers[high]
            if (two_sum == target):
                break
            elif (two_sum > target):
                high -= 1
            else:
                low += 1

        return [low+1, high+1]


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

    test_case_1_input = ([2,7,11,15], 9)
    test_case_1_target = [1, 2]
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.twoSum)


    test_case_2_input = ([5, 25, 75], 100)
    test_case_2_target = [2, 3]
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.twoSum)


