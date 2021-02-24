class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        modulo = 10 ** 9 + 7

        @functools.lru_cache(maxsize=None)
        def dp(dice_index, remain):

            if dice_index == d:
                return (remain == 0)
            elif remain < 0:
                return 0

            combs = 0
            for curr_dice in range(1, f+1):
                increment = dp(dice_index+1, remain - curr_dice)
                combs = (combs + increment) % modulo

            return combs

        return dp(0, target)

