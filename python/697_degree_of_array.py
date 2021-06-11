class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        num_range_dict = {}
        max_count = 0

        for index, num in enumerate(nums):
            if num in num_range_dict:
                start, end, count = num_range_dict[num]
                new_count = count + 1
                num_range_dict[num] = (start, index, new_count)
            else:
                new_count = 1
                num_range_dict[num] = (index, index, new_count)

            if new_count > max_count:
                max_count = new_count

        min_range = float("inf")
        for _, value in num_range_dict.items():
            start, end, count = value
            if count == max_count:
                min_range = min(min_range, end-start+1)

        return min_range


