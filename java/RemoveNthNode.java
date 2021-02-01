
/**
 * 
 * https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
 * 
 Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.
Try to do this in one pass.

 * 
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 12, 2014
 * 
 *
 */


public class RemoveNthNode {
    
	public ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode f_cur = head, b_cur = head;
		
		if(n <= 0){
			return head;
		}
		
		while(--n >= 0 && f_cur != null){
			f_cur = f_cur.next;
		}
		
		if(f_cur == null){
			if(n == -1){
				// remove head
				return head.next;
			}else{
				// N > list.length 
				return head;
			} 
		}
		
		while(f_cur.next != null){
			f_cur = f_cur.next;
			b_cur = b_cur.next;
		}
		
		// remove the Nth element with b_cur pointer
		b_cur.next = b_cur.next.next;
		
		return head;
    }
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		//int [] num = {1, 2, 3, 4, 5};
		int [] num = {1};
		
		
		ListNode head = Utils.array2LinkedList(num);
		
		RemoveNthNode solution = new RemoveNthNode();
		
		Utils.printLinkedNodeList(solution.removeNthFromEnd(head, 1));
	}

}






