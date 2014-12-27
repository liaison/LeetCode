

/**
 * 
 * 
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
	Your algorithm should have a linear runtime complexity. 
	Could you implement it without using extra memory?

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 27, 2014
 *
 */
public class SingleNumber {

    public int singleNumber(int[] A) {
    	int single = 0x0;
    	
    	for(int i=0; i<A.length; i++){
    		single = single ^ A[i];
    	}
    	
    	return single;
    }
    
	public static void main(String[] args) {
		int [] num = {1, 1, 2, 1111, 2, 3, 3};
		
		SingleNumber solution = new SingleNumber();
		
		System.out.println(solution.singleNumber(num));
	}

}
