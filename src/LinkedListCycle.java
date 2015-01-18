
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
     * Given a linked list, return the node where the cycle begins. 
     * If there is no cycle, return null.
     * 
     * Distance from the head to the joint point, K 
     * First K steps: 
     * 		slow:  K    fast: 2K 
            distance of fast behind slow: D = (RING_SIZE - K) mod RING_SIZE
       
       Next D steps: (fast catches up the slow)
       	    distance of fast/slow to the joint point:  
       	    	(RING_SIZE - D) 
       		    = (RING_SIZE - (RING_SIZE-K) mod RING_SIZE)) 
       		
       		if RING_SIZE > K 
       			K 
       			
       			
       	    if RING_SIZE < K 
       	    	D = RING_SIZE - (K mod RING_SIZE)
       	    	
       	    	RING_SIZE - D
       	       = K mod RING_SIZE	
       		    
       
		Follow up:
			Can you solve it without using extra space?
     */
    public ListNode detectCycle(ListNode head) {
    	ListNode fast = head, slow = head;
    	
    	while(fast != null && fast.next != null){
    		fast = fast.next.next;
    		slow = slow.next;
    		
    		if(fast == slow)
    			break;
    	}
    	
    	// no loop
    	if(fast == null || fast.next == null){
    		return null;
    	}
    	
    	// Fast and slow pointers meet at the 
    	//	(RING_SIZE-K) position to the joint point 
    	// Move the slow pointer to the head, and keep 
    	//  the fast pointer at the same pace as slow, 
    	//  they would meet at the joint point. 
    	slow = head;
    	while(slow != fast){
    		slow = slow.next;
    		fast = fast.next;
    	}
    	
    	return slow;
    }
    
    
    /**
     * You are given two linked lists representing two non-negative numbers. 
     * The digits are stored in reverse order and each of their nodes contain a single digit. 
     * Add the two numbers and return it as a linked list.

		Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
		Output: 7 -> 0 -> 8
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	int carry = 0;
    	ListNode pseudoHead = new ListNode(0);
    	ListNode iter = pseudoHead;
    	int sum = 0;
    	while(l1 != null && l2 != null){
    		sum = l1.val + l2.val + carry;
    		ListNode digit = new ListNode(sum % 10);
    		carry = sum / 10;
    		iter.next = digit;
    		
    		iter = digit;
    		l1 = l1.next;
    		l2 = l2.next;
    	}
    	
    	l1 = (l1 == null) ? l2 : l1;
    	while(l1 != null){
    		sum = l1.val + carry;
    		ListNode digit = new ListNode(sum % 10);
    		carry = sum / 10;
    		iter.next = digit;
    		
    		iter = iter.next;
    		l1 = l1.next;
    	}
    	
    	if(carry != 0)
    		iter.next = new ListNode(1);  //mark the end;
    	
    	return pseudoHead.next;
    }
    
    
    public static void main(String[] args) {
		ListNode n1 = new ListNode(1);
		ListNode n2 = new ListNode(2);
		ListNode n3 = new ListNode(3);
		
		n1.next = n2;
		n2.next = n3;
		
		n3.next = n2; // a loop with n2 and n3;
		
		LinkedListCycle solution = new LinkedListCycle();
		ListNode joint = solution.detectCycle(n1);
		
		System.out.println(joint.val);
		

		ListNode l1 = Utils.array2LinkedList(new int[]{5});
		ListNode l2 = Utils.array2LinkedList(new int[]{5});
		Utils.printLinkedNodeList(solution.addTwoNumbers(l1, l2));
	}

}




