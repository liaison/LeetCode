
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
            Similar problem as finding the intersection between two sorted list
        """
        jobs = [(d, p) for (d, p) in zip(difficulty, profit)]
        jobs.sort(key = lambda x: x[0])

        worker.sort()
        job_p, worker_p = 0, 0

        max_profit = 0
        total_profit = 0

        while worker_p < len(worker):

            # move the job pointer to find the most profitable job based on the current difficulty
            while job_p < len(jobs) and jobs[job_p][0] <= worker[worker_p]:
                max_profit = max(max_profit, jobs[job_p][1])
                job_p += 1

            # either we take a new job, or the previously most profitable job
            total_profit += max_profit
            worker_p += 1

        return total_profit