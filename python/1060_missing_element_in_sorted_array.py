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


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        for i in range(1, len(nums)):
            # calculate the gaps between two adjacent numbers
            gaps = nums[i] - nums[i-1] - 1

            # find the gap
            if gaps >= k:
                return nums[i-1] + k

            # reduce the expected target
            k -= gaps

        # the target beyond the array
        return nums[-1] + k


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        # the global index of missing numbers, for each position
        def missing_so_far(index):
            return nums[index] - nums[0] - index

        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2

            if missing_so_far(mid) < k:
                low = mid + 1
            else:
                high = mid

        return k - missing_so_far(low-1) + nums[low-1]


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        def missing_so_far(index):
            return nums[index] - nums[0] - index

        # equivalent to the previous implementation
        # in order to apply bisect, we have to instantialize each index, therefore O(N)
        gap_index = [missing_so_far(index) for index in range(len(nums))]

        low = bisect.bisect_left(gap_index, k)

        return k - missing_so_far(low-1) + nums[low-1]
