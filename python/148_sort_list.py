# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head):
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return head, slow
    
    def merge(self, first, second):
        
        merge_head = ListNode()
        pm, p1, p2 = merge_head, first, second
        while p1 and p2:
            if p1.val <= p2.val:
                pm.next = p1
                p1 = p1.next
            else:
                pm.next = p2
                p2 = p2.next
            pm = pm.next
        
        pm.next = p1 or p2
        return merge_head.next

    
    def sortList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        first_half, second_half = self.partition(head)
        
        first_half = self.sortList(first_half)
        second_half = self.sortList(second_half)
        
        return self.merge(first_half, second_half)
