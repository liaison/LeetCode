
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums.sort()

        # the maximum value for the product of three numbers can only be the following two cases:
        #  -  top 3 numbers
        #  -  top 1 number * bottom 2 numbers
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])
