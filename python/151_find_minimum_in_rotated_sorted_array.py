'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        # the original array is either contains a single element
        #  or is actually not rotated
        if low == len(nums) - 1 or nums[low] < nums[high]:
            return nums[low]

        while low < high:
            pivot = int((low+high)/2)
            #print('old', low, high, pivot)

            if pivot == len(nums)-1:
                return nums[-1]
            # found the rotation pivot !
            if nums[pivot] > nums[pivot+1]:
                return nums[pivot+1]

            if nums[pivot] >= nums[0]:
                low = pivot + 1
            else:
                high = pivot

            #print('new', low, high, pivot)
        return nums[pivot]