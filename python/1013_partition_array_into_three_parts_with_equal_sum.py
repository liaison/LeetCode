
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        total_sum = sum(arr)

        if total_sum % 3 != 0:
            return False

        subarray_sum = total_sum / 3
        group_sum, group_count = 0, 0

        for num in arr:
            group_sum += num
            if group_sum == subarray_sum:
                group_count += 1
                group_sum = 0

        return group_count >= 3
