class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        iterate_num = nums[0]
        missing_count = 0
        for index in range(len(nums)-1):
            iterate_num = nums[index]

            while iterate_num < nums[index+1]:
                if missing_count == k:
                    return iterate_num
                iterate_num += 1
                missing_count += 1

            missing_count -= 1

        return iterate_num + (k - missing_count)