class SeatManager:

    def __init__(self, n: int):
        self.seats = [i+1 for i in range(n)]
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        min_seat = heapq.heappop(self.seats)
        return min_seat


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)