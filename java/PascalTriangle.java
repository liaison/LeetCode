import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * 
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Dec 03, 2014
 *
 */


public class PascalTriangle {

	/**
	 * Given an index k, return the kth row of the Pascal's triangle.

		For example, given k = 3, 	Return [1,3,3,1].

		Note:
			Could you optimize your algorithm to use only O(k) extra space?

	 * The nth row of pascal triangle will have the following format: 
	 * 	1 a(1) a(2) ... a(n) here we have 
	 *  a(1) = n; 
	 *  a(k+1) = a(k) * (n-k)/(k+1).
	 *  
	 */
	public List<Integer> getRow(int rowIndex) {
		List<Integer> res = new ArrayList<Integer>(rowIndex+1);
		res.add(1);
		if(rowIndex <= 0)
			return res; // early exit.
		
		res.add(rowIndex);
		int k=1;
		while(k < rowIndex){
			long ak = res.get(k);
			long next = ak * (rowIndex-k)/(k+1);
			res.add((int)next);
			++k;
		}
		
		return res;
	}
	
	/*
    public List<Integer> getRow(int rowIndex) {
    	ArrayList<Integer> res = new ArrayList<Integer>();
		ArrayList<Integer> preLevel = null;
		
    	for(int i=0; i<=rowIndex; i++){
    		for(int j=0; j<=i; j++){
    			if(j == 0 || j == i){
        			res.add(1);
        		}else{
        			res.add(preLevel.get(j) + preLevel.get(j-1));
        		}	
    		}
    		preLevel = res;
    		res = new ArrayList<Integer>();
        }
    	
    	return preLevel;
    }*/
	
    
    public List<List<Integer>> generate(int numRows) {
    	
    	LinkedList<List<Integer>> res = 
    			new LinkedList<List<Integer>>();
    	
    	for(int i=0; i<numRows; i++){
    		ArrayList<Integer> level = new ArrayList<Integer>(i+1);
    		
    		for(int j=0; j<=i; j++){
    			if(j == 0 || j == i){
    				level.add(1);
    			}else{
    				ArrayList<Integer> preLevel = 
    						(ArrayList<Integer>) res.get(i-1);
    				level.add(preLevel.get(j) + preLevel.get(j-1));
    			}
    		}
    		
    		res.add(level);
    	}
    	
    	return res;
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int numRows = 10; 
		PascalTriangle solution = new PascalTriangle();
		Utils.printListOfList(solution.generate(numRows));
		
		System.out.println("getRow");
		Utils.printList(solution.getRow(30));
	}

}
