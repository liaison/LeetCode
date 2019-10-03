'''
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y

Note:

    - There are at least 1 and at most 1000 words.
    - All words will have the exact same length.
    - Word length is at least 1 and at most 5.
    - Each word contains only lowercase English alphabet a-z.

Example 1:

Input:
    ["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

'''


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = {}
        SIZE = len(words[0])
        WORD_KEY = '$'
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})    
            node[WORD_KEY] = word
        
        ret = []
        word_square = [''] * SIZE
        def backtracking(keyword, row:int, col:int, node):
            
            if row == SIZE:
                ret.append(word_square[:])
                return
            
            while col < row:
                letter = word_square[col][row]    
                col += 1
                node = node.get(letter, None)
                if not node:
                    return

#             while col < SIZE-1 and len(node) == 1:
#                 node = next(iter(node.values()))
#                 col += 1
            
            for letter in node:

                nextNode = node[letter]
                newRow, newCol = row + (col + 1) // SIZE, (col + 1) % SIZE
                
                # end of line
                if newCol == 0:
                    newWord = nextNode[WORD_KEY]
                    word_square[row] = newWord
                    nextNode = trie
                
                backtracking(keyword, newRow, newCol, nextNode)
    
                if newCol == 0:
                    word_square[row] = ''
        
        for word in words:
            if not all([l in trie for l in word]):
                continue
            #word_square = [''] * SIZE
            word_square[0] = word
            backtracking(word, 1, 0, trie)
        
        return ret