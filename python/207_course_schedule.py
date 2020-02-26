"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseDict = {}
    
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            if prevCourse in courseDict:
                courseDict[prevCourse].add(nextCourse)
            else:
                courseDict[prevCourse] = set([nextCourse])

        for courseNum in range(numCourses):
            visited = set()
            if self.isCyclic(courseNum, courseDict, visited):
                return False
        
        return True


    def isCyclic(self, courseNum, courseDict, visited):
        if courseNum not in courseDict:
            # this is the last course to take
            return False
        
        for child in courseDict[courseNum]:
            if child in visited:
                return True
            
            visited.add(child)
            if self.isCyclic(child, courseDict, visited):
                return True
            visited.remove(child)
    
        return False


class SolutionBacktracking(object):
    """
      a more proper backtracking solution
    """

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseDict = {}
    
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            if prevCourse in courseDict:
                courseDict[prevCourse].add(nextCourse)
            else:
                courseDict[prevCourse] = set([nextCourse])

        visited = [False] * numCourses    
        for courseNum in range(numCourses):
            if self.isCyclic(courseNum, courseDict, visited):
                return False
        
        return True


    def isCyclic(self, courseNum, courseDict, visited):
    
        if courseNum not in courseDict:
            # this is the last course to take
            return False
    
        visited[courseNum] = True
        
        # backtracking
        ret = False
        for child in courseDict[courseNum]:
            if visited[child]:
                ret = True
                break
            ret = self.isCyclic(child, courseDict, visited)
            if ret: break
    
        visited[courseNum] = False
        return ret
    
    
    

class GNode(object):    
    def __init__(self, label):
        self.label = label
        self.inNodes = set()
        self.outNodes = set()


class SolutionTopologicalSorting(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [GNode(i) for i in range(numCourses)]
        
        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.add(nextCourse)
            graph[nextCourse].inNodes.add(prevCourse)
            totalDeps += 1

        nodepCourses = set()
        for i in range(numCourses):
            if len(graph[i].inNodes) == 0:
                nodepCourses.add(i)
    
        removedEdges = 0
        while nodepCourses:
            # pop out a random element
            course = nodepCourses.pop()
            
            for nextCourse in graph[course].outNodes:     
                graph[nextCourse].inNodes.remove(course)
                removedEdges += 1
                if len(graph[nextCourse].inNodes) == 0:
                    nodepCourses.add(nextCourse)
        
        # if there are still some edges left, then there exist some cycles
        # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
        if removedEdges == totalDeps:
            return True
        else:
            return False
