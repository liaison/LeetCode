/**
 * 
 * Sort a linked list in O(n log n) time using constant space complexity.
 * 
 * https://oj.leetcode.com/problems/sort-list/
 * 
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 12, 2014
 *
 */


public class QuickSort {
	
	/**
	 * Quick sort on linked list
	 */
    public ListNode sortList(ListNode head) {
    	
		if(head == null){
			return null;
		}
		
		ListNode pivot = head;
		head = head.next;
		
		ListNode bigHead = null, smallHead=null;
		ListNode bigIter = null, smallIter=null;
		
		while(head != null){
			ListNode iter = head.next;
			
			if(head.val >= pivot.val){
				if(bigHead == null){
					bigHead = head;
					bigIter = bigHead;
				}else{
					bigIter.next = head;
					bigIter = bigIter.next;
				}
			}else{
				if(smallHead == null){
					smallHead = head;
					smallIter = smallHead;
				}else{
					smallIter.next = head;
					smallIter = smallIter.next;
				}
			}
			
			head = iter;
		}
		
		// mark the ends for the big/small sub lists.
		if(smallIter != null){
			smallIter.next = null;
		}
		
		if(bigIter != null){
			bigIter.next = null;	
		}
		
		ListNode sortBig = sortList(bigHead);
		ListNode sortSmall = sortList(smallHead);
		
		if(sortSmall == null){
			pivot.next = sortBig;
			return pivot;

		} else {
			smallIter = sortSmall;
			while (smallIter.next != null) {
				smallIter = smallIter.next;
			}
			
			// reach the tail of the small sublist
			smallIter.next = pivot;
			// concatenate the two sublists.
			pivot.next = sortBig;
			
			return sortSmall;	
		}
    }
    
    
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int [] A = {3, 1, 4, 2, 5 };
		ListNode head = Utils.array2LinkedList(A);
		
		QuickSort solution = new QuickSort();
		
		head = solution.sortList(head);
		
		Utils.printLinkedNodeList(head);
		
	}

}






