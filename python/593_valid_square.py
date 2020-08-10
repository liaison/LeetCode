class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        points = sorted([tuple(p1), tuple(p2), tuple(p3), tuple(p4)])
        
        diag1 = (points[3][0] - points[0][0],
                 points[3][1] - points[0][1])
        
        diag2 = (points[2][0] - points[1][0],
                 points[2][1] - points[1][1])
        
        mid1 = ((points[3][0] + points[0][0]) / 2, 
                (points[3][1] + points[0][1]) / 2)
        mid2 = ((points[2][0] + points[1][0]) / 2,
                (points[2][1] + points[1][1]) / 2)
        
        # vectors of the same length
        # orthogonal vectors
        if mid1 != mid2 or \
           (diag1[0] ** 2 + diag1[1] ** 2) == 0 or \
           (diag1[0] * diag2[0] + diag1[1] * diag2[1]) != 0.0 or \
           (diag1[0] ** 2 + diag1[1] ** 2) != (diag2[0] ** 2 + diag2[1] ** 2):
            return False
    
        return True