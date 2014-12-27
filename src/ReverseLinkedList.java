

/**
 * 
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
	Given  1->2->3->4->5->NULL, m = 2 and n = 4,
	return 1->4->3->2->5->NULL.

Note:
	Given m, n satisfy the following condition:
	1 ≤ m ≤ n ≤ length of list.
	
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 24, 2014
 *
 */
public class ReverseLinkedList {

	
	private ListNode reverse_rec(ListNode start, int count){
		if(count == 0 || start == null)
			return start;
	
		ListNode newTail = reverse_rec(start.next, count-1);
		newTail.next = start;
		start.next = null;
		
		return start;
	}
	
	
	private ListNode reverse(ListNode start, int count){
		if(start == null || count <= 0)
			return start;
		
		ListNode preNode, postNode;
		
		preNode = start;
		postNode = preNode.next;
		preNode.next = null;  // clear the link for the first element.
		
		while(count > 0){
			ListNode next = postNode.next;
			
			// reverse the link
			postNode.next = preNode;
			count --;
			
			// move on to next pair.
			preNode = postNode;
			postNode = next;
		}
		
		return preNode;
	}
	
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head == null)
        	return head;
        
        ListNode preNewTail = null, postNewHead = null; 
        ListNode newTail, newHead;
        ListNode iter = head;
        int count = n - m;
        
        if( --m == 0){
    		preNewTail = null;
    	}
    			
        while(n > 1){
        	
        	if(m == 1){
        		preNewTail = iter;
        	}
        	
        	iter = iter.next;
        	m --;
        	n --;
        }
        
        newHead = iter;
        postNewHead = newHead.next;
        
        if(preNewTail == null){
        	newTail = head;
        }else{
        	newTail = preNewTail.next;
        }
        
        //this.reverse(newTail, count);
        this.reverse_rec(newTail, count);
        
        
        newTail.next = postNewHead;
        
        if(preNewTail != null){
        	preNewTail.next = newHead;
        	return head;
        }else{
        	return newHead;
        }
    }
    
    
	public static void main(String[] args) {
		int [] num = {1, 2, 3, 4, 5, 6};
		ListNode head = Utils.array2LinkedList(num);
		
		ReverseLinkedList solution = new ReverseLinkedList();
		
		ListNode newHead = solution.reverseBetween(head, 2, 4);
		Utils.printLinkedNodeList(newHead);
	}

}

















