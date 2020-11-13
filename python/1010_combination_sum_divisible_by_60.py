class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        count = 0

        modulo_table = defaultdict(int)

        for num in time:
            modulo_table[num % 60] += 1

        for factor in [0, 30]:
            if factor in modulo_table:
                count += int(modulo_table[factor] * (modulo_table[factor]-1) / 2)

        for factor in range(1, 30):
            if factor in modulo_table:
                count += modulo_table[factor] * modulo_table[60 - factor]

        return count
