
/**
 * 
Given an unsorted integer array, find the first missing positive integer.

For example,
	Given [1,2,0] return 3,
	and [3,4,-1,1] return 2.

	Your algorithm should run in O(n) time and uses constant space.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 28, 2014
 *
 */
public class MissingPositive {
    
	/**
	 * https://oj.leetcode.com/discuss/4220/a-very-nice-solution-from-ants-aasma-%40stackoverflow
	 * 
	 */
	public int firstMissingPositive(int[] A) {
		int n = A.length; 
		
		for(int i=0; i<n; i++){
			int num = A[i];
			
			// in-place ordering. The complexity O(N).
			while(num > 0 && num < n && A[num-1] != num){
				// swap the values between A[i] and A[num-1] 
				int temp = A[i];
				A[i] = A[num-1];
				A[num-1] = temp;
				
				num = A[i];
			}
		}
		
		for(int i=0; i<n; ++i){
			if(A[i] != i+1){
				return i+1;
			}
		}
		
		return n+1;
	}
	
	public static void main(String[] args) {
		//int [] num = {1, 2, 0};  // expect 3
		int [] num = {3, 4, -1, 1};  // expect 2
		//int [] num = {0};
		
		MissingPositive solution = new MissingPositive();
		System.out.println(solution.firstMissingPositive(num));
	}

}











