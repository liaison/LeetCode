class Solution:
    def titleToNumber(self, s: str) -> int:
        
        length = len(s)
        num = 0
        for i in range(0, length):
            num += (ord(s[length-i-1]) - ord('A') + 1) * (26 ** i)

        return num