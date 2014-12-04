
/**
 * 

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 4, 2014
 *
 */
public class LinkedListIntersection {
    
	/**
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		ListNode iterA = headA, iterB = headB;
		int sizeA=0, sizeB=0;
		
		while(iterA != null){
			sizeA ++;
			iterA = iterA.next;
		}
		
		while(iterB != null){
			sizeB ++;
			iterB = iterB.next;
		}
	
		// reset the iteration pointers.
		iterA = headA;
		iterB = headB;
	
		// adjust the starting points to make them meet the joint point.
		if(sizeA < sizeB){
			int count = sizeB - sizeA;
			while(count > 0){
				iterB = iterB.next;
				count --;
			}
		}else if(sizeA > sizeB){
			int count = sizeA - sizeB;
			while(count > 0){
				iterA = iterA.next;
				count --;
			}
		}
		
		while(iterA != null && iterB != null){
			if(iterA == iterB){
				return iterA;
			}
			iterA = iterA.next;
			iterB = iterB.next;
		}
		
		return null;
    }
	*/
	
	/**
	 * 
Brute-force solution (O(mn) running time, O(1) memory):
For each node ai in list A, traverse the entire list B and check if any node in list B coincides with ai.

Hashset solution (O(n+m) running time, O(n) or O(m) memory):
Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.

Two pointer solution (O(n+m) running time, O(1) memory):
Maintain two pointers pA and pB initialized at the head of A and B, respectively. 
Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); 
similarly when pB reaches the end of a list, redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} 
and B = {2,4,9,11}, which are intersected at node '9'. 
Since B.length (=4) < A.length (=6), pB would reach the end of the merged list first, 
because pB traverses exactly 2 nodes less than pA does. 
By redirecting pB to head A, and pA to head B, we now ask pB to travel exactly 2 more nodes than pA would.
So in the second iteration, they are guaranteed to reach the intersection node at the same time.
If two lists have intersection, then their last nodes must be the same one. 
So when pA/pB reaches the end of a list, record the last element of A/B respectively. 
If the two last elements are not the same one, then the two lists have no intersections.

i.e. Put the list B ahead of A and the list A ahead of B, to make the two iterations 
	would meet at the joint point of the two lists.

	 * @param args
	 */
	
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		ListNode pA = headA, pB = headB;
		
		if(pA == null || pB == null)
			return null;
		
		int count = 0;
		// set a break out
		while(count < 3){
			if(pA == pB){
				// early exit.
				return pA;
			}
			
			pA = pA.next;
			pB = pB.next;
			
			if(pA == null){
				pA = headB;
				count ++;
			}
			
			if(pB == null){
				pB = headA;
				count ++;
			}
			
		}
		
		return null;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListNode a1 = new ListNode(1);
		ListNode a2 = new ListNode(2);
		ListNode a3 = new ListNode(3);
		
		a1.next = a2; 
		a2.next = a3;
		
		ListNode b1 = new ListNode(4);
		ListNode b2 = new ListNode(5);
		
		b1.next = b2;
		
		//b2.next = a1;  // intersection a2
		
		LinkedListIntersection solution = new LinkedListIntersection();
		ListNode joint = solution.getIntersectionNode(a1, b1);
		if(joint == null){
			System.out.println("None");	
		}
		else{
			System.out.println(joint.val);		
		}
	}

}












