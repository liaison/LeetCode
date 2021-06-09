class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == 0 and len(goal) == 0:
            return True
        elif len(s) != len(goal):
            return False

        for split_index in range(len(s)):
            shift_str = s[split_index:] + s[0:split_index]
            if shift_str == goal:
                return True

        return False


    def rotateString_ABAB_BA(self, s: str, goal: str) -> bool:
        if len(s) == 0 and len(goal) == 0:
            return True
        elif len(s) != len(goal):
            return False

        return goal in (s+s)

