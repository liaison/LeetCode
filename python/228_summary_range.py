class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        def format_range(low, high):
            return str(low) if low == high else "{}->{}".format(low, high)
        
        results = []
        
        if len(nums) == 0:
            return results
        
        low = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                results.append(format_range(low, nums[i-1]))
                low = nums[i]
        
        results.append(format_range(low, nums[-1]))
        
        return results