/**
 * Given a linked list and a value x, 
     partition it such that all nodes less than x come before 
 		nodes greater than or equal to x.

	You should preserve the original relative order of the nodes 
		in each of the two partitions.

	For example,
		Given 1->4->3->2->5->2 and x = 3,
		return 1->2->2->4->3->5.
		
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 29, 2015
 *
 */
public class PartitionList {

    public ListNode partition(ListNode head, int x) {
    	ListNode pseudoHead = new ListNode(0);
    	
    	ListNode rightMost = pseudoHead;
    	ListNode end = rightMost;
    	ListNode iter = head;
    	while(iter != null) {
    		ListNode next = iter.next;
    		if(iter.val < x) {
    			// move the node right after rightMost node.
    			iter.next = rightMost.next;
    			rightMost.next = iter;
    			
    			if(end == rightMost){
    				end = iter;
    			}
    			
    			rightMost = iter;
    		}else {
    			end.next = iter;
    			end = iter;
    		}
    		
    		iter = next;
    	}
    	end.next = null; // mark the end;
    	
    	return pseudoHead.next;
    }
    
    public static void main(String[] args) {
    	int x = 3;  
    	ListNode list = Utils.array2LinkedList(new int[]{1, 4, 3, 2, 5, 2});
    	// expected: 1->2->2->4->3->5 
    	PartitionList solution = new PartitionList();
    	Utils.printLinkedNodeList(solution.partition(list, x));
	}

}
