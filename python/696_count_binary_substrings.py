class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        # count the groups of identical bits
        # e.g. [1110011] -> [3, 2, 2]
        groups = [1]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for gi in range(1, len(groups)):
            ans += min(groups[gi], groups[gi-1])

        return ans
