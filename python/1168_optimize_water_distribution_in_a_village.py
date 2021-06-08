

class UnionFind:
    """
        Minimalist implementation of UnionFind without load-balancing.
    """
    def __init__(self, size):
        """
        container to hold parent for each member
        Note: the index of member starts from 1,
            thus we add one element to the container.
        """
        self.parent = [i for i in range(size+1)]

    def find(self, member_id):
        if self.parent[member_id] != member_id:
            self.parent[member_id] = self.find(self.parent[member_id])
        return self.parent[member_id]

    def union(self, person_1, person_2):
        parent_1 = self.find(person_1)
        parent_2 = self.find(person_2)
        if parent_1 != parent_2:
            self.parent[parent_2] = parent_1
            return True
        else:
            return False


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        edges_heap = []
        for index, weight in enumerate(wells):
            heapq.heappush(edges_heap, (weight, n+1, index+1))

        for house_1, house_2, weight in pipes:
            heapq.heappush(edges_heap, (weight, house_1, house_2))

        uf = UnionFind(n+1)
        total_cost = 0
        for _ in range(n+len(pipes)):
            weight, house_1, house_2 = heapq.heappop(edges_heap)

            if uf.union(house_1, house_2):
                total_cost += weight

        return total_cost


    def minCostToSupplyWater_Sort(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
            The sorting solution is two times faster than the heap solution.
        """
        ordered_edges = []

        for index, weight in enumerate(wells):
            ordered_edges.append((weight, n+1, index+1))

        for house_1, house_2, weight in pipes:
            ordered_edges.append((weight, house_1, house_2))

        # sort the edges by its weight
        ordered_edges.sort(key=lambda x: x[0])

        uf = UnionFind(n+1)
        total_cost = 0
        for weight, house_1, house_2 in ordered_edges:

            if uf.union(house_1, house_2):
                total_cost += weight


        return total_cost










