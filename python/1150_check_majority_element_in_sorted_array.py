class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        # locate the target with the binary search
        low, high = 0, len(nums)
        while low < high:
            mid = (high - low) // 2 + low
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                break
        
        if nums[mid] != target:
            return False
        
        # search around the located target for duplicate elements
        count = 1
        low, high = mid - 1, mid + 1
        while low >= 0:
            if nums[low] != target:
                break
            low -= 1
            count += 1
        
        while high < len(nums):
            if nums[high] != target:
                break
            high += 1
            count += 1
        
        return count > len(nums) / 2
                
        