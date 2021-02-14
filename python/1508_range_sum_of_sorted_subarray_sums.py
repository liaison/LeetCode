class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        subarray_sums = []
        modulo = 10 ** 9 + 7

        for start_index, start_num in enumerate(nums):
            subarray_sum = 0
            for end_index, end_num in enumerate(nums[start_index:]):
                subarray_sum += end_num
                subarray_sums.append(subarray_sum)

        subarray_sums.sort()

        ret = 0
        for index in range(left-1, right):
            ret = (ret + subarray_sums[index]) % modulo

        return ret
