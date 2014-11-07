
/**
 * Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


 * @author	Lisong Guo <lisong.guo@inria.fr>
 * @date    Nov 06, 2014
 *
 */

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;


public class Subsets {

	/**
	 *  Divide and conquer 
	 */
	private List<List<Integer>> rec_subsets(int []S, int begin){
		List<List<Integer>> result = new ArrayList<List<Integer>>();
    	
		if(S.length == 0 || begin >= S.length){
			List<Integer> emptyList = new ArrayList<Integer>();
			result.add(emptyList);
			return result;
		}
		
		List<List<Integer>> rest = rec_subsets(S, begin+1);
		
		// Add the result from the rest of the problem.
		result.addAll(rest);
		
		for(List<Integer> elem : rest){
			ArrayList<Integer> newComb = new ArrayList<Integer>();
			newComb.addAll(elem);		
			elem.add(0, S[begin]);
			
			result.add(newComb);
		}
		
		return result;
	}
	
    public List<List<Integer>> subsets(int[] S) {
    	Arrays.sort(S);
		return this.rec_subsets(S, 0);
    }
	
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int [] S = {1};
		
		Subsets soltuion = new Subsets();
		
		Utils.printListOfList(soltuion.subsets(S));
		
	}

}







