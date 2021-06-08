

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


    def minCostToSupplyWater_Prim(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        # bidirectional graph represented in adjacency list
        graph = defaultdict(list)

        # add a virtual vectex indexed with 0.
        #   then add an edge to each of the house weighted by the cost
        for index, weight in enumerate(wells):
            graph[0].append((weight, index+1))

        # add the bidirectional edges to the graph
        for house_1, house_2, weight in pipes:
            graph[house_1].append((weight, house_2))
            graph[house_2].append((weight, house_1))

        # A set to maintain all the vertex that has been added to
        #   the final MST (Minimal Spanning Tree),
        #   starting from the vertex 0.
        mst_set = set([0])

        # heap to maitain the order of edges to be visited,
        #   starting from the edges originated from the vertex 0.
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        total_cost = 0
        while len(mst_set) < n+1:
            weight, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                # adding the new vertex into the set
                mst_set.add(next_house)
                total_cost += weight
                # expanding the candidates of edge to choose from
                #   in the next round
                for weight, house in graph[next_house]:
                    if house not in mst_set:
                        heapq.heappush(edges_heap, (weight, house))

        return total_cost




















