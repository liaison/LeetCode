from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        max_prefix_sum = nums[0]
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1] + 1:
                max_prefix_sum += nums[index]
            else:
                break

        num_set = set()
        for num in nums:
            num_set.add(num)

        next_sum = max_prefix_sum
        while True:
            if next_sum not in num_set:
                return next_sum
            else:
                next_sum += 1

