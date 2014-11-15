import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;


/**
 
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle. 

 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 14, 2014
 *
 */

public class Triangle {

	/**
	 * dynamic programming	 
	 */
    public int minimumTotal(List<List<Integer>> triangle) {
        
    	if(triangle == null || triangle.isEmpty()){
    		return 0;
    	}
    	
    	List<Integer> bottom = new LinkedList<Integer>();
    	bottom.add(triangle.get(0).get(0));
    	List<Integer> prePath = bottom;
    	
        for(int i=1; i<triangle.size(); i++){
        	List<Integer> curLevel = triangle.get(i);
        	
        	List<Integer> minPath = new LinkedList<Integer>();
        	
        	for(int j=0; j<curLevel.size(); j++){
        		
        		if(j == 0){
        			minPath.add(curLevel.get(0) + prePath.get(0));
        			
        		}else if(j == curLevel.size()-1){
        			minPath.add(curLevel.get(j) + prePath.get(j-1));
        			
        		}else{
        			int min = Math.min(prePath.get(j-1), prePath.get(j));
        			minPath.add(curLevel.get(j) + min);
        		}
            }
        	
        	prePath = minPath;
        }
        
        return Collections.min(prePath);
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int [][] A = {
		                {2},
		               {3,4},
		              {6,5,7},
		             {4,1,8,3}
		           };
		List<List<Integer>> input = Utils.array2ListOfList(A);
		
		Triangle solution = new Triangle();
		
		System.out.println(solution.minimumTotal(input));
	}

}





