class LogSystem:

    def __init__(self):
        self.logs = SortedList()

    def put(self, id: int, timestamp: str) -> None:
        self.logs.add((timestamp, id))


    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:

        match granularity:
            case "Year":
                start_timestamp = "{}:00:00:00:00:00".format(start[:4])
                end_timestamp = "{}:12:31:23:59:59".format(end[:4])
            case "Month":
                start_timestamp = "{}:00:00:00:00".format(start[:7])
                end_timestamp = "{}:31:23:59:59".format(end[:7])
            case "Day":
                start_timestamp = "{}:00:00:00".format(start[:10])
                end_timestamp = "{}:23:59:59".format(end[:10])
            case "Hour":
                start_timestamp = "{}:00:00".format(start[:13])
                end_timestamp = "{}:59:59".format(end[:13])
            case "Minute":
                start_timestamp = "{}:00".format(start[:16])
                end_timestamp = "{}:59".format(end[:16])
            case "Second":
                start_timestamp = start
                end_timestamp = end

        start_index = self.logs.bisect_left((start_timestamp, 0))
        end_index = self.logs.bisect_right((end_timestamp, 1000))

        return [log_id for timestamp, log_id in self.logs[start_index:end_index]]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)