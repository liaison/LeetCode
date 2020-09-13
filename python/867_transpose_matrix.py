class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        TA = [[None] * len(A) for _ in range(len(A[0]))]
        
        # This initializaiton wont work!!!  The elements are essentially references.
        # TA = [[0] * len(A)] * len(A[0])
        
        for row in range(len(A)):
            for col, num in enumerate(A[row]):
                TA[col][row] = num
            
        return TA