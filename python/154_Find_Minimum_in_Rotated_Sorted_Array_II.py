"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

    Input: [1,3,5]
    Output: 1

Example 2:
    Input: [2,2,2,0,1]
    Output: 0
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low = 0
        high = len(nums)-1
        while high > low:
            pivot = low + (high - low) // 2
            # pivot = (low + high) // 2 could overflow
            # Case 1):
            if nums[pivot] < nums[high]:
                high = pivot
                # alternative: high = pivot - 1
                # too aggressive to move the `high` index,
                # it won't work for the test case of [3, 1, 3]
            # Case 2):
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            # Case 3):
            else:
                high -= 1
        # the 'low' and 'high' index converge to the inflection point.
        return nums[low]
