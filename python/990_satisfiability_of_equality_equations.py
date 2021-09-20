class LetterUnionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        ga = self.find(a)
        gb = self.find(b)
        if ga != gb:
            self.parent[ga] = self.parent[gb]


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        equals, non_equals = [], []
        for equation in equations:
            if equation[1] == "!":
                non_equals.append(equation)
            else:
                equals.append(equation)

        # Group all the equal variables
        luf = LetterUnionFind()
        base = ord('a')
        for equation in equals:
            a, b = equation[0], equation[3]
            if a == b:
                continue
            index_a, index_b = ord(a) - base, ord(b) - base
            luf.union(index_a, index_b)

        # Check the non-equality condition one by one
        for equation in non_equals:
            a, b = equation[0], equation[3]
            if a == b:
                return False

            index_a, index_b = ord(a) - base, ord(b) - base
            pa, pb = luf.find(index_a), luf.find(index_b)
            if pa == pb:
                return False

        return True


