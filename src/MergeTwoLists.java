
/**
 * Merge two sorted linked lists and return it as a new list. 
 * The new list should be made by splicing together the nodes of the first two lists.
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 08, 2014
 */

public class MergeTwoLists {

	/**
	 * 
	 * @return
	 */
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    	
    	if(l1 == null)
    		return l2;
    	if(l2 == null)
    		return l1;
    	
    	ListNode l1_iter = l1, l2_iter = l2;
    
    	ListNode pyseudoHead = new ListNode(0);
    	ListNode res_iter = pyseudoHead;
    	
    	while(l1_iter != null && l2_iter != null){
    		
    		if(l1_iter.val < l2_iter.val){
    			res_iter.next = l1_iter;
    			res_iter = l1_iter;
    			l1_iter = l1_iter.next;
    		}else{
        		res_iter.next = l2_iter;
        		res_iter = l2_iter;
        		l2_iter = l2_iter.next;
    		}
    	}
    	
    	if(l1_iter == null){
    		res_iter.next = l2_iter;
    	}else{
    		res_iter.next = l1_iter;
    	}
    	
    	return pyseudoHead.next;
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int [] l1_num = {1, 3, 5, 7};
		ListNode l1 = Utils.array2LinkedList(l1_num);
		
		int [] l2_num = {2, 4, 6, 8};
		ListNode l2 = Utils.array2LinkedList(l2_num);
	
		MergeTwoLists solution = new MergeTwoLists();	
		ListNode res = solution.mergeTwoLists(l1, l2);
		Utils.printLinkedNodeList(res);
	}

}







