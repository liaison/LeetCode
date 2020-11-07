"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        node_indegree = {}
        
        for node in tree:
            if node not in node_indegree:
                node_indegree[node] = 0
            for child in node.children:
                node_indegree[child] = 1
        
        for node, indegree in node_indegree.items():
            if indegree == 0:
                return node


class SolutionSet:
    def findRoot(self, tree: List['Node']) -> 'Node':

        seen = set()
        
        for node in tree:
            for child in node.children:
                seen.add(child.val)
        
        for node in tree:
            if node.val not in seen:
                return node

            

        