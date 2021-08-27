class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_queue = []

        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        for task, count in task_count.items():
            task_queue.append((-count, task))

        heapq.heapify(task_queue)

        total_slots = 0

        while task_queue:
            slots_window = n + 1

            # populate one interval of slots
            slot_arrange = []
            while task_queue and slots_window > 0:
                count, task = heapq.heappop(task_queue)
                slot_arrange.append((task, count+1))
                slots_window -= 1
                total_slots += 1

            # need to re-insert the remain tasks
            for task, count in slot_arrange:
                if count != 0:
                    heapq.heappush(task_queue, (count, task))

            if len(task_queue) == 0:
                break

            # padding with idle slots
            total_slots += slots_window

        return total_slots




