class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
            bucket sort alike algorithm
        """
        buckets = {}
        window = (t+1)
        
        if t < 0:
            return False
        
        def locate(num):
            return num // window
        
        for index, num in enumerate(nums):
            bucket_id = locate(num)
         
            left = bucket_id - 1
            right = bucket_id + 1
            
            # check [left_bucket][current_bucket][right_bucket]
            if bucket_id in buckets:
                return True
            if left in buckets and abs(num - buckets[left]) < window:
                return True
            if right in buckets and abs(buckets[right] - num) < window:
                return True
            
            buckets[bucket_id] = num
            
            if len(buckets) > k:
                buckets.pop(locate(nums[index-k]))
                
        return False