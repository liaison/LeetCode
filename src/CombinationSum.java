/**
 * 

Given a set of candidate numbers (C) and a target number (T), 
	find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
	All numbers (including target) will be positive integers.
	Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
	The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7, A solution set is: 
[7] 
[2, 2, 3] 

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 13, 2015
 *
 */
import java.util.List;
import java.util.Arrays;
import java.util.LinkedList;

public class CombinationSum {

	private List<List<Integer>> res = new LinkedList<List<Integer>>();
	
	private void combinationSum(int [] candidates, LinkedList<Integer> vec,
								int start, int target){
		
		for(int i=start; i<candidates.length; ++i){
			if(candidates[i] < target){
				LinkedList<Integer> newVec = new LinkedList<Integer>();
				newVec.addAll(vec);
				newVec.add(candidates[i]);
				// Try a new combination, could repeat itself again. 
				combinationSum(candidates, newVec, i, target-candidates[i]);				
			}else if(candidates[i] == target){
				// Find a combination
				LinkedList<Integer> newVec = new LinkedList<Integer>();
				newVec.addAll(vec);
				newVec.add(candidates[i]);
				res.add(newVec);
			}else{
				// candidates[i] > target, no need to continue
				break;
			}
		}
	}
	
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
    	Arrays.sort(candidates);
    	LinkedList<Integer> vec = new LinkedList<Integer>();
    	this.combinationSum(candidates, vec, 0, target);
    	return res;
    }
    
    public static void main(String[] args) {
    	int [] candidates = {2, 3, 6, 7};
    	int target = 7;
    	
    	CombinationSum solution = new CombinationSum();
    	Utils.printListOfList(solution.combinationSum(candidates, target));
	}

}








