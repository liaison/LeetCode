/**
 * 
 * @author Lisng Guo <lisong.guo@me.com>
 * @date   Jan 18, 2015
 *
 */
public class SwapNodes {


	/**
	 * Given a linked list, swap every two adjacent nodes and return its head.
		For example,
			Given 1->2->3->4, you should return the list as 2->1->4->3.
			
		Your algorithm should use only constant space. 
		You may not modify the values in the list, 
			only nodes itself can be changed.
	 */
    public ListNode swapPairs(ListNode head) {
        ListNode first, second, next=head;
        ListNode res;
        
        if(head == null || head.next == null){
        	return head;
        }
        
        first = head;
        second = head.next;
        res = second;
        
        ListNode prevFirst = first;
        
        while(next != null){

        	first = next;
        	second = next.next;
        	
        	if(second == null)
        		break;
        	
        	next = second.next;  // move on
            
        	second.next = first; // swap the pair
        	
        	prevFirst.next = second;
        	prevFirst = first;
        }
        
        if(second == null){ // list with odd number nodes
        	prevFirst.next = first;
        }else{
        	prevFirst.next = null; // End the list.
        }
        
        
        return res;
    }
	
	public static void main(String[] args) {
		//int [] num = {1, 2, 3, 4}; 
		int [] num = {}; 
		
		SwapNodes solution = new SwapNodes();
		ListNode head = Utils.array2LinkedList(num);
		
		Utils.printLinkedNodeList(solution.swapPairs(head));
	}

}
