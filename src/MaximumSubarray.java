

/**
 * 
 * Find the contiguous subarray within an array (containing at least one number) 
 * which has the largest sum.
									  	         	
	For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
           	
j=1	-2  1 -3  4 -1  2  1 -5 4     A 

j=2	-1 -2  1  3  1  3 -4 -1 
j=3 -4  2  0  5  2 -2  0 
j=4 
	
		the contiguous subarray [4,−1,2,1] has the largest sum = 6.
 * 
 * @author Lisong Guo<lisong.guo@me.com>
 * @date   Dec 11, 2014
 *
 */
public class MaximumSubarray {

	
	/**
	 * dynamic programming.  
	 */
    public int maxSubArray(int[] A) {
    	if(A.length == 0){
    		return 0;
    	}
    	
    	int [] dp = new int[A.length]; 
        
        int max_sum = A[0];
        dp[0] = A[0];
    	
        for(int i=1; i<A.length; i++){
            dp[i] = Math.max(dp[i-1] + A[i], A[i]);
            max_sum = Math.max(dp[i], max_sum);
    	}
        
        return max_sum;	 
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//int [] A = {-2,1,-3,4,-1,2,1,-5,4};
		int [] A = {1};
		MaximumSubarray solution = new MaximumSubarray();
		
		System.out.println(solution.maxSubArray(A));
	}

}
