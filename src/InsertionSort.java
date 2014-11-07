
/**
 * Sort a linked list using insertion sort.
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 */

public class InsertionSort {

	public static void main(String[] args) {
		int [] int_list = {5, 2, 1, 4, 4};
		ListNode input = getList(int_list);
		
		InsertionSort solution = new InsertionSort();
		ListNode output = solution.insertionSortList(input);
		
		System.out.println("Input:");
		printList(input);
		
		System.out.println("Output:");
		printList(output);
	}

	/**
	 *  Memory management is tricky !!!  
	 *  Need to create a new element for each element in the original list, 
	 *  	otherwise the results would be totally mess-up, since Java applies
	 *  	reference for each object.
	 * @param head
	 * @return
	 */
	public ListNode insertionSortList(ListNode head) {

		ListNode result = null;
		ListNode elem = head;

		while (elem != null) {
			ListNode resultCur = result;

			if (resultCur == null) {
				result = new ListNode(elem.val);
				elem = elem.next;
				continue;
			} else {

				while (resultCur.next != null) {
					if (elem.val > resultCur.val) {
						resultCur = resultCur.next;
					} else {
						break;
					}
				}
				
				// In the middle of somewhere 
				if(resultCur.next != null){
					// Insert the new element in front of "resultCur" (switch the values).
					ListNode newNode = new ListNode(resultCur.val);
					resultCur.val = elem.val;
					
					newNode.next = resultCur.next;
					resultCur.next = newNode;
					
				}else{ // The last element in the result set.
					
					if(elem.val > resultCur.val){
						// Put the new element in the tail, after "resultCur".
						ListNode newNode = new ListNode(elem.val);
						resultCur.next = newNode;
					
					}else{
						// Insert the new element in front of "resultCur".
						ListNode newNode = new ListNode(resultCur.val);
						resultCur.val = elem.val;
						
						newNode.next = resultCur.next;
						resultCur.next = newNode;	
					}
				}
			}

			elem = elem.next;
		}

		return result;
	}
	
	
	
	public static ListNode getList(int [] values){
		if(values.length == 0){
			return null;
		}
		
		ListNode head = new ListNode(values[0]);
		ListNode curr = head;
		
		for(int i=1; i < values.length; i++){
			ListNode newNode = new ListNode(values[i]); 
			curr.next = newNode;
			curr = newNode;
		}
		
		return head;
	}
	
	public static void printList(ListNode head){
		while(head != null){
			System.out.println(head.val);
			head = head.next;
		}
	}

	
}
