
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bitmask = 1
        result, remain = n, n

        # exception
        if n == 0:
            return 1

        while remain:
            result = result ^ bitmask

            bitmask = bitmask << 1
            remain = remain >> 1

        return result