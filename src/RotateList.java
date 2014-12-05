

/**
 * 

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 4, 2014
 * 
 */
public class RotateList {

	/**
	 * Two pace pointers 
	 * 
	 * @param head
	 * @param n
	 * @return
	 */
    public ListNode rotateRight(ListNode head, int n) {
    	ListNode newHead = head, iter = head;
    	
    	for(int i=n; i>0; i--){
    		if(head == null)
    			return null;
    		
    		head = head.next;
    	}
    	
    	while(head != null){
    		newHead = newHead.next;
    		head = head.next;
    	}
    	
    	iter = newHead;
    	while(iter.next != null){
    		iter = iter.next;
    	}
    	iter.next = head;
    	
    	return newHead;
    }
    
    
	public static void main(String[] args) {
		
		Utils.array2LinkedList();
		
	}

}

