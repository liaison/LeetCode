class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots_map = {}
        self.slots_map[1] = big
        self.slots_map[2] = medium
        self.slots_map[3] = small


    def addCar(self, carType: int) -> bool:

        if self.slots_map[carType] > 0:
            self.slots_map[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)