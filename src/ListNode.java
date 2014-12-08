
 /** 
  * 
  * Definition for singly-linked list.
  * 
  */
public class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
		next = null;
	}


	/**
	 * Reverse a linked list in place 
	 * 
	 * 1 -> 2 -> 3 -> NULL 
	 * 3 -> 2 -> 1 -> NULL
	 * 
	 * @param head
	 * @return
	 */
	public static ListNode reverse(ListNode head){
		ListNode preIter = head, postIter = null;
		if(preIter == null)
			return null;
		
		postIter = preIter.next;
		
		while(postIter != null){
			ListNode nextIter = postIter.next;
			postIter.next = preIter;  // reverse the link
			
			// move on
			preIter = postIter;
			postIter = nextIter;
		}
		
		head.next = null; // end the list
		return preIter;
	}
}







