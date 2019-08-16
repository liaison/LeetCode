"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

The distance between a node and its child nodes is 1.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]


@author: Lisong Guo <lisong.guo@me.com>

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def buildGraph(self, node, parent, graph):
        if node is None:
            return
        
        if parent is not None:
            graph[node].append(parent)
        
        if node.left is not None:
            graph[node].append(node.left)
            self.buildGraph(node.left, node, graph)
        
        if node.right is not None:
            graph[node].append(node.right)
            self.buildGraph(node.right, node, graph)
        
        
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        from collections import defaultdict
        # vetex: [parent, left, right]
        graph = defaultdict(list)
        
        # DFS to build graph
        self.buildGraph(root, None, graph)
        
        # BFS to retrieve the nodes with given distance
        # Starting from the target node
        q = [(target, 0)]
        
        # keep the records, since the graph is all connected
        visited = set()
        # results
        ans = []
        while q:
            node, distance = q.pop(0)
            if node in visited:
                continue
            visited.add(node)
            
            # we've reached the desired distance/radius
            if K == distance:
                ans.append(node.val)
            
            # we haven't reached the desired distance, keep going
            elif distance < K:
                for child in graph[node]:
                    q.append((child, distance+1))
            # exceed the desired distance
            # No need to go further
        
        return ans
