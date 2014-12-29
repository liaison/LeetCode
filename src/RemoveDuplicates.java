

/**
 * 
Given a sorted array, remove the duplicates in place 
	such that each element appear only once and return the new length.

Do not allocate extra space for another array, 
	you must do this in place with constant memory.

For example,
	Given input array A = [1,1,2],
	Your function should return length = 2, and A is now [1,2].
	
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 29, 2014
 *
 */
public class RemoveDuplicates {

    public int removeDuplicates(int[] A) {
    	if(A.length == 0){
    		return 0;
    	}
    	
    	int fillCur = 0, iterCur = 1;
    	
    	for(; iterCur < A.length; ++iterCur){
    		if(A[iterCur] != A[fillCur]){
    			A[++fillCur] = A[iterCur];
    		}
    	}
    	
    	return fillCur+1;
    }
	
	public static void main(String[] args) {
		//int [] A = {1, 1, 1, 2, 2};
		int [] A = {};
		
		RemoveDuplicates solution = new RemoveDuplicates();
		
		int newLen = solution.removeDuplicates(A);
		System.out.println(newLen);
	
		for(int i=0; i<newLen; i++){
			System.out.print(A[i] + " ");
		}
	}

}
