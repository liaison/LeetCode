class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:  return 0
        
        window_product = 1
        left, count = 0, 0
        
        for right, val in enumerate(nums):
            
            window_product *= val
            
            while window_product >= k:
                window_product //= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
