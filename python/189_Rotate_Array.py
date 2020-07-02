class SolutionReverse:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1

    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length

        # reverse the array in three times: first the entire array,
        #  then first and second part respectively
        self.reverse(nums, 0, length-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)
    

class SolutionShift:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            prev = nums[-1]
            # shift the array to the right, once at a time
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]