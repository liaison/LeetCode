
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


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        """
        https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375390/Python-Solution-with-detailed-explanation-and-proof-and-common-failure-analysis
        """
        milestone_sum, max_milestone = sum(milestones), max(milestones)

        if milestone_sum >= 2 * max_milestone:
            return milestone_sum
        else:
            return 2 * (milestone_sum - max_milestone) + 1
