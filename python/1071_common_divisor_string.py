class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def isDivisor(prefix, fullstr):
            if len(prefix) > len(fullstr):
                return False
            elif len(fullstr) % len(prefix) != 0:
                return False

            fold = int(len(fullstr) / len(prefix))
            return (prefix * fold) == fullstr

        length = len(str1)
        for index in range(length, 0, -1):
            prefix = str1[:index]
            if isDivisor(prefix, str1) and isDivisor(prefix, str2):
                return prefix

        return ""
