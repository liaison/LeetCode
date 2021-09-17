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


class Solution_3(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret


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


class SolutionBacktrack:
    def exist(self, board: List[List[str]], word: str) -> bool:

        word_len = len(word)
        n_row, n_col = len(board), len(board[0])

        #@cache # cannot use memorize, since the state of each entry is different
        def backtrack(row, col, index):

            if index == word_len:
                return True

            if row < 0 or row >= n_row or col < 0 or col >= n_col:
                return False

            if board[row][col] != word[index]:
                return False

            board[row][col] = '#'
            ret = False
            for (next_row, next_col) in [(row, col+1), (row+1, col),
                                         (row, col-1), (row-1, col)]:
                ret = backtrack(next_row, next_col, index+1)
                if ret:
                    break
            board[row][col] = word[index]

            return ret

        for row in range(n_row):
            for col in range(n_col):
                if backtrack(row, col, 0):
                    return True
        return False