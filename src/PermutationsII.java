import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;


/**

Given a collection of numbers that might contain duplicates, 
	return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

tag:  backtracking 

 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   28 Nov, 2014
 *
 */

public class PermutationsII {
	
	private List<List<Integer>> permList = new LinkedList<List<Integer>>();
	
	private void permutation_rec(
			int [] num, boolean [] bitMap, Integer [] res, int k){
		
		if(k == num.length){			
			// make a copy of the result, 
			//  cannot directly use the Arrays.asList() which would share one memory at the end. 
			ArrayList<Integer> onePerm = new ArrayList<Integer>();
			onePerm.addAll(Arrays.asList(res));
			permList.add(onePerm);
			return;
		}
		
		for(int i=0; i<num.length; i++){
			if(bitMap[i]){
				// the number has been taken.
				continue;
			}
			
			// take the number
			bitMap[i] = true;
			res[k] = num[i];
			
			permutation_rec(num, bitMap, res, k+1);
			
			bitMap[i] = false; // try another candidate
		}
	}
	
    public List<List<Integer>> permute(int[] num) {
    	boolean [] bitMap = new boolean[num.length];
    	Arrays.fill(bitMap, false);
    	
    	Integer [] res = new Integer[num.length];
    	
    	permutation_rec(num, bitMap, res, 0);
    	
    	return permList;
    }
    
    
	private void permutationUnique_rec(
			int [] num, boolean [] bitMap, Integer [] res, int k){
		
		if(k == num.length){			
			// make a copy of the result, 
			//  cannot directly use the Arrays.asList() which would share one memory at the end. 
			ArrayList<Integer> onePerm = new ArrayList<Integer>();
			onePerm.addAll(Arrays.asList(res));
			permList.add(onePerm);
			return;
		}
		
		for(int i=0; i<num.length; i++){
			
			if(bitMap[i]){
				// the number has been taken.
				continue;
			}
			
			if(i != num.length-1){
				if(num[i] == num[i+1]){
					bitMap[i] = true; 
					res[k] = num[i];
					
					permutationUnique_rec(num, bitMap, res, k+1);
										
					continue;
				}
			}
			
			// take the number
			bitMap[i] = true;
			res[k] = num[i];
			
			permutationUnique_rec(num, bitMap, res, k+1);
			
			bitMap[i] = false; // try another candidate
		}
	}
	
	
    public List<List<Integer>> permuteUnique(int[] num) {
    	Arrays.sort(num);
    	
    	boolean [] bitMap = new boolean[num.length];
    	Arrays.fill(bitMap, false);
    	
    	Integer [] res = new Integer[num.length];
    	
    	permutationUnique_rec(num, bitMap, res, 0);
    	
    	return permList;	
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] num = {1, 1, 1, 2};
		PermutationsII solution = new PermutationsII();
		
		List<List<Integer>> permList = solution.permuteUnique(num);
		
		Utils.printListOfList(permList);
	}

}









