import org.junit.Test;


/**
 * 

Given a sorted linked list, 
	delete all duplicates such that each element appear only once.

For example,
	Given 1->1->2, return 1->2.
	Given 1->1->2->3->3, return 1->2->3.
	
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 22, 2014
 *
 */
public class LinkedListDuplicate {

	
    public ListNode deleteDuplicates(ListNode head) {
    	ListNode iter = head;
    	if(iter == null)
    		return null;
    	
    	ListNode next = iter.next;		
		while (next != null) {

			if (iter.val == next.val) {
				// Do not move the Iter pointer just yet, 
				//	since there could be a triple duplicates.
				next = next.next;
				iter.next = next;
			} else {
				iter = next;
				next = next.next;
			}
		}

    	return head;
    }
    
    
    /**
     * Remove all elements from a linked list of integers that have value val.

		Example
			Given:  1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
			Return: 1 --> 2 --> 3 --> 4 --> 5
     */
    public ListNode removeElements(ListNode head, int val) {
        ListNode pseudoHead = new ListNode(0);
        pseudoHead.next = head;
        
    	ListNode iter = pseudoHead;

        while(iter.next != null) {
        	
        	// The next node match the value.
        	if (iter.next.val == val) {
        		// remove the next node.
        		iter.next = iter.next.next;
        	} else {
        		iter = iter.next;
        	}
        }
        
        return pseudoHead.next;
    }
    
    /**
     * Write a function to delete a node (except the tail) in a singly linked list,
        given only access to that node.

        Supposed the linked list is 1 -> 2 -> 3 -> 4 and
        you are given the third node with value 3,
        the linked list should become 1 -> 2 -> 4 after calling your function.
     */
    public void deleteNode(ListNode node) {
        // node won't be the tail, therefore no need to check node.next != null.
        node.val = node.next.val;
        node.next = node.next.next;
    }

    @Test
    public void testDeleteNode() {
        int [] input = {1, 1, 2, 3, 3};
        ListNode head = Utils.array2LinkedList(input);

        ListNode node2 = head.next.next;
        new LinkedListDuplicate().deleteNode(node2);

        Utils.printLinkedNodeList(head);
    }


    @Test
    public void testRemoveElement() {
    	int [] input = {1, 1, 2, 3, 3};
    	ListNode head = Utils.array2LinkedList(input);
    	ListNode newHead = new LinkedListDuplicate().removeElements(head, 3);
    	
    	Utils.printLinkedNodeList(newHead);
    }
    
    
	public static void main(String[] args) {
		int [] i = {1, 1, 2, 3, 3};
		//int [] i = {1, 1, 1};
		
		ListNode head = Utils.array2LinkedList(i);
		
		LinkedListDuplicate solution = new LinkedListDuplicate();
		
		Utils.printLinkedNodeList(solution.deleteDuplicates(head));
	}

}
