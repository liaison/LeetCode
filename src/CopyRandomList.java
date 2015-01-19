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

	
    public RandomListNode copyRandomList(RandomListNode head) {
    	Hashtable<Integer, RandomListNode> nodeTable = 
    			new Hashtable<Integer, RandomListNode>();
    	
    	RandomListNode pseudoHead = new RandomListNode(0);
    	RandomListNode iter = head, p = pseudoHead;
    	
    	while(iter != null){
    		RandomListNode newNode = new RandomListNode(iter.label);
    		nodeTable.put(iter.label, newNode);

    		p.next = newNode;
    		p = p.next;
    		iter = iter.next;
    	}
    	
    	// second round: assign the random pointers
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
	
	public static void main(String[] args) {
	
	}

}
