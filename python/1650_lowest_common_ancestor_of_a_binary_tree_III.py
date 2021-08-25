

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
            Bidirectional BFS search to find the earliest intersection,
            It is generic that it can be applied to the graph data structure as well.
        """
        seen = set()
        queue = deque([q, p])

        while queue:
            curr_node = queue.popleft()
            if curr_node.val in seen:
                return curr_node

            seen.add(curr_node.val)

            if curr_node.parent:
                queue.append(curr_node.parent)



"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        """
            https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/932914/Java-in-6-lines
            Two runners in a cycle

                1 ------o---    1 + 2:  ------o-----o---
                2     --o---    2 + 1:  --o---------o---

                lengths after o (o---) are always same, so 2 pointers finally meet at the same node
        """
        one, other = p, q

        # run through the combined path to reach the joint point.
        while one != other:
            one = q if one is None else one.parent
            other = p if other is None else other.parent

        return one



class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def dfs(node, ancestor_set):
            if node:
                ancestor_set.add(node.val)
                dfs(node.parent, ancestor_set)

        p_ancestors = set()
        dfs(p, p_ancestors)

        while q:
            if q.val in p_ancestors:
                return q
            q = q.parent
