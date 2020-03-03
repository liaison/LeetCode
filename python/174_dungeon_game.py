"""

Dungeon Game

https://leetcode.com/problems/dungeon-game/

"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[sys.maxint for c in range(cols)] for r in range(rows)]
        
        def get_dp(row, col):
            if row >= rows or col >= cols:
                return sys.maxint
            else:
                return dp[row][col]
        
        def get_min_health(currCell, nextCell):
            if nextCell == sys.maxint:
                return sys.maxint
    
            if currCell > 0:
                if currCell >= nextCell:
                    return 1
                else:
                    return (nextCell-currCell)
            else:
                return -currCell + nextCell

        
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                min_health = 1 if dungeon[row][col] >= 0 else (1 - dungeon[row][col])
                
                right_step = get_dp(row, col+1)
                down_step = get_dp(row+1, col)
                
                right_health = get_min_health(dungeon[row][col], right_step)
                down_health = get_min_health(dungeon[row][col], down_step)
                
                next_health = min(right_health, down_health)
                if next_health != sys.maxint:
                    min_health = next_health

                dp[row][col] = min_health
        
        return dp[0][0]

