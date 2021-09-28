
class SolutionTLE:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        """
            Greedy strategy to assign the works week by week
        """
        prev_project = -1
        steps = 0

        project_queue = []
        for project, milestone in enumerate(milestones):
            project_queue.append((-milestone, project))

        heapq.heapify(project_queue)

        while project_queue:

            next_projects = []

            window = 2
            while project_queue and window:
                curr_milestone, curr_project = heapq.heappop(project_queue)
                if curr_milestone < -1:
                    next_projects.append((curr_milestone+1, curr_project))

                window -= 1
                steps += 1

            if window > 0:
                break

            for milestone, project in next_projects:
                heapq.heappush(project_queue, (milestone, project))

        return steps

