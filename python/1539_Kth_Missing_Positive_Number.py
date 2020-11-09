class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        prev = 0
        missing_cnt = 0
        
        for curr in arr:
            
            # case 1). we find the missing number in between the array
            while prev < curr - 1:
                prev += 1
                missing_cnt += 1
                if missing_cnt == k:
                    return prev
            
            prev = curr
        
        # case 2). we find the missing number beyond the array
        return curr + (k - missing_cnt)
