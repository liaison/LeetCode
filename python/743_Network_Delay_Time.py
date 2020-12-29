class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
            The original Dijkstra algorithm is to find the shorting distances
                between a starting node and each of the rest nodes.
            This problem can be considered as a variant of Dijkstra problem.
        """

        graph = defaultdict(list)
        for entry in times:
            source, target, weight = entry
            graph[source].append((weight, target))

        queue = graph[K]
        heapq.heapify(queue)
        clocks = 0
        visited = [False for i in range(N+1)]
        visited[K] = True
        visit_cnt = 1

        while queue:
            timestamp, target = heapq.heappop(queue)
            clocks = timestamp

            if not visited[target]:
                visit_cnt += 1
                if visit_cnt == N:
                    break
                visited[target] = True
                for next_weight, next_target in graph[target]:
                    heapq.heappush(queue, (clocks+next_weight, next_target))

        return clocks if visit_cnt == N else -1


class SolutionDijkstra:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
            Dijkstra with heap
        """
        graph = defaultdict(list)
        for entry in times:
            source, target, weight = entry
            graph[source].append((weight, target))

        queue = graph[K]
        heapq.heapify(queue)

        min_elapse = {K:0}

        while queue:
            # one of the cases is that there might be several edges between two nodes.
            # the most optimal one would be picked,
            # therefore we should ignore the rest of the edges.
            clocks, target = heapq.heappop(queue)
            if target in min_elapse:
                continue

            min_elapse[target] = clocks
            for next_weight, next_target in graph[target]:

                if next_target not in min_elapse:
                    heapq.heappush(queue, (clocks + next_weight, next_target))

        return max(min_elapse.values()) if len(min_elapse) == N else -1
