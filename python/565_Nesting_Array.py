class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
                
        max_length = -1
        visited = [False] * len(nums)
        
        for i in range(0, len(nums)):
            if visited[i]:
                continue
            start, count = nums[i], 0
            visited[i] = True
            # form the cycle
            while True:
                start = nums[start]
                visited[start] = True
                count += 1
                if start == nums[i]:
                    break
            
            max_length = max(max_length, count)
        
        return max_length