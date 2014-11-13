import java.util.ArrayList;

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
	 * Return both the head and tail of the final result.
	 * @return
	 */
	public ArrayList<ListNode> quick_sort(ListNode head){
		
		ArrayList<ListNode> res = new ArrayList<ListNode>();
		
		if(head == null){
			res.add(null);
			res.add(null);
			return res;
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
		
		ArrayList<ListNode> sortBig = quick_sort(bigHead);
		ArrayList<ListNode> sortSmall = quick_sort(smallHead);

		if(sortSmall.get(0) == null){
			pivot.next = sortBig.get(0);
			res.add(pivot);
			
		}else{
			res.add(sortSmall.get(0));
			sortSmall.get(1).next = pivot;

			pivot.next = sortBig.get(0);
		}
		
		if(sortBig.get(1) == null){
			res.add(pivot);
		}else{
			res.add(sortBig.get(1));
		}
		
		
		return res;
	}
	
	
	/**
	 * Quick sort on linked list
	 
    public ListNode sortList(ListNode head) {
    	ArrayList<ListNode> res = quick_sort(head);
    	return res.get(0);
    }
    
    */
	
	
	/**
	 * Quick sort on linked list
	 */
    public ListNode sortList(ListNode head) {
    	
		if(head == null || head.next == null){
			return head;
		}
		
		ListNode pivot = head;
		head = head.next;
		
		ListNode bigHead = null, smallHead=null;
		ListNode bigIter = null, smallIter=null;
		ListNode pivotIter = pivot;
		
		while(head != null){
			ListNode iter = head.next;
			
			if(head.val > pivot.val){
				if(bigHead == null){
					bigHead = head;
					bigIter = bigHead;
				}else{
					bigIter.next = head;
					bigIter = bigIter.next;
				}
			}else if(head.val == pivot.val){
				pivotIter.next = head;
				pivotIter = pivotIter.next;
				
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
		
		pivotIter.next = null;
		
		if(bigIter != null){
			bigIter.next = null;	
		}
		
		
		ListNode sortBig = sortList(bigHead);
		ListNode sortSmall = sortList(smallHead);
		
		if(sortSmall == null){
			pivotIter.next = sortBig;
			return pivot;

		} else {
			smallIter = sortSmall;
			while (smallIter.next != null) {
				smallIter = smallIter.next;
			}
			
			// reach the tail of the small sublist
			smallIter.next = pivot;
			// concatenate the two sublists.
			pivotIter.next = sortBig;
			
			return sortSmall;	
		}
    }
    
    
	
    
    
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int [] A = {3, 1, 4, 4, 5, 6};
		//int [] A = {1, 1, 1, 1, 1};
		
		//int [] A = {1,3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1,1,2,2,2,1,2,1,1,2,3,3,2,2,3,2,3,2,2,2};
				
		ListNode head = Utils.array2LinkedList(A);
		
		QuickSort solution = new QuickSort();
		
		head = solution.sortList(head);
		
		Utils.printLinkedNodeList(head);
		
	}

}






