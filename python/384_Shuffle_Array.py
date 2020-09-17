class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.perm = list(self.original)
    
    
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        # restore the current state of permutation to its original state
        self.perm = list(self.original)
        return self.perm
           

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # apparently this is so-call Fisher-Yates algorithm.
        for i in range(len(self.perm)):
            #randi = random.randrange(i, len(self.perm))
            randi = i + random.randint(0, len(self.perm)-i-1)
            self.perm[i], self.perm[randi] = self.perm[randi], self.perm[i]
            
        return self.perm


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()