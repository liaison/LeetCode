class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(maxsize=None)
        def dfs(remain):
            sqrt_root = int(sqrt(remain))
            # current player will win immediately by taking the square number tiles
            if sqrt_root ** 2 == remain:
                return True
            
            for i in range(1, sqrt_root+1):
                # if there is any chance to make the opponent lose the game in the next round,
                #  then the current player will win.
                if not dfs(remain - i*i):
                    return True
    
            return False
    
        return dfs(n)
