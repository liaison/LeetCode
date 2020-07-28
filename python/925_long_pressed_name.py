class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        # two pointers to the "name" and "typed" string respectively
        np, tp = 0, 0
        
        # advance two pointers, until we exhaust one of the strings
        while np < len(name) and tp < len(typed):
            if name[np] == typed[tp]:
                np += 1
                tp += 1
            elif tp >= 1 and typed[tp] == typed[tp-1]:
                tp += 1
            else:
                return False
        
        # if there is still some characters left *unmatched* in the origin string,
        #   then we don't have a match.
        # e.g.  name = "abc"  typed = "aabb"
        if np != len(name):
            return False
        else:
            # In the case that there are some redundant characters left in typed
            # we could still have a match.
            # e.g.  name = "abc"  typed = "abccccc"
            while tp < len(typed):
                if typed[tp] != typed[tp-1]:
                    return False
                tp += 1
        
        return True