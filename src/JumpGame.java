

/**
 * 

Given an array of non-negative integers, 
you are initially positioned at the first index of the array.

Each element in the array represents your "maximum" jump length at that position, the play can take less steps.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
 
 * 
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 */

public class JumpGame {

	
		
	
	public boolean canJump_start_at(int [] A, int start){

    	int curr = start;
    	if(curr >= A.length-1){
    		return true;
    	}
    	
    	int jumpSteps = A[curr];
		
    	// Greedy heuristic, jump as far as possible.
		for(int i=jumpSteps; i>0; i--){
			if(canJump_start_at(A, curr+i)){
				return true;
			}
		}
		// None of the possible jumping strategies above works.
		return false;
	}
	
    
	/**
	 *  Step by step, each step decides the maximum distance one can reach. 
	 */
	public boolean canJump_dp(int [] A, int start){
		int curr = start;
    	if(curr >= A.length-1){
    		return true;
    	}
    	
    	// The starting point should not be ZERO, i.e. stopping.
    	if(A[0] == 0){
    		return false;
    	}
    	
    	for(int i=1; i<A.length-1; i++){
    		A[i] = Math.max(A[i-1]-1, A[i]);
    		
    		// Stuck here, can not proceed, then no
    		if(A[i] == 0){
    			return false;
    		}
    	}
    	
    	//proceed/jump to the end of the input.
    	return true;
	}

	public boolean canJump(int[] A) {
    	return canJump_dp(A, 0);
    }
    
    
    
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();

		JumpGame jp = new JumpGame();
		//int [] A = {6, 2, 1, 0, 4}; 
		
		// should return true, corner case.
		//int [] A = {0}; 
		
		// should return true, at element 2, take only one step instead of two.
		//int [] A = {2, 5, 0, 0};  
		
		// time limit
		//int [] A = {2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6};
		
		// should return false;
		int [] A = {0, 1};
		
		System.out.println(jp.canJump(A));
		
	    long stopTime = System.currentTimeMillis();
	    long elapsedTime = stopTime - startTime;
	    
	    System.out.println("time:" + elapsedTime);
	      
	}

}






