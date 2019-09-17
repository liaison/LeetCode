"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.

The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # enable each position as a unique complex number,
        #  to simply the logic of iteration and the switch of direction later 
        boardDict = {}
        for rowIndex, row in enumerate(board):
            for colIndex, cell in enumerate(row):
                boardDict[rowIndex + 1j*colIndex] = cell
        
        def backtrack(currPos, subword):
            
            # bottom case: we find match for each letter in the word
            if len(subword) == 0: 
                return True
            
            # iterate 4 directions
            for k in range(4):
                nextPos = currPos + 1j**k
                # the nextPos is not VALID
                if nextPos not in boardDict:
                    continue
                
                if boardDict[nextPos] == subword[0]:
                    # mark the next position
                    boardDict[nextPos] = '#'
                    if backtrack(nextPos, subword[1:]):
                        return True
                    
                    # restore the original value
                    boardDict[nextPos] = subword[0]
        
            # Tried all directions, and did not find any match
            return False
        
        # the drawback of this approach is that we end up tempering the original board
        #  at the end of the function. But we avoid the use of visited map and gain some time.
        
        # Start from each of the positions in the board,
        #   to kick off the backtracking.
        for pos in boardDict:
            if boardDict[pos] != word[0]:
                continue
            boardDict[pos] = '#'
            if backtrack(pos, word[1:]):
                return True
            boardDict[pos] = word[0]
        
        return False
 


class Solution_2(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # enable each position as a unique complex number,
        #  to simply the logic of iteration and the switch of direction later 
        boardDict = {}
        for rowIndex, row in enumerate(board):
            for colIndex, cell in enumerate(row):
                boardDict[rowIndex + 1j*colIndex] = cell
        
        def backtrack(currPos, subword):        
            # bottom case: we find match for each letter in the word
            if len(subword) == 0: 
                return True
            
            # the currPos is not VALID
            if currPos not in boardDict or boardDict[currPos] != subword[0]:
                return False
    
            boardDict[currPos] = '#'
            # iterate 4 directions
            for k in range(4):
                nextPos = currPos + 1j**k
                if backtrack(nextPos, subword[1:]):
                    return True
        
            boardDict[currPos] = subword[0]
            # Tried all directions, and did not find any match
            return False
        
        # the drawback of this approach is that we end up tempering the original board
        #  at the end of the function. But we avoid the use of visited map and gain some time.
        
        # Start from each of the positions in the board,
        #   to kick off the backtracking.
        for pos in boardDict:
            if backtrack(pos, word):
                return True
        
        return False
        

