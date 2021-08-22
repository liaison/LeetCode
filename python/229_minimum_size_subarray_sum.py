
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # build the prefix sums first
        prefix_sums = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefix_sums.append(prefix_sum)

        min_size = float('inf')

        # edge cases
        if prefix_sums[-1] < target:
            return 0
        elif prefix_sums[-1] == target:
            return len(nums)

        for index, prefix_sum in enumerate(prefix_sums):

            next_sum = prefix_sum + target
            next_index = bisect.bisect_left(prefix_sums, next_sum, index)

            # check the difference of two prefixes
            if next_index != len(prefix_sums):
                min_size = min(min_size, next_index - index)

            # check the substring of prefixes
            if prefix_sum >= target:
                min_size = min(min_size, index + 1)

        return min_size if min_size != float('inf') else 0


class SolutionSlidingWindow:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_size = float('inf')

        left, right = 0, 0
        window_sum = 0

        # fixing on the right pointer
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_size = min(min_size, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_size if min_size != float('inf') else 0
