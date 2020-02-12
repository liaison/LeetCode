"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.


author note: we could have multiple identifical flights in the input.
e.g.  ['TIA', 'JFK'], ['TIA', 'JFK'], ['JFK', 'TIA'], ['JFK', 'TIA']

"""

class Solution(object):
    def findItinerary(self, tickets):
        """
            faster than 10% of submissions
            
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.originMap = defaultdict(list)
        
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.originMap[origin].append(dest)
        
        # sort the itinerary based on the lexical order
        for origin, itinerary in self.originMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort()
        
        self.flights = len(tickets)
        self.visited = set()
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)
        
        return self.result


    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True
        
        for i, nextDest in enumerate(self.originMap[origin]):
            # unique label to identify an itinerary
            label = origin + str(i)
            if label not in self.visited:
                self.visited.add(label)
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visited.remove(label)
                if ret:
                    # early stopping of backtracking
                    return True
            
        return False

    
    
class Solution_Faster(object):
    """ faster than 19.5 of submissions """
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.originMap = defaultdict(list)
        
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.originMap[origin].append(dest)
        
        self.visitBitmap = {}
        
        # sort the itinerary based on the lexical order
        for origin, itinerary in self.originMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort()
            self.visitBitmap[origin] = [False]*len(itinerary)
        
        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)
        
        return self.result


    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True
        
        for i, nextDest in enumerate(self.originMap[origin]):
            # unique label to identify an itinerary
            if not self.visitBitmap[origin][i]:
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True
            
        return False
        

class SolutionFastest(object):
    def findItinerary(self, tickets):
        """
            faster than 96% of submissions
        
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.originMap = defaultdict(list)
        
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.originMap[origin].append(dest)
        
        # sort the itinerary based on the lexical order
        for origin, itinerary in self.originMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)
        
        self.flights = len(tickets)
        self.result = []
        self.DFS('JFK')
    
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.originMap[origin]
        while destList:
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)
    
 