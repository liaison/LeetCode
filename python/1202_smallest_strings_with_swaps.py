class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        uf = UnionFind(len(s))

        for a, b in pairs:
            uf.union(a, b)

        letter_groups = defaultdict(list)
        for index in range(len(s)):
            parent_id = uf.find(index)
            letter_groups[parent_id].append(index)

        output = [''] * len(s)
        for parent_id, group_index in letter_groups.items():
            letters = [s[index] for index in group_index]
            letters.sort()
            for li, index in enumerate(group_index):
                output[index] = letters[li]

        return "".join(output)

