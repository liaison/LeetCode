

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        # Greedy algorithm
        #   load the boxes prioritized on the their capacities
        boxTypes.sort(key=lambda x:x[1], reverse=True)

        unit_sum = 0
        for box_num, box_units in boxTypes:
            if truckSize == 0:
                break

            if truckSize > box_num:
                truckSize -= box_num
                unit_sum += box_num * box_units
            else:
                unit_sum += truckSize * box_units
                truckSize = 0

        return unit_sum
