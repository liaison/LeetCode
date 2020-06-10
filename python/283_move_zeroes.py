class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read_index, write_index = 0, -1
        len_nums = len(nums)

        # shift non-zero numbers to the head of the list
        while read_index < len_nums:
            if nums[read_index] != 0:
                write_index += 1
                nums[write_index] = nums[read_index]
            read_index += 1

        # reset the rest of numbers to zeroes
        write_index += 1
        while write_index < len_nums:
            nums[write_index] = 0
            write_index += 1
