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