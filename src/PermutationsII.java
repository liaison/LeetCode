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
	
	/**
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
    */
	
	/**
	 * An inspired solution from codereview.stackexchange.com
	 */
	
	private void permute_rec(int[] num, int currIndex, List<List<Integer>> permList){
		if(currIndex == num.length - 1){
			ArrayList<Integer> onePerm = new ArrayList<Integer>();
			for(int i : num) onePerm.add(i);
			permList.add(onePerm);
			return;
		}
		
		permute_rec(num, currIndex+1, permList);
		
		for(int i=currIndex+1; i<num.length; i++){
			
			if(i == num.length -1){
				
				int swap = num[i-1];
				num[i-1] = num[currIndex];
				num[currIndex] = swap;
				
				permute_rec(num, currIndex+1, permList);
				break;
			}
			
			int swap = num[i];
			num[i] = num[currIndex];
			num[currIndex] = swap;
			
			permute_rec(num, currIndex+1, permList);
		}
	}
	
	public List<List<Integer>> permute(int[] num){
		List<List<Integer>> permList = new ArrayList<List<Integer>>();
		permute_rec(num, 0, permList);
		return permList;
	}
    
	
	private List<List<Integer>> permList = new LinkedList<List<Integer>>();

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
		int [] num = {1, 2, 3};
		PermutationsII solution = new PermutationsII();
		
		List<List<Integer>> permList = solution.permute(num);
		
		Utils.printListOfList(permList);
	}

}









