
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
				next = next.next;
				iter.next = next;
			} else {
				iter = next;
				next = next.next;
			}
		}

    	return head;
    }
	
	public static void main(String[] args) {
		int [] i = {1, 1, 2, 3, 3};
		//int [] i = {1, 1, 1};
		
		ListNode head = Utils.array2LinkedList(i);
		
		LinkedListDuplicate solution = new LinkedListDuplicate();
		
		Utils.printLinkedNodeList(solution.deleteDuplicates(head));
	}

}
