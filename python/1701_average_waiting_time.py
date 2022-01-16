class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        prev_end = customers[0][0]

        total_time = 0
        for customer in customers:
            arrival, duration = customer[0], customer[1]

            if prev_end > arrival:
                # delayed by the previous customer
                wait_time = prev_end - arrival + duration
                prev_end = prev_end + duration
            else:
                # the chef is idle and thus serve the customer immediately
                wait_time = duration
                prev_end = arrival + duration

            total_time += wait_time

        return total_time / len(customers)


