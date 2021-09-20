
class SolutionTLE:
    def maxArea(self, height: List[int]) -> int:

        length = len(height)

        max_size = float('-inf')
        for start in range(length):
            for end in range(start+1, length):
                new_size = min(height[start], height[end]) * (end - start)
                max_size = max(max_size, new_size)

        return max_size
