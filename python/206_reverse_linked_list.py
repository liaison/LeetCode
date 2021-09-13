# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head
        while curr:
            next_curr = curr.next
            curr.next = prev

            prev = curr
            curr = next_curr

        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # return the new head element
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        # reverse the pair of elements: head, head->next
        head.next.next = head
        head.next = None

        return new_head
