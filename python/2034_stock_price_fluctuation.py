class StockPrice:
    """
        Lazy removal: keep all the outdated entries in the heap
        remove the outdated entries on the go

    """
    def __init__(self):
        import heapq
        self._price_dict = dict()
        self._max_price_heap = []
        self._min_price_heap = []
        self._latest_ts = float("-inf")

    def update(self, timestamp: int, price: int) -> None:

        # update the historical price or add new price
        self._price_dict[timestamp] = price

        self._latest_ts = max(timestamp, self._latest_ts)

        # add new entries to the price heaps
        # Note: some entries might become outdated, but we'll remove them later.
        heapq.heappush(self._max_price_heap, (-price, timestamp))
        heapq.heappush(self._min_price_heap, (price, timestamp))


    def current(self) -> int:
        return self._price_dict[self._latest_ts]


    def maximum(self) -> int:
        curr_price, timestamp = heapq.heappop(self._max_price_heap)

        while - curr_price != self._price_dict[timestamp]:
            # remove the outdated entries
            curr_price, timestamp = heapq.heappop(self._max_price_heap)

        # keep the first up-to-date entry
        heapq.heappush(self._max_price_heap, (curr_price, timestamp))

        return - curr_price


    def minimum(self) -> int:
        curr_price, timestamp = heapq.heappop(self._min_price_heap)

        while curr_price != self._price_dict[timestamp]:
            # remove the outdated entries
            curr_price, timestamp = heapq.heappop(self._min_price_heap)

        # keep the first up-to-date entry
        heapq.heappush(self._min_price_heap, (curr_price, timestamp))

        return curr_price

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()