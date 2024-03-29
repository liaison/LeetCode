class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) > len(t):
            long, short = s, t
        else:
            long, short = t, s

        NP, NS = len(long), len(short)

        is_edited = False
        p_long, p_short = 0, 0
        while p_long < NP or p_short < NS:

            if p_long < NP and p_short < NS and long[p_long] == short[p_short]:
                p_long += 1
                p_short += 1
            else:
                if is_edited:
                    return False

                if NP == NS:
                    p_long += 1
                    p_short += 1
                else: # len(long) > len(short)
                    p_long += 1

                is_edited = True

        return is_edited


class Solution:
    def isOneEditDistanceRefinedTwoPointers(self, s: str, t: str) -> bool:

        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        ps, pt = 0, 0
        NS, NT = len(s), len(t)
        is_edited = False

        while ps < NS and pt < NT:

            if s[ps] != t[pt]:
                if is_edited:
                    return False

                if NS > NT:
                    pt -= 1
                elif NS < NT:
                    ps -= 1

                is_edited = True

            ps += 1
            pt += 1

        return True


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) > len(t):
            long, short = s, t
        else:
            long, short = t, s

        NP, NS = len(long), len(short)

        for index in range(NS):
            if long[index] != short[index]:
                if NP == NS:
                    return long[index+1:] == short[index+1:]
                else: # NP > NS
                    return long[index+1:] == short[index:]

        return NP == NS + 1

