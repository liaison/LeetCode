class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        range_iter = lower
        num_iter = 0
        ranges = []
        while range_iter < upper and num_iter < len(nums):
            if range_iter < nums[num_iter]:
                if nums[num_iter] - 1 == range_iter:
                    ranges.append(str(range_iter))
                else:
                    ranges.append("{}->{}".format(range_iter, nums[num_iter]-1))
            
            range_iter = nums[num_iter] + 1
            num_iter += 1
        
        if num_iter >= len(nums) and range_iter == upper:
            ranges.append("{}".format(range_iter))
        elif range_iter < upper:
            ranges.append("{}->{}".format(range_iter, upper))

        return ranges