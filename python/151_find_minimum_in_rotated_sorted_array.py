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