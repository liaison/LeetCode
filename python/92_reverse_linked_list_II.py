

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        linked_list = []
        curr = head
        while curr:
            linked_list.append(curr)
            curr = curr.next

        left, right = left - 1, right - 1

        # reverse the linked list within the specified range
        p_right = right
        while p_right > left:
            linked_list[p_right].next = linked_list[p_right-1]
            p_right -= 1

        # chain the prefix if necessary
        if left >= 1:
            linked_list[left-1].next = linked_list[right]

        # chain up the postfix if necessary, else set the last pointer to None to mark the end.
        if right < len(linked_list) - 1:
            linked_list[left].next = linked_list[right+1]
        else:
            linked_list[left].next = None

        return head if left != 0 else linked_list[right]

