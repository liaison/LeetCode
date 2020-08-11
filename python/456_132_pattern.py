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