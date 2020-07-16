class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1
        
        ans = []
        
        def DFS(sublist):
            if len(sublist) <= 1:
                return 
            
            # locate the position of max value for this round
            max_value, max_index = len(sublist), 0
            for index, value in enumerate(sublist):
                if value == max_value:
                    max_index = index
                    break
            
            # sink the max number to the bottom, 
            #   with at most two steps of pancake flipping
            #   i.e. flip the max number to the head if necessary,
            #        and then flip it to the bottom
            if max_index != len(sublist) - 1:
                if max_index != 0:
                    ans.append(max_index+1)
                    flip(sublist, max_index+1)
                    
                ans.append(max_value)
                flip(sublist, max_value)
            
            # move on to the next round
            DFS(sublist[0:-1])
        
        DFS(A)
        
        return ans

