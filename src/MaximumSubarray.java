

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
    	if(A.length == 1){
    		return A[0];
    	}
    	
        int max_i = 0, max_j = 0;
        int max_sum = Integer.MIN_VALUE;
        
        int [][] dp_matrix = new int[A.length][A.length]; 
    	
        for(int i=A.length-1; i>=0; i--){
        	dp_matrix[i][i] = A[i];
            
        	if(dp_matrix[i][i] > max_sum){
        		max_sum = dp_matrix[i][i]; 
        		max_i = max_j = i;
        	}
        	
    		for(int j=i-1; j>=0; j--){
    			dp_matrix[i][j] = dp_matrix[i][j+1] + A[j];
    			 
    			if(dp_matrix[i][j] > max_sum){
    				max_sum = dp_matrix[i][j];
    				max_i = i;
    				max_j = j;
    			}
    		}
    	}
        
        System.out.println(max_i + "," + max_j);
        return max_sum;
    	 
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int [] A = {-2,1,-3,4,-1,2,1,-5,4};
		//int [] A = {1};
		MaximumSubarray solution = new MaximumSubarray();
		
		System.out.println(solution.maxSubArray(A));
	}

}
