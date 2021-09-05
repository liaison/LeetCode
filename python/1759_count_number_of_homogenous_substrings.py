
class Solution:
    def countHomogenous(self, s: str) -> int:

        modulo = 10 ** 9 + 7

        total_substr = 0
        substr_len = 1
        prev = s[0]

        for curr in s[1:]:
            if curr == prev:
                substr_len += 1
            else:
                # calculate each part of the consecutive substring
                total_substr += (1 + substr_len) * substr_len // 2
                # reset
                prev = curr
                substr_len = 1

        # the last part of the homogenous substring
        total_substr += (1 + substr_len) * substr_len // 2

        return total_substr % modulo