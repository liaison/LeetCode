import java.util.ArrayList;


public class ReorderList {

	/**
	 * Given a singly linked list L: L0→L1→…→Ln-1→Ln,
			reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

		You must do this in-place without altering the nodes' values.

		For example,
			Given {1,2,3,4}, reorder it to {1,4,2,3}.
	 */
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
    
    public static void main(String [] args) {
    	int [] num = {1, 2, 3, 4, 5};
    	ListNode head = Utils.array2LinkedList(num);
    	
    	ReorderList solution = new ReorderList();
    	solution.reorderList(head);
    	Utils.printLinkedNodeList(head);
    }


}
