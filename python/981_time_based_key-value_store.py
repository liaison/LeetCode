class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value_dict = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        value_list = []
        if key in self.value_dict:
            value_list = self.value_dict[key]

        to_insert = self.binary_search(value_list, timestamp)
        value_list.insert(to_insert, (value, timestamp))
        self.value_dict[key] = value_list


    def binary_search(self, values, timestamp):
        low, high = 0, len(values)
        while low < high:
            mid = (low + high) // 2
            if values[mid][1] < timestamp:
                low = mid + 1
            else:
                high = mid
        return low


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.value_dict:
            return ""

        values = self.value_dict[key]

        low = self.binary_search(values, timestamp)

        # beyond the current list
        if low >= len(values):
            return values[low-1][0]

        # within the current list
        if values[low][1] > timestamp:
            if low >= 1:
                return values[low-1][0]
            else:
                return ""
        else:
            return values[low][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

