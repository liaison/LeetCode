class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        return num > 0 and math.log2(num) % 2 == 0
        # num & (num - 1) == 0  // power of two
        # num & 0xaaaaaaaa == 0 // odd number of power of twos
        #return num > 0 and num & (num-1) == 0 and (num & 0xaaaaaaaa) == 0
