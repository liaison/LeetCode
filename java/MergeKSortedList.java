/**
 * 
 * Merge k sorted linked lists and return it as one sorted list. 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 19, 2015
 *
 */
import java.util.List;
import java.util.ArrayList;

import java.util.Comparator;

public class MergeKSortedList {
	
	/**  Complexity:  
	 * 		each element needs to iterator K times over the lists. 
	 * 	      There are n * K elements in total. 
	 * 		Therefore, the complexity n * K * K. 
	 * 	
    public ListNode mergeKLists(List<ListNode> lists) {
    	if(lists.size() == 1){
    		return lists.get(0);
    	}
    	
    	List<ListNode> pointerList = new ArrayList<ListNode>();
    	for(ListNode head : lists){
    		pointerList.add(head);
    	}
    	
    	int size = pointerList.size();
    	ListNode pseudoHead = new ListNode(0);
    	ListNode next = null, iter = pseudoHead;
    	
    	int nullCount, min, min_i;
    	
    	while(true){	
    		nullCount = 0;
    		min = Integer.MAX_VALUE;
    		min_i = 0;
    		
    		for(int i=0; i<size; ++i){
    			ListNode head = pointerList.get(i);
    			
    			if(head == null){
    				nullCount ++;
        			continue;	
    			}
    			
    			if(head.val <= min){
    				next = head;
    				min = head.val;
    				min_i = i;
    			}
    		}
    		
    		if(nullCount == size-1 || next == null){
    			break; // Reach all tails of the lists but one.
    		}
    		
    		iter.next = next;
    		iter = next;
    		
			pointerList.set(min_i, next.next); // move on
    	}
    	
    	iter.next = next;
    	
    	return pseudoHead.next;
    }
    */
    
    
	class NodeComparator implements Comparator<ListNode> {

		@Override
		public int compare(ListNode n1, ListNode n2) {
			return n1.val - n2.val;
		}
	}
	
	/**
	 * Solution from the code handbook, with priority queue
	   Complexity: the complexity of the insertion of each element is logK. 
	   Therefore, the overall complexity is n * K * logK.
	   
    public ListNode mergeKLists(List<ListNode> lists) {
    	if(lists == null || lists.size() == 0){
    		return null;
    	}
    	
    	NodeComparator nodeComparator = new NodeComparator();
    	PriorityQueue<ListNode> heap = 
    		new PriorityQueue<ListNode>(lists.size(), nodeComparator);
    	for(ListNode node : lists){
    		if(node != null){
        		heap.add(node);	
    		}
    	}
    	
    	ListNode pseudoHead = new ListNode(0);
    	ListNode p = pseudoHead;
    	
    	while(!heap.isEmpty()){
    		ListNode next = heap.poll();
    		p.next = next;
    		
    		if(next.next != null){
    			// add new element into the heap.
    			heap.add(next.next);
    		}
    		p = next;
    	}
    	
    	return pseudoHead.next;
    }
    */
    

    /**
     * Iterative merging, with the MergeTwoLists function.
     * The order of the merging matters a lot!
     * By pairing two equal-sized lists together, we minimize/optimize the
     *   average complexity of merging in each iteration.
     * While the number of the iteration remains the same, the overall
     *   average complexity of the function is optimal.
     */
    public ListNode mergeKLists(List<ListNode> lists) {
        if(lists == null || lists.size() == 0){
            return null;
        }

    	int begin = 0, end = lists.size() - 1;

    	while(end > 0){
            begin = 0;
            while(begin < end){
                lists.set(begin,
                          mergeTwoLists(lists.get(begin), lists.get(end)));
                ++begin;
                --end;
            }
        }
        return lists.get(0);
    }


    /**
     *  Merge two ordered lists into a single ordered list.
     *  Assume the two lists have the same length N.
     *  The minimal complexity of the function is O(N) in the case
     *    where the first element of a list is bigger than all elements in
     *    another list, then we could just go through one list and concatenate
     *    two lists together.
     *  While the maximal complexity of the function is still O(2N) ~= O(N),
     *    in the case where we have to go through both lists to combine them.
     */
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    	
        if(l1 == null)
            return l2;
    	if(l2 == null)
            return l1;

        ListNode l1_iter = l1, l2_iter = l2;

        ListNode pyseudoHead = new ListNode(0);
        ListNode res_iter = pyseudoHead;

        while(l1_iter != null && l2_iter != null) {

            if(l1_iter.val < l2_iter.val){
                res_iter.next = l1_iter;
                res_iter = l1_iter;
                l1_iter = l1_iter.next;
            } else {
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


    public static void main(String[] args) {
        //ListNode l1 = Utils.array2LinkedList(new int[]{});

        ListNode l1 = Utils.array2LinkedList(new int[]{1, 3, 4, 6});
        ListNode l2 = Utils.array2LinkedList(new int[]{2, 5, 7, 10});
        ListNode l3 = Utils.array2LinkedList(new int[]{9, 11});

        List<ListNode> lists = new ArrayList<ListNode>();
        lists.add(l1);
        lists.add(l2);
        lists.add(l3);

        MergeKSortedList solution = new MergeKSortedList();

        ListNode head = solution.mergeKLists(lists);
        Utils.printLinkedNodeList(head);
    }

}



