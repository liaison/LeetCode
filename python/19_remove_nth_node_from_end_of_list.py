# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # the distance between the 'prev' and 'curr' pointers is n
        curr, prev = head, None
        step = 0
        while curr:
            if prev:
                prev = prev.next

            if step == n:
                prev = head

            step += 1
            curr = curr.next

        if prev and prev.next:
            prev.next = prev.next.next
            return head
        else:
            # remove the head element
            return head.next