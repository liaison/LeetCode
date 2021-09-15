class LetterUnionFind:

    def __init__(self):
        self.parent = [i for i in range(26)]
        self.base = ord('a')

    def find(self, letter):
        lid = ord(letter) - self.base
        if lid != self.parent[lid]:
            parent_letter = chr(self.base + self.parent[lid])
            self.parent[lid] = self.find(parent_letter)
        return self.parent[lid]

    def union(self, la, lb):
        ga = self.find(la)
        gb = self.find(lb)
        if ga != gb:
            # join the group with larger letter to the one with smaller one
            if ga > gb:
                self.parent[ga] = gb
            else:
                self.parent[gb] = ga


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        luf = LetterUnionFind()

        for la, lb in zip(s1, s2):
            luf.union(la, lb)

        ret = []
        base = ord('a')
        for letter in baseStr:
            parent_id = luf.find(letter)
            to_letter = chr(parent_id + base)
            ret.append(to_letter)

        return "".join(ret)



