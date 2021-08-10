class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

        bit_states = minutesToTest / minutesToDie + 1

        # a mathematical solution
        # information contained in buckets: log(buckets)
        # information contained for a single pig (possible states): log(states)
        #return math.ceil(math.log(buckets) / math.log(bit_states))

        num_bits = 0  # number of pigs as well
        while bit_states ** num_bits < buckets:
            num_bits += 1

        return num_bits

