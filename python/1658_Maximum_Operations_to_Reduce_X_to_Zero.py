

class SolutionTLE:
    def minOperations(self, nums: List[int], x: int) -> int:

        """
            TLE: time limit exceeded
        """
        # queue = deque([(x, left, right, 0)])
        queue = deque()
        queue.append((x, 0, len(nums)-1, 0))

        # BFS traversal
        while queue:
            remain, left, right, steps = queue.popleft()

            if remain == 0:
                return steps
            elif remain < 0:
                continue
            elif left > right:
                continue

            # try leftmost and rightmost
            queue.append((remain - nums[left], left+1, right, steps+1))
            queue.append((remain - nums[right], left, right-1, steps+1))


        return -1


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        total_sum = sum(nums)

        # need all elements
        if total_sum == x:
            return len(nums)

        # otherwise, only need a subarray
        target = total_sum - x

        # find the maximum subarray for the remaining sum
        max_subarray_size = float('-inf')
        left = 0
        window_sum = 0
        for right in range(0, len(nums)):
            window_sum += nums[right]

            while window_sum > target and left < right:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                max_subarray_size = max(max_subarray_size, right - left + 1)


        return len(nums) - max_subarray_size if max_subarray_size != float('-inf') else -1
