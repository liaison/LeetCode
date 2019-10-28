'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true

Example 2:

    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false

Follow up:

    - This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
    - Would this affect the run-time complexity? How and why?
'''
class Solution:
    
    def search(self, nums: List[int], target: int) -> bool:

        def binary_search(low, high, nums, target):
            if low > high:
                return False

            pivot = int((low+high)/2)
            if nums[pivot] == target:
                return True

            is_same_side = (nums[pivot] < nums[0]) == (target < nums[0])

            if is_same_side:
                comparator = nums[pivot]
            else:
                # using the nums[0] as the pivot
                comparator = float('-inf') if target < nums[0] else float('inf')

            if target < comparator:
                high = pivot - 1
            else:
                low = pivot + 1        
            return binary_search(low, high, nums, target)

        # avoid the case when the head and the tail are duplicates
        high = len(nums)-1
        while high > 0:
            if nums[high] != nums[0]:
                break
            high -= 1

        return binary_search(0, high, nums, target)

    
class SolutionIteration:

    def search(self, nums: List[int], target: int) -> bool:

        low = 0
        # avoid the case when the head and the tail are duplicates
        high = len(nums)-1
        while high > 0:
            if nums[high] != nums[0]:
                break
            high -= 1

        while low <= high:
            pivot = int((low+high)/2)
            if nums[pivot] == target:
                return True

            is_same_side = (nums[pivot] < nums[0]) == (target < nums[0])

            if is_same_side:
                comparator = nums[pivot]
            else:
                # using the nums[0] as the reversed comparator
                comparator = float('-inf') if target < nums[0] else float('inf')

            if target < comparator:
                high = pivot - 1
            else:
                low = pivot + 1

        return False