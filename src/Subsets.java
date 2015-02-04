
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
		List<List<Integer>> result = new LinkedList<List<Integer>>();
    	
		if(S.length == 0 || begin >= S.length){
			List<Integer> emptyList = new LinkedList<Integer>();
			result.add(emptyList);
			return result;
		}
		
		List<List<Integer>> rest = rec_subsets(S, begin+1);
		
		// Add the result from the rest of the problem.
		result.addAll(rest);
		
		for(List<Integer> elem : rest){
			LinkedList<Integer> newComb = new LinkedList<Integer>();
			newComb.add(S[begin]);
			newComb.addAll(elem);
			result.add(newComb);
		}
		
		return result;
	}
	
    public List<List<Integer>> subsets(int[] S) {
    	Arrays.sort(S);
		return this.rec_subsets(S, 0);
    }
	
    /**
     * Given a collection of integers that might contain duplicates, S, 
     * 		return all possible subsets.
	Note:
		Elements in a subset must be in non-descending order.
		The solution set must not contain duplicate subsets.
	For example,
		If S = [1,2,2], a solution is:

		[
  			[2],
  			[1],
  			[1,2,2],
  			[2,2],
  			[1,2],
  			[]
		]
     */
    public List<List<Integer>> subsetsWithDup(int[] num) {
        Arrays.sort(num);
        return rec_subsetsWithDup(num, 0);
    }
    
	private List<List<Integer>> rec_subsetsWithDup(int []num, int begin){
		List<List<Integer>> result = new ArrayList<List<Integer>>();
    	
		if(num.length == 0 || begin >= num.length){
			List<Integer> emptyList = new ArrayList<Integer>();
			result.add(emptyList);
			return result;
		}
		
		int next = begin+1;
		while(next < num.length && num[begin] == num[next]) ++ next;
		
		List<List<Integer>> rest = rec_subsetsWithDup(num, next);
		
		// Add the result from the rest of the problem.
		result.addAll(rest);

		List<Integer> dupSet = new ArrayList<Integer>();
		
		for (int j = begin; j < next; ++j) {
			dupSet.add(num[begin]);
			
			for (List<Integer> elem : rest) {
				ArrayList<Integer> newComb = new ArrayList<Integer>();
				newComb.addAll(dupSet);
				newComb.addAll(elem);
			
				result.add(newComb);
			}
		}

		return result;
	}

    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Subsets solution = new Subsets();	
		
		int [] S = {1, 2, 3};
		Utils.printListOfList(solution.subsets(S));
		
		int [] num = {1, 2, 2};
		Utils.printListOfList(solution.subsetsWithDup(num));
	}

}







