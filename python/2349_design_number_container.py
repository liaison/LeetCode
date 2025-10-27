from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.index_to_num_map = {}
        self.num_to_index_map = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index not in self.index_to_num_map:
            self.index_to_num_map[index] = number
            self.num_to_index_map[number].add(index)
        else:
            # replace existing number
            prev_num = self.index_to_num_map[index]
            self.index_to_num_map[index] = number
            # remove the previous number
            self.num_to_index_map[prev_num].remove(index)
            if len(self.num_to_index_map[prev_num]) == 0:
                del self.num_to_index_map[prev_num]

            # add new number
            self.num_to_index_map[number].add(index)

    def find(self, number: int) -> int:
        if number in self.num_to_index_map:
            return self.num_to_index_map[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)