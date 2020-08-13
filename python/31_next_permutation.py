class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(array, i, j):
            array[i], array[j] = array[j], array[i]
        
        def reverse(array, start):
            """ reverse the postfix subarray starting from 'start' """
            end = len(array) - 1
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
        
        # locate the pair of elements to switch
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while j > 0:
                if nums[j] > nums[i]:
                    break
                j -= 1
            
            swap(nums, i, j)
        
        # reverse the postfix in order to obtain the minimal permutation
        reverse(nums, i+1)
