class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        clock = 0
        while tickets[k]:

            for index, ticket in enumerate(tickets):
                if ticket > 0:
                    tickets[index] -= 1
                    clock += 1

                # stop the clock as soon as the target reaches zero
                if tickets[k] == 0:
                    return clock

        return clock