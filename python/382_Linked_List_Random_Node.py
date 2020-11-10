# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 0
        chosen_value = 0
        curr = self.head
        
        while curr:
            pick = random.randint(0, scope)
            if pick == 0:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value

    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionSlidingWindow:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 0
        chosen_value = 0
        curr = self.head
        
        window_size = 100
        window = [0] * window_size
        total_index = 0
        
        while curr:
            w_index = 0
            while curr and w_index < window_size:
                window[w_index] = curr.val
                curr = curr.next
                w_index += 1
            
            total_index += w_index
            pick = random.randrange(0, total_index)
            if pick < w_index:
                chosen_value = window[pick]
            
            # move on to the round
            if curr:
                curr = curr.next
        
        return chosen_value


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()