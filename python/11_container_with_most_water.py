
class SolutionTLE:
    def maxArea(self, height: List[int]) -> int:

        length = len(height)

        max_size = float('-inf')
        for start in range(length):
            for end in range(start+1, length):
                new_size = min(height[start], height[end]) * (end - start)
                max_size = max(max_size, new_size)

        return max_size


class SolutionTwoPointer:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_size = float('-inf')
        while left < right:
            new_size = min(height[left], height[right]) * (right - left)
            max_size = max(max_size, new_size)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_size