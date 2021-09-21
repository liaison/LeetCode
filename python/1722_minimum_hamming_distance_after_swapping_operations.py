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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        str_len = len(source)

        uf = UnionFind(str_len)
        for a, b in allowedSwaps:
            uf.union(a, b)

        group_index = defaultdict(list)
        for index in range(str_len):
            group_id = uf.find(index)
            group_index[group_id].append(index)

        hamming_distance = 0
        for group_id, group_index in group_index.items():
            source_counter = Counter([source[i] for i in group_index])
            target_counter = Counter([target[i] for i in group_index])
            common_elements = source_counter & target_counter
            hamming_distance += len(group_index) - sum(common_elements.values())

        return hamming_distance


