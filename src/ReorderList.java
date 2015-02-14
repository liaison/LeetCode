import java.util.ArrayList;


public class ReorderList {

	/**
	 * Given a singly linked list L: L0→L1→…→Ln-1→Ln,
			reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

		You must do this in-place without altering the nodes' values.

		For example,
			Given {1,2,3,4}, reorder it to {1,4,2,3}.
	 
	 	Note: there is a O(N) time complexity and O(1) space complexity solution.
	public void reorderList(ListNode head) {
        if(head == null) return;
        
    	ArrayList<ListNode> array = new ArrayList<ListNode>();
        
        ListNode iter = head;
        while(iter != null) {
        	array.add(iter);
        	iter = iter.next;
        }
        
        int hd=0, tl=array.size()-1;
        while(hd < tl) {
        	array.get(hd).next = array.get(tl);
        	array.get(tl).next = array.get(hd+1);
        	
        	++hd;
        	--tl;
        }
        // mark the end of the new linked list.   
        array.get(hd).next = null;
    }
	 */
	
	/**
	 *  1). Find the mid point and cut the list into halves
	 *  2). Reverse the second half of the list 
	 *  3). Merge the two half lists.  
	 */
	public void reorderList(ListNode head) {
		if(head == null || head.next == null) return;
		
		// Find the mid point in the list.
		ListNode slow = head, fast = head.next;
		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		
		
		// Reverse the second half of the original list.
		ListNode mid = slow, iter = slow.next;
		mid.next = null;  // Cut the list into two.
		
		while(iter != null) {
			ListNode temp = iter.next;
			iter.next = mid;
			mid = iter;
			iter = temp;
		}
		
		// Merge the two sublists. 
		ListNode pre = head, post = mid;
		while(pre != null && post != null) {
			ListNode nextPre = pre.next;
			ListNode nextPost = post.next;
			pre.next = post;
			post.next = nextPre;
			
			pre = nextPre;
			post = nextPost;
		}
	}
    
    public static void main(String [] args) {
    	int [] num = {1, 2, 3};
    	ListNode head = Utils.array2LinkedList(num);
    	
    	ReorderList solution = new ReorderList();
    	solution.reorderList(head);
    	Utils.printLinkedNodeList(head);
    }


}
