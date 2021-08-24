
class UnionFind:

    def __init__(self, size):
        self.group = [group_id for group_id in range(size)]
        self.rank = [0] * size

    def find(self, person):
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, a, b):
        group_a = self.find(a)
        group_b = self.find(b)
        is_merged = False
        if group_a == group_b:
            return is_merged

        is_merged = True
        # merge the two groups with rank to balance
        #  join the group with lower rank to the one with higher rank
        if self.rank[group_a] > self.rank[group_b]:
            self.group[group_b] = group_a
        elif self.rank[group_a] < self.rank[group_b]:
            self.group[group_a] = group_b
        else:
            self.group[group_a] = group_b
            self.rank[group_b] += 1

        # whether the two persons belong to the same group
        return is_merged


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        logs.sort(key = lambda x: x[0])

        uf = UnionFind(n)

        group_cnt = n
        for timestamp, friend_a, friend_b in logs:
            if uf.union(friend_a, friend_b):
                group_cnt -= 1

            if group_cnt == 1:
                # early exit
                return timestamp

        # there are still more than one groups/circles of friends
        return -1



