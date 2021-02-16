class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def possible(capacity):
            ship_weight = 0
            ship_count = 1
            for weight in weights:
                if weight > capacity:
                    return False
                elif ship_weight + weight <= capacity:
                    ship_weight += weight
                elif ship_count > D:
                    return False
                else:
                    # add a new ship
                    ship_count += 1
                    ship_weight = weight
            return (ship_count <= D)


        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            is_ok = possible(mid)
            if is_ok:
                high = mid
            else:
                low = mid + 1

        return low