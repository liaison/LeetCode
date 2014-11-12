import java.util.List;


/**
 *  utility function toolbox 
 *  
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 *
 */

public class Utils {

	
    public static void printListOfList(List<List<Integer>> result){
    
    	for(List<Integer> list : result){
    		System.out.print("[");
    		for(Integer i : list){
    			System.out.print(i + ",");
    		}
    		System.out.println("]");
    	}
    }
    
    
    public static void printArray(int [] array){
    	for(int i=0; i<array.length; i++){
    		System.out.print(array[i] + ",");
    	}
    	System.out.println("");
    }
    
    
    public static void printIntervalList(List<Interval> list){
    	for(Interval iter : list){
    		System.out.print("[" + iter.start + "," + iter.end + "]\t");
    	}
    	
    	System.out.println();
    }
    
    public static ListNode array2LinkedList(int [] num){
    	if(num.length == 0){
    		return null;
    	}
    	
    	ListNode head = new ListNode(num[0]);
    	ListNode iter = head;
    	
    	for(int i=1; i<num.length; i++){
    		ListNode newNode = new ListNode(num[i]);
    		iter.next = newNode;
    		iter = newNode;
    	}
    	
    	return head;
    }
    
    public static void printLinkedNodeList(ListNode head){
    	if(head == null){
    		System.out.println("Empty List.");
    		return;
    	}
    	
    	while(head != null){
    		System.out.print(head.val + ",");
    		head = head.next;
    	}
    	
    	System.out.println("");
    }
    
}











