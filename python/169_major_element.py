class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ Boyer-Moore voting algorithm"""
        candidate, count = 0, 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            count += (1 if num == candidate else -1)
    
        return candidate