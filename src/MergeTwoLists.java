
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
     * 
    Given two sorted integer arrays A and B, merge B into A as one sorted array.

	Note:
	You may assume that A has enough space (size that is greater or equal to m + n) 
		to hold additional elements from B. 

	The number of elements initialized in A and B are m and n respectively.
     */
    public void merge(int A[], int m, int B[], int n) {
    	int p = m+n-1, Ai = m-1, Bi = n-1;
    	
    	while(Ai >= 0 && Bi >= 0){
    		if(A[Ai] > B[Bi]){
    			A[p--] = A[Ai--];
    		}else{
    			A[p--] = B[Bi--];
    		}
    	}
    	
    	if(Ai < 0){
    		// copy the rest of B to A 
    		while(Bi >= 0){
    			A[p--] = B[Bi--];
    		}
    	}// else Bi < 0, the rest of A is already in order.
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
		
		
		int [] A = new int[10];
		A[0] = 1; 
		A[1] = 3; 
		A[2] = 5;
		int [] B = {2, 4, 6, 8};
		solution.merge(A, 3, B, 4);
		
		for(int a : A){
			System.out.println(a);
		}
	}

}







