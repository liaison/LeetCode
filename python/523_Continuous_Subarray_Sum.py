class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
        # the earliest index with the same module remaider of k
        prefix_sum_indices = {}
        
        # a virtual prefix sum index.
        # for the test case of [0, 0]  k = 0
        prefix_sum = 0
        prefix_sum_indices[0] = -1
        
        for index, num in enumerate(nums):
            
            prefix_sum += num

            # group the prefix sums with modulo
            if k != 0:
                prefix_sum %= k # normalize the sum
            
            if prefix_sum in prefix_sum_indices:
                if index - prefix_sum_indices[prefix_sum] > 1:
                    return True
            else:
                prefix_sum_indices[prefix_sum] = index
        
        return False
