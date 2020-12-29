class Solution:
    def minJumps(self, arr) -> int:

        # value: [indices]
        graph = defaultdict(set)

        for index, value in enumerate(arr):
            graph[value].add(index)

        queue = deque([0])
        visited = [False for i in range(len(arr))]
        target = len(arr) - 1
        steps = 0

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                curr = queue.popleft()

                if curr == target:
                    return steps
                visited[curr] = True

                for neighbor in graph[arr[curr]]:
                    if not visited[neighbor]:
                        queue.append(neighbor)

                graph[arr[curr]].clear()

                for neighbor in [curr-1, curr+1]:
                    if 0 <= neighbor <= target and not visited[neighbor]:
                        queue.append(neighbor)

            steps += 1

        return steps



class SolutionBidirectionalBFS:
    def minJumps(self, arr) -> int:

        # value: [indices]
        graph = defaultdict(set)

        for index, value in enumerate(arr):
            graph[value].add(index)


        visited = [False for i in range(len(arr))]
        target = len(arr) - 1

        head_queue = set([0])
        tail_queue = set([target])
        steps = 0

        # bidirectional BFS
        # alternating the queue in the forward and backward directions
        # pick the queue with less elements to advance
        while head_queue:
            if len(tail_queue) < len(head_queue):
                head_queue, tail_queue = tail_queue, head_queue

            next_queue = set()
            while head_queue:
                curr = head_queue.pop()

                if curr in tail_queue:
                    return steps
                visited[curr] = True

                for neighbor in graph[arr[curr]]:
                    if not visited[neighbor]:
                        next_queue.add(neighbor)

                graph[arr[curr]].clear()

                for neighbor in [curr-1, curr+1]:
                    if 0 <= neighbor <= target and not visited[neighbor]:
                        next_queue.add(neighbor)

            head_queue = next_queue
            steps += 1

        return steps

