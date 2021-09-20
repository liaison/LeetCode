class Solution:
    def trap(self, height: List[int]) -> int:

        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1

        total_sum = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                total_sum += left_max - height[left]
                left += 1
            else:
                total_sum += right_max - height[right]
                right -= 1

        return total_sum
