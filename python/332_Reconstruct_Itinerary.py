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
 