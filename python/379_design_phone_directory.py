import random

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.assigned_numbers = set()
        self.number_counter = 0
        self.limit = maxNumbers

    def get(self) -> int:
        if self.number_counter == self.limit:
            return -1

        while True:
            new_number = random.randrange(0, self.limit)
            if new_number not in self.assigned_numbers:
                self.assigned_numbers.add(new_number)
                self.number_counter += 1
                return new_number


    def check(self, number: int) -> bool:
        return number not in self.assigned_numbers


    def release(self, number: int) -> None:
        if number in self.assigned_numbers:
            self.number_counter -= 1
            self.assigned_numbers.remove(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)