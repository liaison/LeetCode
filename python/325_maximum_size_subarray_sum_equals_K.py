class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        max_subarray = 0
        prefix_sum_index = {}
        prefix_sum = 0

        for index in range(0, len(nums)):

            prefix_sum += nums[index]

            if prefix_sum == k:
                # use only the prefix
                max_subarray = max(max_subarray, index + 1)

            if prefix_sum not in prefix_sum_index:
                prefix_sum_index[prefix_sum] = index

            target = prefix_sum - k
            if target in prefix_sum_index:
                prev_index = prefix_sum_index[target]
                max_subarray = max(max_subarray, index - prev_index)

        return max_subarray


