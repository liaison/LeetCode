

/**
 * 
 * Find the contiguous subarray within an array (containing at least one number) 
 * which has the largest sum.
									  	         	
	For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
		the contiguous subarray [4,−1,2,1] has the largest sum = 6.
 * 
 * @author Lisong Guo<lisong.guo@me.com>
 * @date   Dec 11, 2014
 *
 */
public class MaximumSubarray {

	
	/**
	 * Divide and conquer or dynamic programming ? 
	 * This algorithm can do more than returning the maximum sum, 
	 * 	but also returning the subarray that has the maximum sum.  
	 */
    public int maxSubArray(int[] A) {
    	if(A.length == 0){
    		return 0;
    	}
    	
    	if(A.length == 1){
    		return A[0];
    	}
    	
        int max_sum = Integer.MIN_VALUE;
        
        int [] dp_array = new int[A.length]; 
    	
        for(int i=A.length-1; i>=0; i--){
        	dp_array[i] = A[i];
            
        	if(dp_array[i] > max_sum){
        		max_sum = dp_array[i]; 
        	}
        	
    		for(int j=i-1; j>=0; j--){
    			dp_array[j] = dp_array[j+1] + A[j];
    			 
    			if(dp_array[j] > max_sum){
    				max_sum = dp_array[j];
    			}
    		}
    	}
        
        return max_sum;
    	 
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int [] A = {-2,1,-3,4,-1,2,1,-5,4};
		//int [] A = {};
		MaximumSubarray solution = new MaximumSubarray();
		
		System.out.println(solution.maxSubArray(A));
	}

}
