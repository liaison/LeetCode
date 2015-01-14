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

	private void combinationSum2(int[] candidates, LinkedList<Integer> vec,
			int start, int target) {
		// Found the combination
		if(target == 0){
			LinkedList<Integer> newVec = new LinkedList<Integer>();
			newVec.addAll(vec);
			res.add(newVec);
			return;
		}
		
		for (int i = start; i < candidates.length; ++i) {
			if(candidates[i] > target){
				// No need to continue
				break;
			}else{  // candidates[i] <= target
				LinkedList<Integer> newVec = new LinkedList<Integer>();
				newVec.addAll(vec);
				
				// Find the starting point of next group
				int j = i+1;
				while(j < candidates.length && candidates[j] == candidates[i]){
					++j;
				}
				
				if (candidates[i] < target) {
					int newTarget = target;
					for(int k=0; k<j-i; ++k){
						newVec.add(candidates[i]);
						// Try a new combination.
						newTarget = newTarget - candidates[i];
						combinationSum2(candidates, newVec, j, newTarget);
					}
				} else if (candidates[i] == target) {
					// Found a combination
					newVec.add(candidates[i]);
					res.add(newVec);
				}
				
				// start from next group
				i = j-1;
			}
		}
	}
    
	/**
	 * https://oj.leetcode.com/problems/combination-sum-ii/
	 */
    public List<List<Integer>> combinationSum2(int[] num, int target) {
    	Arrays.sort(num);
    	
    	LinkedList<Integer> vec = new LinkedList<Integer>();
    	this.combinationSum2(num, vec, 0, target);
    	return res;    
    }
    
    public static void main(String[] args) {
    	//int [] candidates = {2, 3, 6, 7};
    	//int target = 7;
    	
    	//int [] candidates = {10,1,2,7,6,1,5};
    	//int target = 8;
    	// expected: [1, 7] [1, 2, 5] [2, 6] [1, 1, 6]
    	
    	//int [] candidates = {1, 1};
    	//int target = 1;  // expected: {1}
    	
    	//int [] candidates = {1, 1};
    	//int target = 2;  // expected: {1, 1}
    	
    	int [] candidates = {2, 2, 2};
    	int target = 4;
    	// expected: [2, 2]
    	
    	
    	CombinationSum solution = new CombinationSum();
    	Utils.printListOfList(solution.combinationSum2(candidates, target));
	}

}








