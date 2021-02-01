import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;


/**
 * 
Given an array S of n integers, are there elements a, b, c, 
and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
	Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
	The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
 * 
 */

public class Sum {

	
    public List<List<Integer>> fourSum(int[] num, int target) {
        
    	Arrays.sort(num);
        
    	Utils.printArray(num);
    	
        LinkedList<List<Integer>> res = new LinkedList<List<Integer>>();
        Integer [] quad = {0, 0, 0, 0};
        int qi = 0;
        
        fourSum_rec(num, target, 0, quad, qi, res);
        return res;
    }
	
    private void fourSum_rec(
    		int [] num, int target, int start, 
    		Integer [] quad, int qi, 
    		LinkedList<List<Integer>> res){
    	
    	if(qi == 4){
    		if(target == 0){
    			List<Integer> newQuad = new ArrayList<Integer>(Arrays.asList(quad));
    			res.add(newQuad);
    		}
    		
    		return;
    	}
    
    	/*
    	if(num.length - start < 3 - qi){
    		return;
    	}*/
    	
    	while(start < num.length && num[start] <= target ){
    		quad[qi]=num[start];
    		fourSum_rec(num, target-num[start], start+1, quad, qi+1, res);		
    		// try another candidate.
    		start ++;
    	}
    }
    
    
    /**
     * Given an array S of n integers, are there elements a, b, c in S 
     * 	such that a + b + c = 0? Find all unique triplets in the array 
     * 	which gives the sum of zero.
	Note:
		Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
		The solution set must not contain duplicate triplets.
    	For example, given array S = {-1 0 1 2 -1 -4},

    	A solution set is:
    		(-1, 0, 1)
    		(-1, -1, 2)
     */
    public List<List<Integer>> threeSum(int[] num) {
        Arrays.sort(num);
        Utils.printArray(num);
        
        int size = num.length;
        
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        Integer [] comb = new Integer[] {0, 0, 0};
        int sum = 0;
        
        for(int i=0; i<size-2; ++i) {
        	sum = 0;
        	
        	if(num[i] > 0)
        		break;
        	
        	sum += num[i];
        	comb[0] = num[i];
        	
        	for(int j=i+1; j<size-1; ++j) {
        		
        		sum += num[j];
        		comb[1] = num[j];
        		
        		for(int k=j+1; k<size; ++k) {
        			if(sum + num[k] == 0){
        				comb[2] = num[k];
        				ArrayList<Integer> newComb = 
        						new ArrayList<Integer>(Arrays.asList(comb));
        				res.add(newComb);
        			}
        		}
        		
        		sum -= num[j];
        	}
        	
        	sum -= num[i];
        }
        
        return res;
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//int [] S = {1, 0, -1, 0, -2, 2};
		//int target = 0;
		
		int [] S = {1, 0, -1, 0, -2, 2, -3, 3};
		int target = 0;
		
		//int [] S= {-497,-480,-477,-470,-452,-448,-440,-412,-390,-381,-372,-372,-369,-366,-355,-346,-340,-3, 37,-322,-321,-311,-296,-258,-249,-248,-232,-215,-199,-174,-154,-128,-122,-122,-117,-115,-113,-110,-89,-86,-84,-78,-71,-69,-53,-49,-35,-25,-21,-7,3,7,21,25,30,47,52,81,84,87,91,96,157,161,167,178,184,210,217,228,236,274,277,283,286,290,301,302,341,352,354,361,367,384,390,412,421,458,468,483,484,486,487,490,491};
		//int target = 8377;

		Sum solution = new Sum();
		
		Utils.printListOfList(solution.fourSum(S, target));
		
		
		int [] num = {-1, 0, 1, 2, -1, -4};
		System.out.println("ThreeSum:");
		Utils.printListOfList(solution.threeSum(num));
	}

}





