class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        median_index = len(self.nums) // 2

        if len(self.nums) % 2 == 0:
            return (self.nums[median_index] + self.nums[median_index-1]) / 2
        else:
            return self.nums[median_index]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

import heapq

class MedianFinderHeap:
    """
        Solution with two heaps
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        # push the element through both low and high heap
        heapq.heappush(self.low, - num)
        heapq.heappush(self.high, - self.low[0])
        heapq.heappop(self.low)

        # rebalancing, to ensure len(low) >= len(high)
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, - self.high[0])
            heapq.heappop(self.high)


    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return - self.low[0]
        else:
            return (- self.low[0] + self.high[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
