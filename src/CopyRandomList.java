/**
 * A linked list is given such that each node contains an additional 
  	random pointer which could point to any node in the list or null.

	Return a deep copy of the list.
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 19, 2015
 *
 */
import java.util.Hashtable;

public class CopyRandomList {

	/**
	 * Time complexity O(N). Space complexity O(N).
	 
    public RandomListNode copyRandomList(RandomListNode head) {
    	Hashtable<Integer, RandomListNode> nodeTable = 
    			new Hashtable<Integer, RandomListNode>();
    	
    	RandomListNode pseudoHead = new RandomListNode(0);
    	RandomListNode iter = head, p = pseudoHead;
    	
    	// First round: copy all the nodes without assigning random pointers.
    	while(iter != null){
    		RandomListNode newNode = new RandomListNode(iter.label);
    		nodeTable.put(iter.label, newNode);

    		p.next = newNode;
    		p = p.next;
    		iter = iter.next;
    	}
    	
    	// Second round: assign the random pointers
    	iter = head;
    	while(iter != null){
    		if(iter.random != null){
    			nodeTable.get(iter.label).random = 
    					nodeTable.get(iter.random.label);
    		}
    		iter = iter.next;
    	}
    	
    	return pseudoHead.next;
    }
	*/
    
	/**
	 * Solution from the code handbook.
	 *  Associate naturally the original node and copy node in a single linked list.
	 *    Therefore, we don't need extra space to keep track of the nodes.
	 *    
	 * Time complexity O(N) (3 rounds of iteration), space complexity O(1).
	 */
    public RandomListNode copyRandomList(RandomListNode head) {
    	RandomListNode iter = head, next;
    	
    	// First round: make copy of each node, 
    	//		and link them together side-by-side in a single list. 
    	while(iter != null){
    		next = iter.next;
    		
    		RandomListNode copy = new RandomListNode(iter.label);
    		iter.next = copy;
    		copy.next = next;
    		
    		iter = next;
    	}
    	
    	// Second round: assign random pointers for the copy nodes.
    	iter = head;
    	while(iter != null){
    		if(iter.random != null){
    			iter.next.random = iter.random.next;
    		}
    		iter = iter.next.next;
    	}
    	
    	// Third round: restore the original list, and extract the copy list.
    	iter = head;
    	RandomListNode pseudoHead = new RandomListNode(0);
    	RandomListNode copy, copyIter = pseudoHead;
    	
    	while(iter != null){
    		next = iter.next.next;
    		
    		// extract the copy
    		copy = iter.next;
    		copyIter.next = copy;
    		copyIter = copy;
    	
    		// restore the original list
    		iter.next = next;
    		
    		iter = next;
    	}
    	
    	return pseudoHead.next;
    }
    
    
	public static void main(String[] args) {
	
	}

}
