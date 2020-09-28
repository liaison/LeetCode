# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#         def printList(head):
#             ret = []
#             while head:
#                 ret.append(head.val)
#                 head = head.next
#             print(ret)

class Solution:

    def insertionSortList(self, head: ListNode) -> ListNode:

        pseudo_head = ListNode()
        
        curr = head        
        while curr:
            prev_node = pseudo_head
            next_node = prev_node.next
            
            # find the position to insert the current node
            while next_node:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next
            
            # insert the current node to the new list
            new_node = ListNode(curr.val)
            if next_node:
                new_node.next = next_node
            prev_node.next = new_node
            
            # moving on
            curr = curr.next

        return pseudo_head.next


