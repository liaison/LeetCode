class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x:x%2)
        return A

    
class SolutionTwoPointers:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        p_odd, p_even = 0, len(A)-1
        while p_odd < p_even:
            
            if A[p_odd] % 2 == 0:
                p_odd += 1
            elif A[p_even] % 2 == 1:
                p_even -= 1
            else:
                A[p_odd], A[p_even] = A[p_even], A[p_odd]
        
        return A