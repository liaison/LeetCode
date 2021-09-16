
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        first_switch, second_switch = None, None

        step = 1
        # the distance between the 'prev' and 'curr' is k steps,
        #  so when the 'curr' reaches the end, the 'prev' would be the second switching point
        curr, prev = head, None

        while curr:
            if prev:
                prev = prev.next

            if step == k:
                # kick of the 'prev' pointer
                first_switch = curr
                prev = head

            # move on to the next step
            curr = curr.next
            step += 1

        second_switch = prev

        first_switch.val, second_switch.val = second_switch.val, first_switch.val

        return head