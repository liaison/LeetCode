import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;


/**
 *  utility function toolbox 
 *  
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 *
 */

public class Utils {

	public static char [][] string2matrix(String [] input){
		char [][] res = new char[input.length][];
		int i = 0;
		for(String s : input){
			res[i] = input[i].toCharArray();
			++i;
		}
		
		return res;
	}
	
	public static void printListOfStringArray(List<String[]> res){
		for(String [] array : res){
			for(int i=0; i<array.length; i++){
				System.out.println(array[i]);
			}
			System.out.println("====");
		}
	}
	
    public static void printListOfList(List<List<Integer>> result){
    
    	for(List<Integer> list : result){
    		System.out.print("[");
    		for(Integer i : list){
    			System.out.print(i + ",");
    		}
    		System.out.println("]");
    	}
    }
    
    /**
     * 
     * @param input
     * @return  ArrayList<LinkedList<Integer>> 
     */
    public static List<List<Integer>> array2ListOfList(int [][] input){
    	List<List<Integer>> matrix = new ArrayList<List<Integer>>();
    	
    	for(int i=0; i<input.length; i++){
    		List<Integer> array = new LinkedList<Integer>();
        	
    		for(int j=0; j<input[i].length; j++){
    			array.add(input[i][j]);
    		}
    		
    		matrix.add(array);
    	}
    	
    	return matrix;
    }
    
    public static void printList(List<Integer> list){
    	for(Integer iter : list){
    		System.out.print(iter + ",");
    	}
    	System.out.println();
    }
    
    
    public static void printArray(int [] array){
    	for(int i=0; i<array.length; i++){
    		System.out.print(array[i] + ",");
    	}
    	System.out.println("");
    }
    
    public static void printMatrix(int [][] matrix){
    	for(int i=0; i<matrix.length; ++i){
    		for(int j=0; j<matrix[i].length; ++j){
        		System.out.print(matrix[i][j] + ",");	
    		}

    		System.out.println("");
    	}
    	System.out.println("");
    }
    
    
    public static void printIntervalList(List<Interval> list){
    	for(Interval iter : list){
    		System.out.print("[" + iter.start + "," + iter.end + "]\t");
    	}
    	
    	System.out.println();
    }
    
    public static void printStringList(List<String> list){
    	for(String str : list){
    		System.out.println(str);
    	}
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
    
    public static void printTree(TreeNode root){
        if(root == null){
        	return;
        }
    	
        TreeNode lastLevel = root;
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
                
        StringBuffer levelStr = new StringBuffer();
        while(! queue.isEmpty()){
        	
        	TreeNode curr = queue.poll();
        	
        	String str = (curr == null)? "#" : String.valueOf(curr.val);
        	
        	levelStr.append(str);
        	
        	if(curr != null){
        		queue.offer(curr.left);
            	queue.offer(curr.right);
        	}
        	
        	if(curr == lastLevel){
        		lastLevel = queue.peekLast();
        		System.out.println(levelStr.toString());
        		levelStr.delete(0, levelStr.length());
        	}
        }
    
    }
}











