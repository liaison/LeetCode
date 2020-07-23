class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        result = [0] * len(A)
    
        # pointers to left and right end of the array.
        lp, rp = 0, len(A)-1
        sp = len(A) - 1 # pointer for the result list

        while sp >= 0:
            if abs(A[lp]) > abs(A[rp]):
                result[sp] = A[lp] * A[lp]
                lp += 1
            else:
                result[sp] = A[rp] * A[rp]
                rp -= 1
            sp -= 1
        
        return result
