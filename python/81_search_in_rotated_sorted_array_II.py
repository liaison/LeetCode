class Solution:
    
    def search(self, nums: List[int], target: int) -> bool:

        def binary_search(low, high, nums, target):
            if low > high:
                return False

            pivot = int((low+high)/2)
            if nums[pivot] == target:
                return True

            is_same_side = (nums[pivot] < nums[0]) == (target < nums[0])

            if is_same_side:
                comparator = nums[pivot]
            else:
                # using the nums[0] as the pivot
                comparator = float('-inf') if target < nums[0] else float('inf')

            if target < comparator:
                high = pivot - 1
            else:
                low = pivot + 1        
            return binary_search(low, high, nums, target)

        # avoid the case when the head and the tail are duplicates
        high = len(nums)-1
        while high > 0:
            if nums[high] != nums[0]:
                break
            high -= 1

        return binary_search(0, high, nums, target)
