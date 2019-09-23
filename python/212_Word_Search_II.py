"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

"""

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        # we don't need to store the actual value, 
        #   since the prefix would do the comparison of values along the path.
        self.hasValue = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
          Inserts a word into the trie, 
          create nodes along the way.
        """
        curr = self.root
        for key in word:
            if key in curr.children:
                curr = curr.children[key]
            else:
                # create the new node
                newNode = TrieNode()
                curr.children[key] = newNode
                curr = newNode

        # reach the desired node
        curr.hasValue = True

    
    def match(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for key in word:
            if key in curr.children:
                curr = curr.children[key]
            else:
                # mismatch of prefix, early return
                return 0
        
        # check if the node contains a value
        if curr.hasValue:
            return 2
        else:
            return 1

class Solution_optimal:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        MaxWordLen = 0
        
        wordInitSet = set()
        # create the word dictionary for quick lookup later, with Trie
        wordDict = Trie()
        wordIndice = {}
        for index, word in enumerate(words):
            wordDict.insert(word)
            MaxWordLen = max(len(word), MaxWordLen)
            wordInitSet.add(word[0])
            wordIndice[word] = index
        
        rowNum = len(board)
        colNum = len(board[0])
        
        def nextPosition(row, col, dirIndex):
            DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            offsets = DIRECTIONS[dirIndex]
            row = row + offsets[0]
            col = col + offsets[1]
            if row < 0 or row >= rowNum or col < 0 or col >= colNum:
                return None
            else:
                return (row, col)
        
        ans = set()
        visited = set()
        def backtracking(row, col, prefix):
            nonlocal ans
            
            if len(prefix) > MaxWordLen:
                # no need to explore further
                return
            
            res = wordDict.match(prefix)
            if res == 2:
                # We found a matched word
                #ans.add(prefix)
                # Store the indice of words instead of the string value
                ans.add(wordIndice[prefix])
            elif res == 0:
                # No match whatsoever
                return
            #elif res == 1:
                # We found a matched prefix
            
            for dirIndex in range(4):
                nextPos = nextPosition(row, col, dirIndex)
                if nextPos is None or nextPos in visited:
                    continue
                
                visited.add(nextPos)
                newPrefix = prefix + board[nextPos[0]][nextPos[1]]
                
                backtracking(nextPos[0], nextPos[1], newPrefix)
                
                visited.remove(nextPos)
        
        for row in range(rowNum):
            for col in range(colNum):
                # narrow down the starting points
                if board[row][col] not in wordInitSet:
                    continue
                
                # starting from the position
                visited = set()
                visited.add((row,col))
                backtracking(row, col, prefix=board[row][col])
    
        return map(words.__getitem__, list(ans))
        

        
