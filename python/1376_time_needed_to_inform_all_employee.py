
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        subordinates = dict()
        for employee_id, manager_id in enumerate(manager):
            if manager_id not in subordinates:
                subordinates[manager_id] = []

            if manager_id == -1:
                # pseudo head
                subordinates[manager_id].append((employee_id, 0))
            else:
                subordinates[manager_id].append((employee_id, informTime[manager_id]))


        max_time = float('-inf')
        def dfs(curr, time_elapse):
            nonlocal max_time

            if curr not in subordinates:
                # bottom
                max_time = max(max_time, time_elapse)
                return

            for employee_id, added_time in subordinates[curr]:
                dfs(employee_id, added_time + time_elapse)

        dfs(-1, 0)

        return max_time

