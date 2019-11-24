
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution_recursion(object):
    def flatten(self, head):
        if not head:
            return head
    
        def flatten_dfs(prev, curr):
            """ return the tail of the flatten list """
            if not curr:
                return prev
            
            curr.prev = prev
            prev.next = curr
            
            # the curr.next would be temperred in the recursive function
            tempNext = curr.next
            
            tail = flatten_dfs(curr, curr.child)
            curr.child = None
            
            return flatten_dfs(tail, tempNext)
        
        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        flatten_dfs(pseudoHead, head)
        
        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next


class Solution_iteration(object):
    def flatten(self, head):
        if not head:
            return
        
        pseudoHead = Node(0,None,head,None)     
        
        prev = pseudoHead
        stack = []
        stack.append(head)
        
        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            prev = curr        
    
        pseudoHead.next.prev = None
        return pseudoHead.next