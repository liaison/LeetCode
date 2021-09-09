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


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_count = 0
        prefix_sum = 0
        prefix_sum_table = defaultdict(int)
        for index, num in enumerate(nums):
            prefix_sum += num

            # case 1). the prefix is the subarray
            if prefix_sum == k:
                total_count += 1

            # case 2). the differece between two prefixes
            delta = prefix_sum - k
            if delta in prefix_sum_table:
                total_count += prefix_sum_table[delta]

            prefix_sum_table[prefix_sum] += 1

        return total_count

