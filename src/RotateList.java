

/**
 * 

Given a list, rotate the list to the right by k places, where k is non-negative.

Rotate the last element of the list by K times, 
	each time put the last element to the head.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Note: 
	when n = 0, return old list
	when n > size of list,  return the reverse of the original list
	  

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
    	if(n == 0 || head == null || head.next == null) return head;

    	ListNode preNewHead = head;
    	ListNode iter = head;
    	
    	int size = 0;
    	while(iter != null){
    		iter = iter.next;
    		size ++;
    	}
    	
    	int k = n % size;
    	iter = head;
    	
    	if(k == 0) return head;
    	
    	// fast pointer goes K steps first.
    	while(k-- > 0){
    		iter = iter.next;
    	}
    	
    	while(iter.next != null){
    		preNewHead = preNewHead.next;
    		iter = iter.next;
    	}
    	
    	ListNode newHead = preNewHead.next;
    	// Set the ending point for the new list.
    	preNewHead.next = null; 
    	
    	// Connect back to the old head;
    	iter.next = head;
    	
    	return newHead;

    }
    
    
	public static void main(String[] args) {
		
		
		int [] num = {1, 2, 3};
		int k = 5; 
		
		
		// input: {1, 2} k=3, expected: {2, 1}
		// input: {1, 2} k=2, expected: {1, 2}
		/**
		int [] num = {1, 2};
		int k = 2; 
		*/
		
		RotateList solution = new RotateList();
		
		ListNode head = Utils.array2LinkedList(num);
		
		Utils.printLinkedNodeList(solution.rotateRight(head, k));
		
	}

}

