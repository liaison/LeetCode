"""
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution_refined:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
        
        prev, curr = head, head.next
        toInsert = False
        
        while True:
                
            if prev.val <= insertVal <= curr.val:
                # simple case
                toInsert = True
            elif prev.val > curr.val:
                # case where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:    
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head
            
            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break

        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head



class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
        
        curr = head
        prev = curr
        tail = None
        isAdded = False
        while True:
            if curr.val <= insertVal and insertVal <= curr.next.val:
                newNode = Node(insertVal, curr.next)
                curr.next = newNode
                isAdded = True
                break
            else:
                prev = curr
                curr = curr.next
            
            # Find the tail element !
            if prev.val > curr.val:
                tail = prev
                # optimization step, early break !
                if insertVal > tail.val or insertVal < tail.next.val:
                    break
                
            if curr == head:
                break
        
        if not isAdded:
            if tail:
                newNode = Node(insertVal, tail.next)
                tail.next = newNode
            else:
                newNode = Node(insertVal, curr)
                prev.next = newNode
        
        return head
 