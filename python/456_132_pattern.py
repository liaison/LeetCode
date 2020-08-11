class SolutionTLE:
    def find132pattern(self, nums: List[int]) -> bool:
        
        # even with the deduplication process, 
        #   still the solution runs into TLE.
        dedup_nums = []
        prev = None
        # deduplication
        for num in nums:
            if prev is None or prev != num:
                prev = num
                dedup_nums.append(num)
        
        small = float('inf')
        
        for j in range(0, len(dedup_nums)):
            small = min(small, dedup_nums[j])
            
            for k in range(j+1, len(dedup_nums)):
                if small < dedup_nums[k] and dedup_nums[k] < dedup_nums[j]:
                    return True
        
        return False

    
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        small_index = 0
        # build the rising slopes on-the-go
        #   and check if the number falls into any of the rising slopes.
        rising_slopes = []
        
        for i in range(1, len(nums)):
            
            if nums[i] < nums[i-1]:
                if small_index < i - 1:
                    rising_slopes.append((small_index, i-1))
                
                small_index = i
            
            for (li, hi) in rising_slopes:
                if nums[li] < nums[i] < nums[hi]:
                    return True
        
        return False
        