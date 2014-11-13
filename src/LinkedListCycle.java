
/**
 * 

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 13, 2014
 *
 */

public class LinkedListCycle {

	
	/**
	 * Faster and slower pointers
	 */
    public boolean hasCycle(ListNode head) {
        ListNode fast_iter = head;
        ListNode slow_iter = head;
      
        // empty and simple element in the list
        if(head == null || head.next == null){
        	return false;
        }
        
        while(fast_iter != null){
        	fast_iter = fast_iter.next;
            slow_iter = slow_iter.next;
            
            if(fast_iter != null){
            	// move two steps at one time.
                fast_iter = fast_iter.next;
                if(fast_iter == slow_iter){
                	// fast pointer catches the slow pointer, there is cycle!
                	return true;
                }
            }
        }
        
        return false;
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
