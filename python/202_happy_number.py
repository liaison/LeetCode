class Solution:
    def isHappy(self, n: int) -> bool:

        def nextHappyNumber(num):
            ret = 0
            while num > 0:
                digit = num % 10
                num = num // 10
                ret += digit * digit
            return ret

        num_set = set()
        next_n = n
        num_set.add(next_n)
        while True:
            if next_n == 1:
                return True

            next_n = nextHappyNumber(next_n)

            if next_n in num_set:
                return False

            num_set.add(next_n)


solution = Solution()

assert solution.isHappy(7)


