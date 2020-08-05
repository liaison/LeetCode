class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sums_count = defaultdict(int)
        acc_sum = 0
        count = 0
        
        for index, num in enumerate(nums):
            acc_sum += num
            
            # case 1: subarray from the begining
            if acc_sum == k:
                count += 1
            
            # case 2: subarray starts somewhere in the middle
            count += prefix_sums_count[acc_sum-k]
            
            # keep the account for the appearance of prefix sum
            prefix_sums_count[acc_sum] += 1
        
        return count
