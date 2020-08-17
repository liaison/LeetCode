class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefix_sum_index = {}
        prefix_sum = 0
        max_size = 0
        
        for index, num in enumerate(nums):
            
            prefix_sum += num
            
            if prefix_sum not in prefix_sum_index:
                prefix_sum_index[prefix_sum] = index
            
            if prefix_sum == k:
                max_size = max(max_size, index+1)
            
            prev_sum = prefix_sum - k
            if prev_sum in prefix_sum_index:
                max_size = max(max_size, index - prefix_sum_index[prev_sum])
        
        return max_size