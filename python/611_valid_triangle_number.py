class Solution:
    """
        Time limit exceeded
    """
    def triangleNumber(self, nums: List[int]) -> int:

        triangle_cnt = 0
        nums.sort()

        def backtrack(start, comb):
            nonlocal triangle_cnt
            if len(comb) == 3:
                if comb[0] + comb[1] > comb[2] and comb[2] - comb[1] < comb[0]:
                    triangle_cnt += 1
                return

            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(0, [])

        return triangle_cnt
