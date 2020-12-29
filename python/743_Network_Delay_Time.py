class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

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

