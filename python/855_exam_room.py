class ExamRoom:

    def __init__(self, n: int):
        self.total_seats = n
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0

        new_seat = 0 # sitting at the door
        max_distance = self.seats[0] # distance between the first and the door
        # iterate through all existing intervals
        for index in range(1, len(self.seats)):
            prev, curr = self.seats[index-1], self.seats[index]

            # place the seat in the middle of the interval
            distance = (curr - prev) // 2
            if distance > max_distance:
                max_distance = distance
                new_seat = (curr + prev) // 2

        # check the last seat
        if self.total_seats - 1 - self.seats[-1] > max_distance:
            new_seat = self.total_seats - 1

        # insert the new seat into the list in order
        insort(self.seats, new_seat)

        return new_seat


    def leave(self, p: int) -> None:
        self.seats.remove(p)



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)