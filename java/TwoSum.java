import java.util.Hashtable;


/**
 * 
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

	Input: numbers={2, 7, 11, 15}, target=9
	Output: index1=1, index2=2

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 30, 2014
 *
 */

public class TwoSum {

    public int[] twoSum(int[] numbers, int target) {
    	Hashtable<Integer, Integer> numTable = 
    			new Hashtable<Integer, Integer>();
    	int [] res = new int[2];
    	
    	for(int i=0; i<numbers.length; ++i){
    		Integer index1 = numTable.get(target - numbers[i]);
    		if(index1 != null){
    			res[0] = index1+1;
    			res[1] = i+1;
    			break;
    		}
    		
    		numTable.put(numbers[i], i);
    	}
    	
    	return res;
    }
    
	public static void main(String[] args) {
		int [] numbers={2, 7, 11, 15};
		TwoSum solution = new TwoSum();
		int target = 9;
		
		int [] res = solution.twoSum(numbers, target);
	
		System.out.println(res[0] + "," + res[1]);
	}

}
